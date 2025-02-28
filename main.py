import pandas as pd 
df = pd.read_csv('./data/GOOGL.csv')

######Pre-process######
def imported():
    print(df.head())

# check for null and duplicate rows
def null_dup_sum():
    missing=df.isnull().sum()
    print("missing values: ", missing)
    if (missing.sum()>0):
        print(df[df.isnull().any(axis=1)]) #if any value is null, print the entire column
    dup=df.duplicated().sum()
    print(dup)
    if (dup>0):
        print(df[df.duplicated()]) #if any value is null, print the entire column


null_dup_sum()

######End of Pre-process######


### Stock performance measure for RNN ##

"""
SMA, 
EMA, 
RSI, 
MACD



"""




