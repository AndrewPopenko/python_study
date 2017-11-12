import random


numbers = []

numbers_size = random.randint(10, 20)

for _ in range(numbers_size):
    numbers.append(random.randint(10,20))

print("befor sorting: " + str(numbers))
numbers.sort()
print("after sorting: " + str(numbers))

half_size = len(numbers) // 2
median = None

if half_size % 2 == 1:
    median = numbers[half_size]
else:
    median = sum(numbers[half_size - 1:half_size + 1]) / 2

print("median is: " + str(median))

import statistics


median = statistics.median(numbers)

print(median)