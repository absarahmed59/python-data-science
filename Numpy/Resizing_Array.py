import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

#Numpy Array

height_arr = np.array(heights)

#Shape
print(f'Shape of Height Array is: {height_arr.shape}')

#Reshape
print(f'Reshaped Arrays is: {height_arr.reshape((5,9))}')
