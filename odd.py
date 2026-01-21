# Create a python function that creates a sequence between 1 and 100 and prints all the odd numbers.
# Compute and display the sum of all even numbers.
def sequence():
    even_sum=0
    print("All the odd numbers:")
    for i in range(1,101):
        if i % 2 == 0:
            even_sum += i
        else:
            print(i)
    print("Sum of even numbers between 1 and 100:", even_sum)
sequence()
