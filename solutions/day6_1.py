from functools import reduce

# with open('../test-inputs/day6testinput.txt', 'r') as file:
with open('../puzzle-inputs/day6input.txt', 'r') as file:
	races = []
	for line in file:
		a = line.replace('\n', '').split(' ')[1:]
		inputs = []
		for char in a:
			if char:
				inputs.append(int(char))
		races.append(inputs)

	output = []
	for index in range(len(races[0])):
		winning_outcomes = 0
		time = races[0][index]
		distance = races[1][index]

		for t in range(time):
			speed = t
			time_remaining = time - speed
			distance_traveled = speed * time_remaining
			if (distance_traveled > distance):
				winning_outcomes += 1
		output.append(winning_outcomes)
	print(races)
	print(reduce(lambda a, b: a * b, output))
