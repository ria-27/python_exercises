# . Create a data frame with details of 10 students and columns as Roll Number, Name, Gender, Marks1, Marks2, Marks3. 
#a. Create a new column with total marks 
#b. Find the lowest marks in Marks1 
#c. Find the Highest marks in Marks2 
#d. Find the average marks in Marks3 
#e. Find student name with highest average 
#f. Find how many students failed in Marks2 (<40) 

import pandas as pd
data = {
    "Roll Number": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["Asha","Ravi","Meera","Kiran","Sita","Arjun","Lata","Vikram","Nina","Raj"],
    "Gender": ["F","M","F","M","F","M","F","M","F","M"],
    "Marks1": [55, 72, 38, 90, 67, 45, 88, 76, 59, 81],
    "Marks2": [60, 35, 78, 92, 40, 25, 85, 66, 55, 89],
    "Marks3": [70, 80, 65, 88, 55, 60, 95, 72, 68, 77]
}
df = pd.DataFrame(data)
print("Student Dataframe:\n",df)
df["Total"] = df["Marks1"] + df["Marks2"] + df["Marks3"]

lowest_marks1 = df["Marks1"].min()
print("Lowest Marks in Marks1:", lowest_marks1)

highest_marks2 = df["Marks2"].max()
print("Highest Marks in Marks2:", highest_marks2)

average_marks3 = df["Marks3"].mean()
print("Average Marks in Marks3:", average_marks3)

df["Average"] = df[["Marks1","Marks2","Marks3"]].mean(axis=1)
top_student = df.loc[df["Average"].idxmax(), "Name"]
print("Student with highest average:", top_student)

failed_count = (df["Marks2"] < 40).sum()
print("Number of students failed in Marks2:", failed_count)

