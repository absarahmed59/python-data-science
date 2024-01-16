heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

#Height Stats
print(f'No of Heights are: {len(heights)}')
print(f'Sum of Heights are: {sum(heights)}')
print(f'Average Height is: {sum(heights)//len(heights)}')

#Counting Heights above 180

cnt = 0
for height in heights:
  if height > 188:
    cnt +=1

print(f'Total Heights above 180cm are: {cnt}')