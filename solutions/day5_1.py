with open('../puzzle-inputs/day5input.txt','r') as file:
# with open('../test-inputs/day5testinput.txt','r') as file:
	segments = file.read().split('\n\n')
	seeds = segments[0].split(' ')[1:]
	locations = []
	print('seeds: ', seeds)
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
	for seed in seeds:
		loc = int(seed)
		for map in maps:
			for line in map:
				if loc >= line['source_start'] and loc < line['source_start'] + line['range_len']:
					loc = line['destination_start'] + (loc - line['source_start'])
					break
		locations.append(loc)
	print(min(locations))
	
