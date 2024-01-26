# CSV (Comma Separated Values)
# with open("weather_data.csv") as data:
#   weather = data.readlines()


# import csv
#
# with open("weather_data.csv") as data:
#   weather = csv.reader(data)
#   temperature = []
#   for row in weather:
#     if row[1] == "temp":
#       pass
#     else:
#       act_temp = int(row[1])
#       temperature.append(act_temp)
#
# print(temperature)

import pandas
import pyarrow

data = pandas.read_csv("weather_data.csv")
print(data)
temp_list = data["temp"].to_list()

add = 0
for num in temp_list:
  add += num

average = add / len(temp_list)
print(average)

# python have include a metod call sum
sum(temp_list)

# but pandas have a metod to calculate the average
print(data["temp"].mean())
print(data["temp"].max())

print(data.temp)
# Get data in row
print(data[data.temp == data.temp.max()])

# Convert the Monday's temperature to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
new_temp = ((monday.temp * 9) / 5) + 32
print(new_temp)

# Create a data frame from scratch
my_languages = {
  "languages": ['Ingles', 'Chino Mandarin', 'Aleman'],
  "pais_origen": ['Estados Unidos', 'China', 'Alemania']
}

data_language = pandas.DataFrame(my_languages)
print(data_language)
da

