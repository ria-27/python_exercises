#2. Create two (3 * 3) matrices using NumPy and print it.
#Perform and print the results of the following linear algebra operations 
#a. Matrix addition 
#b. Matrix subtraction 
#c. Matrix multiplication (element-wise and dot product) 
#d. Transpose of a matrix 
#e. Determinant and inverse (if applicable) 

import numpy as np
A=np.random.randint(1,10,size=(3,3))
print(A)
B=np.random.randint(1,10,size=(3,3))
print(B)

print("Matrix addition:\n",np.add(A,B))

print("Matrix subtraction:\n",np.subtract(A,B))

print("Matrix multiplication(element-wise):\n",np.multiply(A,B))
print("Dot Product:\n",np.dot(A,B))

print("Transpose of A:\n",np.transpose(A))
print("Transpose of B:\n",np.transpose(B))

print("Determinant of A:\n",np.linalg.det(A))
print("Determinant of B:\n",np.linalg.det(B))
print("Inverse of A:\n",np.linalg.inv(A))
print("Inverse of B:\n",np.linalg.inv(B))
