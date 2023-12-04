# schematic = {
# 	numbers: {
# 		123: [(start_row, start_column), (end_row, end_column)]
# 	},
# 	symbols: [(row, column)]
# }

def get_adjacent_loc(row, start_col, end_col):
	locations = []
	locations.append((row, start_col - 1))
	locations.append((row, end_col + 1))
	for col in range(start_col - 1, end_col + 2):
		locations.append((row - 1, col))
		locations.append((row + 1, col))
	return locations

digits = ['0','1','2','3','4','5','6','7','8','9']

with open('../puzzle-inputs/day3input.txt','r') as file:
# with open('../test-inputs/day3testinput.txt','r') as file:
	row = 0
	schematic_nums = []
	gear_symbols = []
	for line in file:
		line = line.replace('\n','')
		num_string = ''
		current_column = 0
		for char in line:
			if char in digits:
				if num_string == '':
					num_start_column = current_column
					num_string = char
				else:
					num_string += char
				if current_column == len(line) - 1:
					num_end_column = current_column - 1
					adjacent = get_adjacent_loc(row, num_start_column, num_end_column)
					schematic_nums.append({
						'value': int(num_string),
						'adjacents': adjacent,
					})
			elif num_string != '':
				num_end_column = current_column - 1
				adjacent = get_adjacent_loc(row, num_start_column, num_end_column)
				schematic_nums.append({
					'value': int(num_string),
					'adjacents': adjacent,
				})
				num_string = ''
			if char == '*':
				gear_symbols.append((row, current_column))
			current_column += 1
		row += 1
	sum_gear_ratio = 0
	gears = []
	for gear in gear_symbols:
		part_count = 0
		gear_ratio = 1
		for part in schematic_nums:
			for loc in part['adjacents']:
				if gear == loc:
					part_count += 1
					gear_ratio *= part['value']
					break
		if part_count == 2:
			sum_gear_ratio += gear_ratio
			gears.append(gear)
	print(sum_gear_ratio)
	print(gears)
		
			
