import numpy as np
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)

# 3rd value
print(heights_arr[2])

# updating value
heights_arr[2] = 160
print(heights_arr[2])

# slicing
heights_arr_slice = heights_arr[2:5]
print(heights_arr_slice)

# slicing from start
heights_arr_slice_start = heights_arr[:5]
print(heights_arr_slice_start)

# slicing from end
heights_arr_slice_end = heights_arr[-5:]
print(heights_arr_slice_end)
