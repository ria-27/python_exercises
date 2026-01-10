# Program to classify age of user.
print("What is your age?")
age = int(input())
if age <= 1:
    print("Infant")
elif age < 18:
    print("Child")
elif age < 40:
    print("Young Adult")
elif age < 65:
    print("Adult")
else:
    print("Senior Citizen")

