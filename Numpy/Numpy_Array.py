import numpy as np

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

heights_arr = np.array(heights)

#Height Stats
print(f'No of Heights are: {len(heights_arr)}')
print(f'Sum of Heights are: {sum(heights_arr)}')
print(f'Average Height is: {sum(heights_arr)//len(heights_arr)}')

#Counting Heights above 180

#Python List
'''
cnt = 0
for height in heights:
  if height > 188:
    cnt +=1
'''

#Numpy Array

print(f'Total Heights above 180cm are: {(heights_arr>180).sum()}')

