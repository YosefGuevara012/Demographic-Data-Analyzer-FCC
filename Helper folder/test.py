import pandas as pd
df = pd.read_csv('adult.csv')

def percentage(series_1, series_2):

    len_1 = float(len(series_1))
    len_2 = float(len(series_2))

    return round(len_1 / len_2 * 100, 1)


n = float(len(df))
HE = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
LE = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

higher_education = round(float(len(HE)) /n *100, 1) 
lower_education =  100 - higher_education


HE_50K = HE[HE["salary"] == ">50K"]
LE_50K = LE[LE["salary"] == ">50K"]

higher_education_rich = percentage(HE,df)
lower_education_rich = percentage(LE,df)


### min hours of work


min_work_hours = df["hours-per-week"].min()

num_min_workers = num_min_workers = df[(df["hours-per-week"] == min_work_hours)
                  & (df["salary"] == ">50K")]

rich_percentage = percentage(num_min_workers,df)


# What country has the highest percentage of people that earn >50K?

# highest_earning_country = df.groupby(['native-country']).nunique()

earn_more_50K = df[df["salary"] == ">50K"]

citizens_per_country = df.iloc[:,-2].value_counts().sort_index()

count_earn_more_50K = earn_more_50K.iloc[:,-2].value_counts().sort_index()

percentage_rich = count_earn_more_50K.div(citizens_per_country)

highest_earning_country = percentage_rich.idxmax()

# highest_earning_country = df.iloc[:,-2].value_counts()

highest_earning_country_percentage = round(count_earn_more_50K[0] / n * 100, 1)

# Identify the most popular occupation for those who earn >50K in India.

india = earn_more_50K[earn_more_50K["native-country"] == "India"]

top_IN_occupation = india.occupation.value_counts().idxmax()

print(highest_earning_country)
