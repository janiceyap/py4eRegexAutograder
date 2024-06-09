import re

f = open("regex_sum_2032387.txt")
sum = 0
count = 0

for line in f:
    y = re.findall('([0-9]+)',line)
    
    if len(y) > 0:
        for item in y:
            count = count + 1
            sum = sum + int(item)

print(count,sum)