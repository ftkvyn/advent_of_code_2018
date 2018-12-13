def parse_line(line):
	raw_vals = line.split(' ')
	id = raw_vals[0].replace('#','')
	start = raw_vals[2].replace(':','').split(',')
	start[0] = int(start[0])
	start[1] = int(start[1])
	dims = raw_vals[3].split('x')
	dims[0] = int(dims[0])
	dims[1] = int(dims[1])
	return id, start, dims

values = []

with open('data-3.txt') as f:
	lines = f.read().splitlines() 
	for _,line in enumerate(lines):
		values.append(parse_line(line))

count = 1000

total = [[0 for x in range(count)] for y in range(count)]
overlap = 0

for _,value in enumerate(values):
	for i in range(value[1][0], value[1][0] + value[2][0]):
		for j in range(value[1][1], value[1][1] + value[2][1]):
			if(total[i][j] == 0):
				total[i][j] = value[0]
			elif(total[i][j] != 'X'):
				overlap += 1
				total[i][j] = 'X'

for _,value in enumerate(values):
	has_overlaps = False
	for i in range(value[1][0], value[1][0] + value[2][0]):
		for j in range(value[1][1], value[1][1] + value[2][1]):
			if(total[i][j] == 'X'):
				has_overlaps = True
	if(not has_overlaps):
		print(value[0])