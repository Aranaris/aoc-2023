with open('../puzzle-inputs/day2input.txt', 'r') as file:
	sum_id = 0
	for line in file:
		inputs = line.replace('\n', '').split(': ')
		game_id = inputs[0].replace('Game ', '')
		rounds = inputs[1].split('; ')
		max_red = 12
		max_green = 13
		max_blue = 14
		possible = True
		for round in rounds:
			cubes = round.split(', ')
			for cube_color in cubes:
				if ' green' in cube_color:
					green_cubes = int(cube_color.replace(' green',''))
					if green_cubes > max_green:
						possible = False
						break
				elif ' red' in cube_color:
					red_cubes = int(cube_color.replace(' red', ''))
					if red_cubes > max_red:
						possible = False
						break
				elif ' blue' in cube_color:
					blue_cubes = int(cube_color.replace(' blue', ''))
					if blue_cubes > max_blue:
						possible = False
						break
			if not possible:
				break
		if possible:
			sum_id += int(game_id)
	print(sum_id)
										
