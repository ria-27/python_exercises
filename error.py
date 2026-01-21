# write a python code block to create a tuple with five elements.
# Try to change one of the elements and handle the error that occurs.
# Print a message that explains why the error occurred.
t={10,20,30,40,50}
print(t)
try:
    t[2]=55
except TypeError as e:
    print("error occurred",e)
    print("Explanation: Tuples in python are immutable, meaning their elements cannot be changed once created.")
