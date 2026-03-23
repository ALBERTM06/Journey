import numpy as np
from numpy.random import randint, rand, randn
#Create an array of 10 zeros
# array = np.zeros(10)
# print(array)

#Create an array of 10 zeros
# array = np.ones(10)
# print(array)

# Create an array of 10 fives
# array = 5*(np.ones(10))
# print(array)

#Create an array of the integers from 10 to 50
# array = np.arange(10,51)
# print(array)

#Create an array of all the even integers from 10 to 50
# array = np.arange(10,51,2)
# print(array)

#Create a 3x3 matrix with values ranging from 0 to 8
# array = randint(0,8,9).reshape(3,3)
# print(array)

#Create a 3x3 identity matrix
# array = np.eye(3)
# print(array)

#Use NumPy to generate a random number between 0 and 1
# array = rand(2)
# print(array)

#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
# array = randn(5,5)
# print(array)

#Create a matrix with elements from 0.01-1
# array = np.linspace(0.01,1.,100).reshape(10,10)
# print(array)

#Create an array of 20 linearly spaced points between 0 and 1:
# array = np.linspace(0.,1.,20)
# print(array)

mat = np.arange(1,26).reshape(5,5)
# arr = np.array([mat[0,1],mat[1,1],mat[2,1]])
# print(arr)
# arr = np.array(mat[:3,1])
# print(arr)

#Get the sum of all the values in mat
#print(mat.sum())

#Get the standard deviation of the values in mat
# print(mat.std())

#Get the sum of all the columns in mat
# print(mat.sum(axis=0))