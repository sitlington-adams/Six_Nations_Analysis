# WHAT THIS DOES
# Loads in the libraries (pre-written bits of code) you'll need to do the analyis 
import pandas as pd
# Selects the spreadsheet you'd like to analyse
address = r"C:\Users\RMAda\PycharmProjects\SixNations Analysis\Scotland_Rugby_Data.csv"
Scotland = pd.read_csv(address)
# Let's you have a look at the first 25 lines of the spreadsheet
#print(Scotland.head(25))
#Let's you drop columns you don't need
Scotland_clean = Scotland.drop(["HTf", "HTa", "Unnamed: 7", "Unnamed: 11"], axis=1)
#print(Scotland_clean.head(5))
# Let's you change the column names and fill in the gaps
Scotland_clean_columns = ["Team", "Result", "For", "Against", "Diff", "Opposition", "Ground", "Date"]
print(Scotland_clean.head(5))
# calculates frequencies for columns containing letter/words 
Result = Scotland_clean.Result
print(Result.value_counts())
# calculates averages for columns containing numbers 
print(Scotland_clean.mean())
# Groups the spreadsheet (called a DataFrame) by its values in a particular column
Ground_groups = Scotland_clean.groupby(Scotland_clean["Ground"])
print(Ground_groups.mean())
# Groups the spreadsheet (called a DataFrame) by the result
Results = Scotland_clean.groupby(Scotland_clean["Result"])
print(Results.median())
# Saves a dataframe as a csv
Scotland_clean.to_csv(r"C:\Users\RMAda\PycharmProjects\SixNations Analysis\Scotland_Rugby_Data_Output.csv")