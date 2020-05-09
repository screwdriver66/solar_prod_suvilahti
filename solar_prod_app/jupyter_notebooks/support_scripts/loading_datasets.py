def load_df_with_datetime(filepath, datetime_col, delimiter=','):
    # loads a dataframe, converts datetime column into datetime in UTC and sets it as an index
    df = pd.read_csv(filepath, delimiter=delimiter)
    df[datetime_col] = pd.to_datetime(df[datetime_col], utc=True)
    df = df.set_index(pd.DatetimeIndex(df[datetime_col], dayfirst=True))
    df = df.drop(columns=datetime_col)
    return df

'''data analysis scripts'''
def analyse_na_value(df, var,target):

    df = df.copy()
    #creating a variable that indicates - 1 if the observation was missing or else - 0
    df[var] = np.where(df[var].isnull(),1,0)
    #comparing median power production in the observations where data is missing vs available
    df.groupby(var)[target].mean().plot.bar()
    plt.title(var)
    plt.show()

def analyse_discrete(df, var, target):
    df = df.copy()
    df.groupby(var)[target].mean().plot.bar()
    plt.title(var)
    plt.ylabel(str(target))
    plt.show()

def analyse_continuous(df, var):
    df = df.copy()
    df[var].hist(bins=30)
    plt.ylabel('Number of observations')
    plt.xlabel(var)
    plt.title(var)
    plt.show()

def analyse_transformed_continuous(df,var):
    df = df.copy()

    #log cannot take 0 or negative values, let's skip those for that matter
    if any(df[var]<0):
        pass
    else:
        df[var] = np.log(df[var])
        df[var].hist(bins=30)
        plt.ylabel('Number of observations')
        plt.xlabel(var)
        plt.title(var)
        plt.show()

import scipy.stats as stats
def diagnostic_plots(df, variable):

    # function to plot a histogram and a Q-Q plot
    # side by side, for a certain variable

    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    df[variable].hist(bins=30)

    plt.subplot(1, 2, 2)
    stats.probplot(df[variable], dist="norm", plot=plt)

    plt.show()
