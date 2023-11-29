import re

message = 'Tuesday: 22C, Wednesday: 21C, Thursday: 26C'
temperature = re.findall('\\d{2}',message)
print(temperature)

sum = 0
for t in temperature:
    sum += int(t)

av = sum / len(temperature)

print(av)