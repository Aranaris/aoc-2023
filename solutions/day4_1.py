with open('../puzzle-inputs/day4input.txt', 'r') as file:
# with open('../test-inputs/day4testinput.txt', 'r') as file:
	point_total = 0
	for line in file:
		sections = line.replace('\n', '').split(': ')[1].split(' | ')
		winning_nums = sections[0].split(' ')
		card_nums = sections[1].split(' ')

		match_count = 0
		for num in winning_nums:
			if num != '' and num in card_nums:
				match_count += 1
		if match_count > 0:
			point_total += 2 ** (match_count - 1)
	print(point_total)
