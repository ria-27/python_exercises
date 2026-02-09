#1.Create a Series from a list of integers representing daily temperatures (in Celsius) over a week. Assign index labels as day of the week. 
#a. Find and print the average (mean) temperature for the week. 
#b. Identify and print the maximum and minimum temperatures and their respective days. 
#c. Display the temperatures greater than a specific value. 
#d. Convert all temperatures to Fahrenheit. 
#e. Print the days had temperatures above the average. 
import pandas as pd
temps = [25, 28, 30, 27, 26, 29, 31]  
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

temp_series = pd.Series(temps, index=days, name="Temperature")
print("Temperature Series:\n", temp_series, "\n")

avg_temp = temp_series.mean()
print("Average temperature for the week:", avg_temp)

max_temp = temp_series.max()
min_temp = temp_series.min()
max_day= temp_series.idxmax()
min_day = temp_series.idxmin()
print("Maximum temperature:", max_temp, "on", max_day)
print("Minimum temperature:", min_temp, "on", min_day)

sv=30
greater=temp_series[temp_series > 30]
print("\nTemperatures greater than",sv,":\n",greater) 

fahrenheit = (temp_series * 9/5) + 32
print("\nTemperatures in Fahrenheit:\n", fahrenheit)

above_avg_days = temp_series[temp_series > avg_temp]
print("\nDays with temperatures above average:\n", above_avg_days)
