import numpy as np

arr = np.array([1,2,3,4,5])
print("Original array  = ",arr)
print("Sum of array = ",np.sum(arr))
print("Sum of array = ",np.mean(arr))
print("Sum of array = ",np.min(arr))
print("Sum of array = ",np.max(arr))

# Reshape the array

reshaped_arr = arr.reshape(1,5)
print(reshaped_arr)
reshaped_arr = arr.reshape(5,1)
print(reshaped_arr)
