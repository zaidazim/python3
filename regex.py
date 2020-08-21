import re
fh = open("regexactual.txt")
sum = 0
for line in fh:
    numbers = re.findall('[0-9]+', line)
    if len(numbers) < 1:
        continue
    for str in numbers:
        intval = int(str)
        sum += intval
print(sum)
