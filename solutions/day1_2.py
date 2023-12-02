import os
import re

total = 0
array = []

spelledout = ['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('../puzzle-inputs/day1input.txt', 'r') as file:
	for line in file:
		firstdigit, lastdigit = '', ''
		for i in range(len(line)):
			if re.search("\d", line[i]):
				firstdigit = line[i]
				break
			else:
				for y in range(len(spelledout)):
					wordlength = len(spelledout[y])
					if i + wordlength <= len(line):
						if re.search(spelledout[y], line[i:i+wordlength]):
							firstdigit = str(y)
							break
				if len(firstdigit) > 0:
					break
		for j in range(1, len(line)+1):
			if re.search("\d", line[-j]):
				lastdigit = line[-j]
				break
			else:
				for y in range(len(spelledout)):
					wordlength = len(spelledout[y])
					if j + wordlength <= len(line):
						if re.search(spelledout[y], line[-(j+wordlength):-j]):
							lastdigit = str(y)
							break
				if len(lastdigit) > 0:
					break
		calibration = int(firstdigit+lastdigit)
		array.append(calibration)
		total = total + calibration

print(total, array)
				
