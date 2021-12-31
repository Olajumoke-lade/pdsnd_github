import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_filter = ['all', 'january', 'february', 'march',
                    'april', 'may', 'june']
day_filter = ['all', 'sunday', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    city_filter = ['chicago', 'new york city', 'washington']
    city = input("Please input your city name. The available cities are Chicago, New york city and Washington.\n").lower().strip()
    while city not in city_filter:
        print('You have entered an incorrect input for city')
        city_loop = input('Do you wish to re-enter a correct city input?\n Enter Yes or any other character to exit\n').lower().strip()
        if city_loop == 'yes':
            city = input("\nFilter data by city\n. Available cities are Chicago, New York city or Washington\n").lower().strip()
            continue
        else:
            city = city_loop
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    month = input("Input the month between January to June.\n").lower().strip()
    while month not in month_filter:
        print('You have entered an incorrect input')
        month_loop = input('Do you want to re-enter a correct input for month?\n Enter yes or any other character to exit\n').lower().strip()
        if month_loop == 'yes':
            month = input("\nYou can now enter the correct month\n. Input 'all' to view all available month or input any month between january to june").lower().strip()
            continue
        else:
            month = month_loop
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)  
    day = None
    day = input("Input the day of the week.\n").lower().strip()
    while day not in day_filter:
        print('You have entered an incorrect input')
        day_loop = input('Do you wish to re-enter a correct day input?\n Enter yes or any other character to exit\n').lower().strip()
        if day_loop == 'yes':
            day = input("\nYou can now enter the correct day of the week\n. Input 'all' to view all days of the week or input any day of the week").lower().strip()
            continue
        else:
            day = day_loop
            break       

    print('-'*40)
    return city, month, day
    

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
    print()
    print(" Filters applied : "
          "[ {}, {}, {}] ".format(city, month, day).center(40, '*'))
    print()
    
    # load data file into a dtaframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    popular_month_name = months[popular_month - 1].title()
    
    
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour)
    print('Most Popular Month:', popular_month_name)
    print('Most Popular Day:', popular_day_of_week)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    count_popular_start_station = df['Start Station'].value_counts()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    count_popular_end_station = df['End Station'].value_counts()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['Start_to_End'] = df['Start Station'] + ' ' + 'to'+ ' '+ df['End Station']
    popular_start_to_end_station = df['Start_to_End'].mode()[0]
    count_popular_start_to_end_station = df['Start_to_End'].value_counts()[0]
    
    print("Most commonly used start station:\n", popular_start_station, "with a count of", count_popular_start_station)
    print("Most commonly used end station:\n", popular_end_station, "with a count of", count_popular_end_station)
    print("Most commonly used start to end station:\n", popular_start_to_end_station, "with a count of", count_popular_start_to_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    print("total travel time is\n", total_travel_time, "hours")
    print("mean travel time is\n", mean_travel_time, "hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender'in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        pass

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        
        print("Earliest year of birth:\n", earliest_birth_year)
        print("Most recent year of birth:\n", most_recent_birth_year)
        print("Most common year of birth:\n", most_common_birth_year)
    else:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def rawdata(df):
    
    start = 0
    end = 5
    
    while input("Enter 'Yes' to see 5 lines of the raw data.\n If uninterested, press 'no' to continue\n").lower().strip() == 'yes':
        print(df.iloc[start:end,:])
        start +=5
        end +=5

def main():
    while True:
        city, month, day = get_filters()
        if city in CITY_DATA and month in month_filter and day in day_filter:
            df = load_data(city, month, day)
            
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            rawdata(df)
        else:
            pass

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
