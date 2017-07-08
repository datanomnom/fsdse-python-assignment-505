import pandas as pd

def load_data():

    df = pd.read_csv("files/olympics.csv", skiprows= 1)
    df.rename(columns={'01 !': 'Gold', '02 !': 'Silver', '03 !': 'Bronze'}, inplace=True)
    country_names = [x.split('\xc2\xa0(')[0] for x in df['Unnamed: 0']]   #iloc[:,0]]
    df.set_index(pd.Series(country_names), inplace=True)
    df.rename(columns={"Unnamed: 0" : "Country"},inplace = True)
    df.iloc[:,0] = country_names
    df.drop(['Totals'],axis=0, inplace= True)

    return df

load_data()

def first_country(df):

    return df.iloc[0,:]


def gold_medal(df):

    return df['Gold'].argmax()     # return df.iloc[:,12].idxmax()


def biggest_difference_in_gold_medal(df):

    df1 = df[['Gold','01 !.1']]
    df1['Difference'] = df1['Gold'] - df1['01 !.1']    # df1.iloc[:,1] - df1.iloc[:,2]
    return df1['Difference'].argmax()                  # return df1['Difference'].idxmax()


def get_points(df):

    df['Points'] = 3*df.iloc[:,12]+2*df.iloc[:,13]+df.iloc[:,14]

    return df.loc[:,'Points']

# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
