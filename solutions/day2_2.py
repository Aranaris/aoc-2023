with open('../puzzle-inputs/day2input.txt', 'r') as file:
	sum_power = 0
	for line in file:
		inputs = line.replace('\n', '').split(': ')
		game_id = inputs[0].replace('Game ', '')
		rounds = inputs[1].split('; ')
		max_red = 0
		max_green = 0
		max_blue = 0
		for round in rounds:
			cubes = round.split(', ')
			for cube_color in cubes:
				if ' green' in cube_color:
					green_cubes = int(cube_color.replace(' green',''))
					if green_cubes > max_green:
						max_green = green_cubes
				elif ' red' in cube_color:
					red_cubes = int(cube_color.replace(' red', ''))
					if red_cubes > max_red:
						max_red = red_cubes
				elif ' blue' in cube_color:
					blue_cubes = int(cube_color.replace(' blue', ''))
					if blue_cubes > max_blue:
						max_blue = blue_cubes
		sum_power += max_blue * max_red * max_green
	print(sum_power)
										
