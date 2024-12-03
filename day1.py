import re

left = []
right = []

txt = open('day1-input.txt').read().split('\n')

for line in txt:
  left_number = re.match(r"\d+", line).group(0)
  right_number = re.search(r"\d+$", line).group(0)
  left.append(int(left_number))
  right.append(int(right_number))

left.sort()
right.sort()

distance_sum = 0
for i in range(len(left)): 
  distance = abs(left[i] - right[i])
  distance_sum += distance

print(distance_sum)