# Fetch Backend Project
Hi, this repositiory contains my work for the backend internship at Fetch.

**Assignment 1** is containined in spend_points.py

**Assignment 2** is containined in summary.txt

## Instructions to run spend_points.py
### Python Setup
If you have never run a python program before you can follow [this guide](https://realpython.com/installing-python/) to set up python from realpython.com

### Installing Dependencies
Once you have python set up on your local machine you should will have to install pandas, a python module, before you can successfully run the code.
To do that run the following command in your command line:
>pip install -r requirements.txt

This will install the most recent version of pandas

### Running the program
Now you are ready to run the program. You can use the following command on the command line:
>python3 spend_points.py [number of points to spend (int)] [csv file]

For Example:
> python3 spend_points.py 5000 https://fetch-hiring.s3.amazonaws.com/transactions.csv

This should output the following string to the command line:
>{
     "DANNON": 1000
     "MILLER COORS": 5300
     "UNILEVER": 0
}
