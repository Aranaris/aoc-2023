import os
import re

total = 0
array = []

with open('../puzzle-inputs/day1input.txt', 'r') as file:
	for line in file:
		firstdigit, lastdigit = '', ''
		for i in range(len(line)):
			if re.search("\d", line[i]):
				firstdigit = line[i]
				break
		for j in range(1, len(line)+1):
			if re.search("\d", line[-j]):
				lastdigit = line[-j]
				break
		calibration = int(firstdigit+lastdigit)
		array.append(calibration)
		total = total + calibration

print(total, array)
				
