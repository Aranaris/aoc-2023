from functools import reduce

with open('../puzzle-inputs/day9input.txt','r') as file:
# with open('../test-inputs/day9testinput.txt','r') as file:
	def get_last_value(input_array):
		not_zero = False
		next_array = []
		for i in range(len(input_array)-1):
			difference = int(input_array[i+1]) - int(input_array[i])
			next_array.append(difference)
			if difference != 0:
				not_zero = True
		if not_zero:
			return get_last_value(next_array) + int(input_array[-1])
		else:
			return int(input_array[-1])
	
	output = []

	for line in file:
			input = line.replace('\n','').split(' ')
			output.append(get_last_value(input))
	
	print(reduce(lambda a, b: a + b, output))
