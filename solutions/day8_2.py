from functools import reduce

# with open('../test-inputs/day8testinput_part2.txt','r') as file:
with open('../puzzle-inputs/day8input.txt','r') as file:
	data = file.read().split('\n\n')
	steps = data[0]
	lines = data[1].split('\n')[:-1]
	nodes = []
	for line in lines:
		parsed = line.split(' = ')

		node = {
			'name': parsed[0],
			'L': parsed[1].split(', ')[0][1:4],
			'R': parsed[1].split(', ')[1][0:3]
		}
		nodes.append(node)

	def next_node(node_name, instruction):
		current_node = next(node for node in nodes if node['name'] == node_name)
		return current_node[instruction]
	
	
	# start = next(node for node in nodes if node['name'][2] == 'A')
	# new_node_name = start['name']
	
	starting_nodes = []

	for node in nodes:
		if node['name'][2] == 'A':
			starting_nodes.append(node['name'])
	
	# while not all_nodes_ended:
	# 	for step in steps:
	# 		for index in range(len(starting_nodes)):
	# 			starting_nodes[index] = next_node(starting_nodes[index], step)
	# 		total_steps += 1
	# 		check_z = False
	# 		for node_name in starting_nodes:
	# 			if node_name[2] != 'Z':
	# 				check_z = True
	# 				break
	# 		if not check_z:
	# 			all_nodes_ended = True
	# 			break

	min_steps = []
	for node in starting_nodes:
		total_steps = 0
		new_node_name = node
		while new_node_name[2] != 'Z':
			for step in steps:
				new_node_name = next_node(new_node_name, step)
				total_steps += 1
				if new_node_name[2] == 'Z':
					min_steps.append(total_steps)
					break
	
	def get_factors(number):	
			factor_array = []
			factor = 1
			x = number
			while factor <= x :
				factor += 1
				if x % factor == 0:
					factor_array.append(factor)
					x = x / factor
					factor -= 1
			return factor_array
	
	unique_factors = []
	for s in min_steps:
		factors = get_factors(s)
		for x in factors:
			if x not in unique_factors:
				unique_factors.append(x)
			# TODO add logic for handling multiple same factors

	print(steps)
	print(starting_nodes)
	print(min_steps)
	print(unique_factors)
	print(reduce(lambda a, b: a * b, unique_factors))
	
