# with open('../test-inputs/day8testinput_part1.txt','r') as file:
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
	
	total_steps = 0
	start = next(node for node in nodes if node['name'] == 'AAA')
	new_node_name = start['name']

	while new_node_name != 'ZZZ':
		for step in steps:
			new_node_name = next_node(new_node_name, step)
			total_steps += 1
			if new_node_name == 'ZZZ':
				break
	print(steps)
	print(nodes)
	print(total_steps)
