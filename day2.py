txt = open("day2-input.txt").read().split("\n")

arrays = []
for line in txt: 
  temp = [int(item) for item in line.split(" ")]
  arrays.append(temp)

safe_reports = 0
for array in arrays: 
  # Monotonic strictly increasing stack
  increasing_stack = [array[0]] 

  # Monotonic strictly decreasing stack
  decreasing_stack = [array[0]]
  for i in range(len(array)): 
    # Add to strictly increasing stack
    if array[i] > increasing_stack[-1] and array[i] - increasing_stack[-1] <= 3: 
      increasing_stack.append(array[i])
    # Add to strictly decreasing stack
    if array[i] < decreasing_stack[-1] and abs(array[i] - decreasing_stack[-1]) <= 3: 
      decreasing_stack.append(array[i])
  
  if len(increasing_stack) == len(array) or len(decreasing_stack) == len(array): 
    safe_reports += 1

print(safe_reports)
    