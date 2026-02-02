#1. Generate a 3x4 NumPy array with random integers between 1 and 50.   
#a. Calculate and print the Mean, Median, and Standard Deviation of the array 
#b. Print the Sum of all elements and the sum of each row. 
#c. Reshape the 3x4 array into a 2x6 array and print it. 
import numpy as np
a=np.random.randint(1,51,size=(3,4))
print(a)

print('Mean=',np.mean(a))
print('Median=',np.median(a))
print('Standard Deviation=',np.std(a))

print('Sum=',a.sum())
print('Sum of Rows=',a.sum(axis=0))

a=a.reshape(2,6)
print(a)
