# Election Analysis

## Overview

### Purpose
The purpose of the PyPoll with Python analysis is to assist Tom and his manager, Seth, in auditing the results of a recent election to send to the election commission.

### Background
Seth and Tom are requesting that an audit be completed on the election results and data regarding the specific counties outcomes to send to the election commission. In order to do this, we used Python to sort through the data and find the outcomes.

## Results
- How many votes were cast in this congressional election?
  - There were 369,711 total votes cast in the election.
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  - Arapahoe County had a total of **24,801 votes cast**. These votes accounted for **6.7% of the total votes** cast in the election
  - Denver County had a total of **306,055 votes cast**. These votes accounted for **82.8% of the total votes** cast in the election.
  - Jefferson County had a total of **38,885 votes cast**. These votes accounted for **10.5% of the total votes** cast in the election.
- Which county had the largest number of votes?
  - Denver county had the largest number of votes in the elections with 306,055 total votes cast.
- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  - Charles Casper Stockham recieved **85,213 total votes**. His votes account for **23.0% of the total votes** cast in the election.
  - Diana DeGette recieved **272,892 total votes**. Her votes account for **73.8% of the total votes** cast in the election.
  - Raymon Anthony Doane recieved **11,606 total votes**. His votes account for **3.1% of the total votes** cast in the election.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  - Diana Degette won the election with 272,892 votes and 73.8% of the total votes in the election.

## Election Audit Summary
Assuimg the data provided is in a similar format this script can be used again with upcoming elections! The script does not need to be modified for a similar data set. However some changes can be made to make it easier to use. Currently the script will pull data from a CSV file in a specific directory that does not exist on every machine. A good change that can be made is adding something like:
```python
file_path = raw_input("Please drag in the file you want to use: ")
```
This way the user doesn't have worry about the code breaking if they don't have the folders the script looks for. Antoher change could be adding a method of transforming the data if it has the same information but arranged in different columns.

## Resources
- Data source: election_results.csv
- Software: Python 3.8.3, Visual Studio Code 1.47.3
