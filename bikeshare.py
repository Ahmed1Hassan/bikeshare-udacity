import time
import pandas as pd

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in city_data.keys():
        print("First, you need to choose the city")
        print("So Would you like to see data for Chicago, New York City, or Washington?")
        city = input().lower()

        if city not in city_data.keys():
            print("OOPS! Sorry, this city's data is not available with us")
            print("Let's try again")

    # get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in month_list:
        print("Now wer are done with the city, let's move to the date by specifying the month")
        print("Which month are you looking for? \
        \n(January - February - March - April - May - June)")
        month = input().lower()

        if month not in month_list:
            print("mmmm, it seems you are attracted to the data not available with us")
            print("from January to June, Please pick between them")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in day_list:
        print("Last thing, Are you interested in a specific week day?")
        print("if not, you can select the whole week by typing 'all'")
        day = input().lower()

        if day not in day_list:
            print("invaild selection, Pick again please")

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
    #Load data for city
    print("\nLoading data...")
    df = pd.read_csv(city_data[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name
    df['hour'] = df['Start Time'].dt.hour

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df




def time_stats(df):
    """Display statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is {}".format(most_common_month))

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week is {}".format(most_common_day_of_week))

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print("The most common start hour of day is {}".format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Display statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station: {}".format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station: {}".format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
        .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Display statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_minute, total_second = divmod(total_travel_time, 60)
    total_hour, total_minute = divmod(total_minute, 60)
    print("The total travel time is {} hours, {} minutes and {} seconds.\
    ".format(total_hour, total_minute, total_second))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_minute, mean_second = divmod(mean_travel_time, 60)
    mean_hour, total_minute = divmod(mean_minute, 60)
    print("The mean travel time is {} hours, {} minutes and {} seconds.\
    ".format(mean_hour, mean_minute, mean_second))

    # display max travel time
    max_travel_time = df['Trip Duration'].max()
    max_minute, max_second = divmod(max_travel_time, 60)
    max_hour, max_minute = divmod(max_minute, 60)
    print("The max travel time is {} hours, {} minutes and {} seconds.\
    ".format(max_hour, max_minute, max_second))

    # display the total trip duration for each user type
    total_trip_duration = round(df['Trip Duration'].mean())
    total_trip_minute, total_trip_second = divmod(total_trip_duration, 60)
    total_trip_hour, total_trip_minute = divmod(total_trip_minute, 60)
    print("The total travel time for each user type is {} hours, {} minutes and {} seconds.\
    ".format(total_trip_hour, total_trip_minute, total_trip_second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Display statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("The counts of User Types are \n{}".format(user_type))

    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("The counts of User Gender are \n{}".format(gender))
    except:
        print("\nThere is no 'Gender' data in this file.")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        most_recent_recet = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print("\nThe earliest year of birth: {} \
        \nThe most recent year of birth: {}\
        \nThe most common year of birth: {}\
        ".format(earliest_year, most_recent_recet, most_common_year))
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def display_data(df):
    """Display raw bikeshare data."""
    row_length = df.shape[0]

    #iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        yes = input("\nWould you like to examine this raw bike trip data?\
        \nType 'yes' or 'no'")
        if yes.lower() != 'yes':
            break

        row_data = df.iloc[i: i + 5]
        print(row_data)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
