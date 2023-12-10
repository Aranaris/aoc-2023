with open('../puzzle-inputs/day5input.txt','r') as file:
# with open('../test-inputs/day5testinput.txt','r') as file:
	segments = file.read().split('\n\n')
	seed_input = segments[0].split(' ')[1:]
	print('seeds: ', seed_input)
	locations = []
	maps = []
	for i in segments[1:]:
		next_map = []
		map = i.split('\n')
		for line in map[1:]:
			if line != '':
				numbers = line.split(' ')
				destination_start = numbers[0]
				source_start = numbers[1]
				range_length = numbers[2]
				next_map.append({
					'name': map[0],
					'destination_start': int(destination_start),
					'source_start': int(source_start),
					'range_len': int(range_length),
				}) 
		maps.append(next_map)
	
	min_location = 0
	no_seed = True
	while(no_seed):
		source = min_location
		for map in maps[::-1]:
			for line in map:
				if source >= line['destination_start'] and source < line['destination_start'] + line['range_len']:
					source = line['source_start'] + (source - line['destination_start'])
					break
		for i in range(0, len(seed_input), 2):
			if source >= int(seed_input[i]) and source < int(seed_input[i]) + int(seed_input[i+1]):
				no_seed = False
				print(min_location, source)
		min_location += 1
