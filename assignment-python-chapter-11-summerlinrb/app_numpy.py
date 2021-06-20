import numpy as np

# convert list to an numpy array

simple_list = [1, 2, 3]
array = np.array(simple_list)
print(array)
print(type(array))

# convert multidimensional list to numpy array
print("-----------Multi-dimensional array")
multidimensional_list = [
    [1, 2, 3],
    [4, 5, 6]
]
array = np.array(multidimensional_list)
print(array)
print(type(array))
print(f"Dimensions are {array.shape}")

# Initializing arrays with default values
# specify the dimensions and data type
print("-------Initializing arrays")
array = np.zeros((2, 4), dtype=int)
print(array)
array = np.ones((2, 4), dtype=int)
print(array)
array = np.full((2, 4), 99, dtype=int)
print(array)
# array of random numbers
# pylint may complain about the method np.random.random
# ignore pyltins complaint and run the code anyway
# search google for an explanation of the bug
# in pylint if interested

array = np.random.random((2, 4))
print(array)

# accessing elements in the array
print("-------Accessing elements in the array")
print(array[0, 0])
print(array[0, 1])
print(array[1, 0])
print(array[1, 1])

# loop through every element in the array
print("---------Loop through elements in the array")
for element in array:
    print(element)

print("---------Loop through individual items in the array")
for element in array:
    for item in element:
        print(item)

print("-" * 30)

# comparison operators
print(array > 0.2)

# filtering array values using comparison operators
print(array[array > 0.2])

# math operations on numpy
print(np.round(array))

print("-" * 30)

# how to perform math operations on an array, easily.

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])
print(first + second)
print(first - second)
print(first * second)
print(first + 100)

print("------ convert inches to cm")
dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
