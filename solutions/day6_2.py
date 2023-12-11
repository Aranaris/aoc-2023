# with open('../test-inputs/day6testinput.txt', 'r') as file:
with open('../puzzle-inputs/day6input.txt', 'r') as file:
	race = []
	for line in file:
		a = line.replace('\n', '').replace(' ','').split(':')[1:]
		race.append(int(a[0]))
	print(race)

	time = race[0]
	distance = race[1]
	winning_outcomes = 0

	for t in range(time):
		speed = t
		time_remaining = time - speed
		distance_traveled = speed * time_remaining
		if (distance_traveled > distance):
			winning_outcomes += 1
	print(winning_outcomes)
