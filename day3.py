import re

txt = open('day3-input.txt').read().split('\n')
sum = 0
for word in txt: 
    matches = re.findall(r"mul\(\d+,\d+\)", word)
    for expression in matches: 
        numbers = expression.replace("mul(", "").replace(",", " ").replace(")", "")
        number1 = int(re.search(r"\d+", numbers).group(0))
        number2 = int(re.search(r" \d+", numbers).group(0).strip())
        sum += (number1 * number2)

print(sum)

# Part 2

txt = open('day3-input.txt').read()
sum = 0
matches = re.findall(r"(mul\(\d+,\d+\)|don't\(\)|do\(\))", txt)
print(matches)
enabled = True
for expression in matches: 
    if expression == "don't()": 
        enabled = False
        continue 
    elif expression == "do()": 
        enabled = True 
        continue

    if enabled: 
        numbers = expression.replace("mul(", "").replace(",", " ").replace(")", "")
        number1 = int(re.search(r"\d+", numbers).group(0))
        number2 = int(re.search(r" \d+", numbers).group(0).strip())
        sum += (number1 * number2)

print(sum)