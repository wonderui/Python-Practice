import random

count = 0
end = 1000000

for i in range(end):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        count += 1

print(4*float(count)/float(end))

