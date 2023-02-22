import pandas as pd
import sys


def spend_points(points_to_spend: str, points_log_file: str) -> str:
    """
    Takes in a points_to_spend value and a path to a CSV file containing point logs.
    The method spends the given number of points by iterating through the CSV and subtracting
    points until the total number of points to spend is reached. The method ensures that the
    oldest points are spent first, and no payer's points go negative. Finally, the method
    groups the remaining points by payer and returns a formatted string showing each payer's
    remaining points.

    Args:
        points_to_spend (str): The number of points to spend, passed as a string.
        points_log_file (str): The path to the CSV file containing point logs.


    Returns:
        A formatted, JSON-like string showing each payer's remaining points after the points are spent.
    """
    # Ensure that the points given from the command line is a valid integer
    try:
        points_to_spend = int(points_to_spend)
    except ValueError:
        print(
            "Invalid input for points to spend. Points to spend must be an integer value."
        )

    points_log = pd.read_csv(points_log_file)

    # take the oldest entry first
    points_log = points_log.sort_values(by="timestamp")

    # we want to iterate over each row
    for index, row in points_log.iterrows():
        points_avalible = row["points"]
        # case 1: this row has enough points such that we can just subtract from this row to finish spending
        if points_avalible >= points_to_spend:
            points_log.loc[index, "points"] = points_avalible - points_to_spend
            break
        # case 2: the row does not have enough points, so spend all of the points from this row, 
        # update our points_to_spend and go to the next row
        else:
            points_to_spend -= points_avalible
            points_log.loc[index, "points"] = 0

    # group based on the payer and sum the remaining points
    grouped = points_log.groupby("payer").sum(numeric_only=True)
    grouped = grouped.reset_index()

    return _format_string(grouped)


def _format_string(df: pd.DataFrame) -> str:
    """
    This is a helper method to convert the grouped dataframe to a string in JSON-like format.
    It iterates over each row in the data frame and extracts the payer and points.

    Args:
        df (pandas DataFrame)

    Returns:
        String: with each row of the form "{payer}: {points}
    """
    return_string = "{\n"
    # loop through the dataframe and extract the payer and points information 
    # and add it to the return string
    for index, row in df.iterrows():
        return_string += f"     \"{row['payer']}\": {row['points']}\n"
    return_string += "}"
    return return_string


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "This program takes in two arguments: the number of points to spend (int)"
            + "and the file name of the points log"
        )
        sys.exit(1)

    points_to_spend = sys.argv[1]
    points_log_file = sys.argv[2]

    # run the program with the given inputs
    remaining_points = spend_points(points_to_spend, points_log_file)
    print(remaining_points)
