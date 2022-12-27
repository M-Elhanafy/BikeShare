import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply
        ...no month filter
        (str) day - name of the day of week to filter by, or "all" to apply
        ...no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    accepted_city_inputs = ["chicago", "new york city", "washington"]
    accepted_month_inputs = ['all','january', 'february', 'march', 'april', 
                             'may', 'june']
    accepted_day_of_week_inputs = ["all","monday","tuesday","wednesday",
                                   "thursday","friday","saturday","sunday"]
    # get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Enter name of city to analyze choose one of these 3 " +
                     "cities [chicago, new york city, washington]:\n").lower()
        if city in accepted_city_inputs:
            break
        else:
            print("!!!NOT A VALID INPUT!!!")


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter name of a month from january to june only these"+
                      " 6 months are valid input to filter data by "+
                      "or Enter all to apply to no month filter:\n").lower()
        if month in accepted_month_inputs:
            break
        else:
            print("!!!NOT A VALID INPUT!!!")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Enter day of week to filter data by or all to apply"+
                    " no day filter:\n").lower()
        if day in accepted_day_of_week_inputs:
            break
        else:
            print("!!!NOT A VALID INPUT!!!")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day
    ...if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
        ...to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
        ...to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #start_time is a valriable to calculate speed of this function 
    #acchived to get this statistics (efficiency)
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("The Most Common Month of Travel: {}".format(popular_month))
    
    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print("The Most Common day_of_week of "+
          "Travel: {}".format(popular_day_of_week))


    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['start_hour'].mode()[0]
    print("The Most Common start_hour of"+
          " Travel: {}".format(popular_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The Most Common Start Station" +
          " among all travels: " + popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The Most Common End Station" +
          " among all travels: " + popular_end_station)

    # display most frequent combination of start station and end station trip
    df['travel'] = "From: " + df['Start Station'] + " To: " + df['End Station']
    popular_travel = df['travel'].mode()[0]
    print("The Most Common Travel from start to end starion" +
          " among all travels: " + popular_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: " + str(total_travel_time / 60*60) + " Hour")

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average Travel Time: "
          + str(round(mean_travel_time / 60, 2)) + " Minute")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)

    # Display counts of gender
    if city != 'washington':
        gender_counts = df['Gender'].value_counts()
        print("\n" + str(gender_counts))
    # Display oldest, youngest, and most common year of birth
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        popular_birth_year = df['Birth Year'].mode()[0]
        print("\nOldest Birth Year: " + str(oldest))
        print("Youngest Birth Year: " + str(youngest))
        print("Most Common Year of Birth: " + str(popular_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_row_data(df):
    """
    Displays row data for the user to see 5 lines by 5 lines upone his request
    """
    num_of_rows = len(df.index)
    
    #looping over the hole data frame
    for i in range(0, num_of_rows, 5):
        
        #prompting the user if they want to see 5 lines of raw data
        valid_inputs = ['yes', 'no']
        while True:
            show_more = input("Do you want to see 5 lines of raw data?" +
                              " Enter yes or no. \n").lower()
            #Breaking from the while loop (from prompting for valid yes/no)
            if show_more in valid_inputs:
                break
            
        #Breaking from for loop (from displying more row inputs)
        if show_more == 'no':
            break
            
        #Display the first five rows of DataFrame
        print(df.head())
        
        #Make sure that interator value i will not result a sigmentation fault
        if num_of_rows - i < 5:
            print(df)
            print("End of Dataset")
            break
        else:
            #Droping five rows if the iterator i is not out of boundaries 
            df = df.drop([i, i+1, i+2, i+3, i+4], axis = 0)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
