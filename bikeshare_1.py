import pandas as pd
import numpy as np
import time
from datetime import date


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

short_day_name=['mon','tues','wed','thurs','fri','sat','sun']
full_day_name=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

days_names_dict=dict(zip(short_day_name,full_day_name))

short_month_name=['jan','feb','mar','apr','may','jun']
full_month_name=['January','February','March','April','May','June']

months_names_dict=dict(zip(short_month_name,full_month_name))

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city=input('Which city would you like to analyze data for? Type New York City, Chicago, or Washington: ').lower()
            if city in CITY_DATA:
                print("You selected {}".format(city.title()))
                break
            else:
                print("Invalid city name. Try again\n")
    # get user input for month (all, january, february, ... , june)
    while True:
        month_name=input('Would you like to explore bike usage data in a specific month or in all months?\nType Jan, Feb, Mar, Apr, May, Jun, or all: ').lower()
        if month_name in short_month_name:
            month_name=months_names_dict[month_name]
            print("You selected {}".format(month_name.title()))
            break
        elif month_name=='all':
            print("You selected all months")
            break
        else:
            print("Invalid month name. Try again\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        weekday=input('Would you like to explore bike usage data in a specific weekday or throughout the week?\nType Mon, Tues, Wed, Thurs, Fri, Sat, Sun, or all: ').lower()

        if weekday in short_day_name:
            weekday=days_names_dict[weekday]
            print("You selected {}".format(weekday.title()))
            break
        elif weekday=='all':
            print("You selected all days of the week")
            break
        else:
            print("Invalid weekday name. Try again\n")

    print('-'*40)
    return city, month_name, weekday


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    filename=CITY_DATA[city]
    df = pd.read_csv(filename)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    #df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = full_month_name.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel considering the filtered data...\n')
    start_time = time.time()

    # display the most common month
    busiest_month=full_month_name[df['month'].mode()[0]-1]
    print('The busiest month is: ',busiest_month)
    print()

    # display the most common day of week
    busiest_weekday=df['day_of_week'].mode()[0]
    print('The busiest weekday is: ',busiest_weekday)
    print()

    # display the most common start hour
    busiest_hour=df['Start Time'].dt.hour.mode()[0]
    print('The busiest hour is: ',busiest_hour,':00:00 (24-hr)')
    print()

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    busiest_start_dock=df['Start Station'].mode()[0]
    print('The most popular start station is: ',busiest_start_dock)
    print()

    # display most commonly used end station
    busiest_end_dock=df['End Station'].mode()[0]
    print('The most popular end station is: ',busiest_end_dock)
    print()

    # display most frequent combination of start station and end station trip
    df['Route']=df['Start Station']+" to "+df['End Station']
    busiest_start_stop=df['Route'].mode()[0]
    print('Most trips are from',busiest_start_stop)
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_dur=round(df['Trip Duration'].sum(),1)
    print('Total Trip Duration is {} seconds, or {} minutes, or equivalently, {} hours'.format(total_trip_dur,round(total_trip_dur/60,1),round(total_trip_dur/(60*60),1)))
    print()

    # display mean travel time
    mean_trip_dur=round(df['Trip Duration'].mean(),1)
    print('Mean Trip Duration is {} seconds, or {} minutes, or equivalently, {} hours'.format(mean_trip_dur,round(mean_trip_dur/60,1),round(mean_trip_dur/(60*60),1)))
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of User Types:\n")
    print(df[['User Type']].value_counts())
    print("{} trips had unidentified user type".format(df['User Type'].isnull().sum()))
    print()

    if city !='washington':
        # Display counts of gender
        print("Count of Male and Female users:\n")
        print(df[['Gender']].value_counts())
        print("{} trips were made by users who did not disclose their gender".format(df['Gender'].isnull().sum()))
        print()

        # Display earliest, most recent, and most common year of birth
        df['Birth Year']=df['Birth Year']
        earliest_yob=round(df['Birth Year'].min())
        latest_yob=round(df['Birth Year'].max())
        popular_yob=round(df['Birth Year'].mode()[0])

        currentyear=date.today().year
        print("Year of Birth Statistics:\n")
        print("The oldest user was born in: ",earliest_yob,"--> {} years old".format(currentyear-earliest_yob))
        print("The youngest user was born in: ",latest_yob,"--> {} years old".format(currentyear-latest_yob))
        print("Most users were born in: ",popular_yob,"--> {} years old".format(currentyear-popular_yob))
        print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month_name, weekday = get_filters()
        df = load_data(city, month_name, weekday)
        print("{} records found".format(df.shape[0]))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            viewraw=input('\nWould you like to view 5 random rows of the raw data? [y/n]\n')
            if viewraw.lower()=='y':
                pd.set_option('display.max_columns', 2000)
                print(df.sample(5))
            else:
                break

        restart = input('\nWould you like to restart? Enter [y/n].\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
