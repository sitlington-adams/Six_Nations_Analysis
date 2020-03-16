import pandas
address = r"\Users\RMAda\PycharmProjects\SixNations Analysis\Week_1_France\Starter_Materials\France_Rugby_Data.csv" #remember the r in the address
France = pandas.read_csv(address)
France_clean = France.drop(["HTf", "HTa", "Unnamed: 7", "Unnamed: 11"], axis=1)
France_clean.columns = ["Team", "Result", "For", "Against", "Diff", "Opposition", "Ground", "Match Date"]
France_clean.to_csv(r"\Users\RMAda\PycharmProjects\SixNations Analysis\Week_1_France\Starter_Materials\France_Rugby_Data_Output2.csv")
print(France_clean)

