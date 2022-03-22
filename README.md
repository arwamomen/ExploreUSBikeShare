# ExploreUSBikeShare
This is a student project created as part of Udacity's Data Analysis Professional Nanodegree Program (egFWD initiative). 

In this project, Python was used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. The code will import the data and answer interesting questions about it by computing descriptive statistics. The script takes in raw input from the terminal to apply filters to the data, thereby creating an interactive experience and presenting descriptive statistics. 

## Download bikeshare datasets

Download data for:
- Chicago from https://ride.divvybikes.com/system-data, and re-name the CSV file to 'chicago.csv'
- New York City from https://ride.citibikenyc.com/system-data, and re-name the CSV file to 'new_york_city.csv'
- Washington from https://ride.capitalbikeshare.com/system-data, and re-name the CSV file to 'washington.csv'

## Statistics Computed

The code provides the following information:

#1 Popular times of travel (i.e., occurs most often in the start time)

most common month
most common day of week
most common hour of day

#2 Popular stations and trip

most common start station
most common end station
most common trip from start to end (i.e., most frequent combination of start station and end station)

#3 Trip duration

total travel time
average travel time

#4 User info

counts of each user type
counts of each gender (only available for NYC and Chicago)
earliest, most recent, most common year of birth (only available for NYC and Chicago)

## User prompts:

1.	Would you like to see data for Chicago, New York, or Washington?
2.	Would you like to filter the data by month, day, or not at all?
3.	(If they chose month) Which month - January, February, March, April, May, or June?
4.	(If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.
