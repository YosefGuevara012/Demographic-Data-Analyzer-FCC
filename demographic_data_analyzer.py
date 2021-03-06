import pandas as pd


def calculate_demographic_data(print_data=True):

    # Read data from file
    df = pd.read_csv('adult.data.csv')

    n = float(len(df))

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    # race_count = list(df["race"].unique())
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors = df[df["education"] == "Bachelors"]
    percentage_bachelors = percentage(bachelors,df)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # HE high education
    HE = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    LE = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education = percentage(HE,df)
    lower_education =  100 - higher_education

    # percentage with salary >50K

    HE_50K = HE[HE["salary"] == ">50K"]
    LE_50K = LE[LE["salary"] == ">50K"]

    higher_education_rich = percentage(HE_50K, HE)
    lower_education_rich = percentage(LE_50K, LE)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

    min_hours= df[df["hours-per-week"] == min_work_hours]

    min_hours_50K = df[(df["hours-per-week"] == min_work_hours)
                       & (df["salary"] == ">50K")]

    rich_percentage = percentage(min_hours_50K, min_hours)

    # What country has the highest percentage of people that earn >50K?

    earn_more_50K = df[df["salary"] == ">50K"]

    citizens_per_country = df.iloc[:,-2].value_counts().sort_index()
    
    count_earn_more_50K = earn_more_50K.iloc[:,-2].value_counts().sort_index()

    percentage_rich = count_earn_more_50K.div(citizens_per_country)


    highest_earning_country = percentage_rich.idxmax()

    highest_earning_country_percentage = round(percentage_rich.max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.

    india = earn_more_50K[earn_more_50K["native-country"] == "India"]

    top_IN_occupation = india.occupation.value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

def percentage(series_1, series_2):

    len_1 = float(len(series_1))
    len_2 = float(len(series_2))

    return round(len_1 / len_2 * 100, 1)