lines = []

with open('data-4.txt') as f:
	lines = f.read().splitlines()
	lines.sort()

values = []
guards = {}
current_guard = -1
current_sleep_start = -1

max_guard = -1
max_min_num = -1
max_mins = -1

for i,line in enumerate(lines):
	date = line[1:17]
	# hour = date[-5:-3]
	# if(hour == '23'):
	# 	line = lines[i+1][0:12] + '00:00' + lines[i][17:]
	# 	date_new = line[1:17]
	# 	lines[i] = line

	# date = line[1:17]
	minute = int(date[-2:])
	value = line[19:]

	if(value[0:5] == 'Guard'):
		current_guard = int(value.split(' ')[1][1:])
		if(not current_guard in guards):
			guards[current_guard] = [0]*60
	elif(value == 'falls asleep'):
		current_sleep_start = minute
	elif(value == 'wakes up'):
		for i in range(current_sleep_start,minute):
			guards[current_guard][i] += 1
			if(guards[current_guard][i] > max_mins):
				max_guard = current_guard
				max_min_num = i
				max_mins = guards[current_guard][i]

print(max_guard)
print(guards[max_guard])
print(max_min_num)
print(max_guard * max_min_num)

# max_guard = max(guards.keys(), key=(lambda key: sum(guards[key])))
# print(max_guard)
# print(guards[max_guard])
# max_min_num = max(range(0,60), key=(lambda key: guards[max_guard][key]))
# print(max_min_num)
# print(max_guard * max_min_num)