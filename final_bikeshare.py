import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#created a list of names which is used by a while loop to determine if the user has entered a correct value
city_names = ['chicago', 'new york city', 'washington']
month_names = ['january', 'february', 'march', 'april', 'may', 'june','july','august','all']
day_names = ['monday','tuesday','wednesday', 'thursday', 'friday','saturday','sunday','all']


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')


    city = input ("Enter a city you would like to analyze: " ).lower()

    print('Now searching within ',city)
    print ('')
    while city not in city_names:
        city = input ('Could not find that city, please type the city name correctly: ').lower()



    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ('Enter a specific month you would like to analyze or type "All" to see all: ').lower()
    print ('Searching within the month ',month)
    print ('')
    while month not in month_names:
        month = input ('This month does not exist, please type in a valid month: ').lower()
        print ('Searching within the month ',month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ('Enter a specific day you would like to search for or type "All" to see all : ').lower()
    print ('here is a look at ',day)
    print ('')
    while day not in day_names:
        day = input ('A problem occured, please make sure your number corresponds with the correct day: ').lower()
        print ('here is a look at ',day)
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
    #get the city, month and day as variables to be analyzed

    df = pd.read_csv(CITY_DATA[city])
    #split up the date and time into individual variables so it can be analyzed
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august']
    #create a list and get a corresponding int based on the index. Add +1 because the index starts at 0
    if month != 'all':
        month = months.index(month) + 1
        # filter the data by the month to createthe new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        #create an index for the days of the week using integers to be filtered by
        df = df[df['day_of_week'] == day.title()]



    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

     # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    #use mode to find the most frequent month value
    pop_month = df['month'].mode()


    print ('The most popular month which is travelled is: ', pop_month)
    print (' ')

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #use mode to find the most frequent day of week value
    df['day'] = df['Start Time'].dt.day
    pop_day = df['day'].mode()



    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    #use mode to find the most frequent hour value
    pop_hour = df['hour'].mode()

    print ('The most popular hour which is travelled is: ', pop_hour)
    print (' ')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()
    print ('{}, is the most commonly used starting station for this specific search'.format(pop_start_station))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()
    print ('{}, is the most common end station for this specific search'.format(pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    popular_start=df['Start Station'].mode()[0]
    popular_end=df['End Station'].mode()[0]

    popular_trip=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most popular trip from start to end is \n{}".format(popular_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_time = df['Trip Duration'].sum()
    #convert the minutes into hours and round it to 2 decimal places
    tot_time = tot_time/60
    tot_time_round = round(tot_time,2)
    print('The total travel time is: {} hours'.format(tot_time_round))

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    avg_time = avg_time/60
    avg_time_round = round(avg_time,2)
    print ('The average travl time is: {} hours'.format(avg_time_round))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        #use the value_counts function for the dataframe to display the different types of users with their corresponding values
        user_type = df['User Type'].value_counts()
        print ('The total amount of each user type is: \n{}'.format(user_type))
        print('')

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        #use the value_counts function for the dataframe to display the different types of users with their corresponding values
        gender = df['Gender'].value_counts()
        print ('The genders of the passengers are as shown below: \n{}'.format(gender))
        print ('')

    # TO DO: Display earliest, most recent, and most common year of birth
        early_year = int (df['Birth Year'].min())
        print ('{} is the earliest year of birth in your search result'.format(early_year))
        latest_year = int(df['Birth Year'].max())
        print ('{} is the most recent year of birth in your search result'.format(latest_year))
        common_year = int(df['Birth Year'].mode())
        print ('{} is the most common year of birth in your search result'.format(common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def display_raw_data(df):
        i=0
        user_question=input('Would you like to see the raw data?\ntype yes or no: ').lower()
        while user_question in ['yes'] and i+5 < df.shape[0]:
            #get the 5 lines of data from the database and then add the new starting value to i+5 to get the next 5 lines in the loop
            print(df.iloc[i:i+5])
            i += 5
            user_question = input('Would you like to see more data? Please enter yes or no:').lower()




def main():
    start_program = input ('Would you like to start the program? type yes or no: ')
    #get the user to input a yes or no value to start the while loop which will display the statistics
    while start_program == 'yes':
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        q1 = input ("would you like to see more stats? type 'yes' or 'no' : ")
        if q1 == 'yes':
            print (station_stats(df))
        else:
            break
        q2 = input ("would you like to see more stats? type 'yes' or 'no' : ")
        if q2 == 'yes':
            print (trip_duration_stats(df))
        else:
            break
        q3 = input ("would you like to see more stats? type 'yes' or 'no' : ")
        if q3 == 'yes':
            print (user_stats(df))
        else:
            break

        display_raw_data (df)
        break







if __name__ == "__main__":
	main()
