#Create a 1D array of numbers from 0 to 9.
#Create a 3x3 NumPy array of all True's.
#Extract all odd numbers from array.
#Replace all odd numbers in array with -1.
#Convert a 1D array to 2D array with 2 rows.

import numpy as np
a=np.arange(0,10)
print(a)

a=np.ones((3,3),dtype=bool)
print(a)

a=np.arange(1,10)
print(a)
odd=a[a%2!=0]
print("Odd numbers:\n",odd)

a[a%2!=0]=-1
print("Array with odd numbers replaced:\n",a)

a=np.arange(1,11)
print("1D array:\n",a)
a2=a.reshape(2,-1) #auto-gives proper amount of columns
print("2D array:\n",a2)

