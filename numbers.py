# Write a python code block that inputs numbers into a list.
# Print largest, smallest,sum and average of the numbers.
# Count occurrences of a specific number in the list.
numbers=list(map(int,input("Enter numbers:").split()))
largest=max(numbers)
smallest=min(numbers)
total_sum=sum(numbers)
average=total_sum/len(numbers)
print("Numbers entered:", numbers)
print("Largest number:",largest)
print("Smallest number:",smallest)
print("Sum of numbers:",total_sum)
print("Average of numbers:",average)
search_num=int(input("Enter number to count its occurrences:"))
count=numbers.count(search_num)
print("The number",search_num,"occurs",count,"times in the list.")

