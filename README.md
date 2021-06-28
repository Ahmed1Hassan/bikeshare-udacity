# Explore US Bikeshare Data
Udacity project using pandas library in Python for US bikeshare data exploration.

## Project Overview:
This project focuses on pandas library usage and simple statistics methods to perform analysis on the bikeshare data from three major U.S. cities - Chicago, Washington, and New York City - to display information such as most popular days or most common stations.

## Running the program:
You can input 'python bikeshare.py' in your terminal to run this program. I use Anaconda's command prompt on a Windows 10 machine.

## Program Details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

### Popular times of travel (i.e., occurs most often in the start time):
- Most common month
- Most common day of week
- Most common hour of day
### Popular stations and trip:
- Most common start station
- Most common end station
- Most common trip from start to end (i.e., most frequent combination of start station and end station)
### Trip duration:
- Total travel time
- Average travel time
### User info:
- Counts of each user type
- Counts of each gender (only available for NYC and Chicago)
- Earliest, most recent, most common year of birth (only available for NYC and Chicago)
- Finally, the user is prompted with the choice of restarting the program or not.

## Requirements:
- Language: Python 3.6 or above
- Libraries: pandas, time

## Project Data:
- chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

- new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

- washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. No- te: This does not include the 'Gender' or 'Birth Year' data.

## Author:
*Ahmed Hassan*

## Acknowledgements:
- Udacity - Udacity's Data Analyst Nanodegree program
- pandas docs - pandas documentation
