import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
color = data["Primary Fur Color"].value_counts()

colors = pandas.DataFrame(color)
colors.to_csv("squirrel_colors.csv")
