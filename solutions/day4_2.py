# card = {
# 	'id': id,
# 	'match_count': match_count,
# 	'next_cards': [],
# }

def parse_cards(file):
	cards = []
	for line in file:
		sections = line.replace('\n', '').split(': ')
		card_id = sections[0].replace('Card ','')
		numbers = sections[1].split(' | ')
		winning_nums = numbers[0].split(' ')
		card_nums = numbers[1].split(' ')
		match_count = 0
		for num in winning_nums:
			if num != '' and num in card_nums:
				match_count += 1
		cards.append({
			'id': int(card_id),
			'match_count': match_count
		})
	return cards


with open('../puzzle-inputs/day4input.txt', 'r') as file:
# with open('../test-inputs/day4testinput.txt', 'r') as file:
	card_total = 0
	cards = parse_cards(file)

	def get_total_cards(card):
		total_cards = 1
		if card['match_count'] == 0:
			return total_cards
		else:
			for i in range(1, card['match_count'] + 1):
				new_card = next(j for j in cards if j['id'] == card['id'] + i)
				total_cards += get_total_cards(new_card)
			return total_cards
		
	for card in cards:
		card_total += get_total_cards(card)
		print(card, card_total)

