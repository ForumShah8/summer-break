# summer-break
------- Environment Setup, Running and Testing the Code -------
To test this code you need bash setup and working. 
Currently I have tested the code in Ubuntu 23.04 version.

>>>> Steps to install Python and Flask <<<<

To install Python type in the following commands in your terminal:

``` 
sudo apt update
```
```
sudo apt install python3
```

To install Flask, type in the following commands in your terminal:

```
sudo apt install python3-venv
```
Navigate inside the current folder and then type these commands:

```
python3 -m venv venv 
```

```
source venv/bin/activate
```

```
pip install Flask
```

>>>> Steps to run and test the code: <<<<

Make sure the data.csv, test.sh and the solution.py file are all in same folder.
Navigate to the directory containing these files and open the terminal there.
Start the Flask app by running the following command in terminal:

```
source venv/bin/activate
```

```
python3 solution.py
```
The Flask development server has now started and is successfully running on 'http://127.0.0.1:5000' by default.

Now to test the endpoints open another terminal within this folder and type in the following command:

```
source ./test.sh
```

this will execute the test.sh file which has the commands to test the endpoints "/transactions" and "/report".

An output like this will be produced on your terminal.

![img.png](img.png)

>>>> Current Approach to the Solution and any Assumptions made: <<<<

Current solution has 2 API endpoints setup: 
  The '/transactions' endpoint, takes .csv file as input, parses it's data and stores it.
    While parsing the data from CSV file, only those lines which have 4 fields available (`Date, Type, Amount($), Memo`) will be parsed and stored. Rest all lines which do not match this     format will be ignored.
    The Parsed data from the CSV is stored in a Nested List.

  The '/report' endpoint, gives user a tally report of gross revenue, total expenses and net revenue (gross revenue - total expenses) in a JSON format. 
    Whenever this endpoint is called we take the data stored in Nested List, identify each entry as Income/Expenses, and perform calculations for gross revenue, total expenses and net        revenue.

  By default, if the data row contains 4 fields, it is assumed that these are all valid fields following the given format (Date, Type, Amount($), Memo).

>>>> Shortcomings of this project and scope of improvement <<<<

The user can currently parse only one csv file at a time. If the user tries to parse multiple files one after the other, the data parsed from the previous files will be lost.

In future, a feature supporting multiple files parsing can be added and also the csv file parsing can be refined more to make sure only the relevant data is being parsed.
