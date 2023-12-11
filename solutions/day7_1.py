with open('../puzzle-inputs/day7input.txt', 'r') as file:
# with open('../test-inputs/day7testinput.txt') as file:
	hands = []
	bids = []
	card_ranks = {
		'A': 14,
		'K': 13,
		'Q': 12,
		'J': 11,
		'T': 10,
		'9': 9,
		'8': 8,
		'7': 7,
		'6': 6,
		'5': 5,
		'4': 4,
		'3': 3,
		'2': 2,
	}
	hand_ranks = {
		'Five': 7,
		'Four': 6,
		'Full House': 5,
		'Three': 4,
		'Two Pair': 3,
		'One Pair': 2,
		'High Card': 1,
	}

	for line in file:
		hands.append(line.split(' ')[0])
		bids.append(int(line.replace('\n', '').split(' ')[1]))
	
	print(hands)

	data = []
	for i in range(len(hands)):
		hand = hands[i]
		bid = bids[i]
		hand_dict = {
			'hand':hand,
			'bid':bid,
			'type':'High Card',
			'cards': {},
		}

		for card in hand:
			if card not in hand_dict['cards']:
				hand_dict['cards'][card] = 1
			else:
				hand_dict['cards'][card] += 1
		max_count = max(hand_dict['cards'].values())
		if max_count == 5:
			hand_dict['type'] = 'Five'
		elif max_count == 4:
			hand_dict['type'] = 'Four'
		elif max_count == 3 and 2 in hand_dict['cards'].values():
			hand_dict['type'] = 'Full House'
		elif max_count == 3:
			hand_dict['type'] = 'Three'
		elif max_count == 2:
			pair_count = 0
			for value in hand_dict['cards'].values():
				if value == 2:
					pair_count += 1
			if pair_count == 2:
				hand_dict['type'] = 'Two Pair'
			else:
				hand_dict['type'] = 'One Pair'
		
		if not data:
			data.append(hand_dict)
		else:
			for index in range(len(data)):
				new_hand_score = hand_ranks[hand_dict['type']]
				compare_hand_score = hand_ranks[data[index]['type']] 
				if new_hand_score < compare_hand_score:
					data.insert(index, hand_dict)
					break
				elif new_hand_score == compare_hand_score:
					inserted = False
					for j in range(len(hand)):
						if card_ranks[hand[j]] < card_ranks[data[index]['hand'][j]]:
							data.insert(index, hand_dict)
							inserted = True
							break
						elif card_ranks[hand[j]] > card_ranks[data[index]['hand'][j]]:
							break
					if inserted:
						break
				if index == len(data) - 1:
					data.insert(index + 1, hand_dict)
					break
	
	total_winnings = 0
	for rank in range(len(data)):
		total_winnings += (rank + 1) * data[rank]['bid']

	print(total_winnings)
		
