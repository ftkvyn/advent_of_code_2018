import math
import numpy

points = []

shift = 0

with open('data-6.txt') as f:
	lines = f.read().splitlines()
	for _, line in enumerate(lines):
		coords = line.split(',')
		x = int(coords[0]) + shift
		y = int(coords[1]) + shift
		points.append([x, y, 0, '???'])

points = sorted(points, key=lambda point: point[0])
points = sorted(points, key=lambda point: point[1])

x0 = points[0][0]
y0 = points[0][1]

max_x = max(points, key=lambda point: point[0])[0] + shift
max_y = max(points, key=lambda point: point[1])[1] + shift

# calculating angle cos for each point
for i,_ in enumerate(points):
	if( i == 0):
		continue

	x = points[i][0]
	y = points[i][1]
	dx = x - x0
	if(dx == 0):
		continue
	dy = y - y0
	hyp = math.sqrt(dx**2 + dy**2)
	points[i][2] = float(dx) / hyp

points[0][2] = 2
points[0][3] = 'out'
points = sorted(points, key=lambda point: -point[2])

stack = []

stack.append(points[0])
stack.append(points[1])

def is_right_turn(p_1, p_2, p_3):
	result = (p_2[0] - p_1[0])*(p_3[1] - p_1[1]) - (p_3[0] - p_1[0])*(p_2[1] - p_1[1])
	return result < 0

for i,point in enumerate(points):
	if(i < 2):
		continue
	if(point[3] == 'in'):
		continue
	point_3 = point
	left_found = False
	while not left_found:
		if(len(stack) < 2):
			left_found = True
			stack.append(point_3)
			continue

		point_2 = stack.pop()
		point_1 = stack.pop()

		if(is_right_turn(point_1, point_2, point_3)):
			point_2[3] = 'in'
			stack.append(point_1)
			continue
		else:
			left_found = True
			stack.append(point_1)
			stack.append(point_2)
			stack.append(point_3)

for i,_ in enumerate(stack):
	stack[i][3] = 'out'

points = list(map(lambda item: [item[0],item[1],item[3],0], points))

# field entry = [point_number, length_to_point]
field = numpy.zeros((max_x+1, max_y+1, 2))

stack = []
for i,item in enumerate(points):
	stack.append([item[0],item[1],item[2],i+1, 0])

print(stack)
in_added = True

def try_add_point(x, y, num, iteration):
	global max_x, max_y, field
	if(x < 0 or y < 0):
		return False
	if(x > max_x or y > max_y):
		return False
	if(field[x][y][0] == 0):
		field[x][y][0] = num
		field[x][y][1] = iteration
		return True	
	elif(field[x][y][1] == iteration and field[x][y][0] != num):
		field[x][y][0] = -1
	return False

iteration = 1

while in_added:
	in_added = False
	new_stack = []
	for i,item in enumerate(stack):
		x = item[0]
		y = item[1]
		if(try_add_point(x, y, item[3], iteration)):
			new_stack.append([x, y, item[2], item[3]])
			if(item[2] == 'in'):
				in_added = True
		if(try_add_point(x-1, y, item[3], iteration)):
			new_stack.append([x-1, y, item[2], item[3]])
			if(item[2] == 'in'):
				in_added = True
		if(try_add_point(x+1, y, item[3], iteration)):
			new_stack.append([x+1, y, item[2], item[3]])
			if(item[2] == 'in'):
				in_added = True
		if(try_add_point(x, y+1, item[3], iteration)):
			new_stack.append([x, y+1, item[2], item[3]])
			if(item[2] == 'in'):
				in_added = True
		if(try_add_point(x, y-1, item[3], iteration)):
			new_stack.append([x, y-1, item[2], item[3]])
			if(item[2] == 'in'):
				in_added = True
	stack = new_stack
	iteration = iteration + 1

for k,point in enumerate(points):
	if(point[2] != 'in'):
		print(f'{point[0]}, {point[1]}')

for x in range(max_x):
	for y in range(max_y):
		# if(field[x][y][0] == -1):
		# 	print('.', end='')
		# else:
		# 	print(int(field[x][y][0]), end='')
		num = int(field[x][y][0])
		if(num >= 0 ):
			point = points[num - 1]
			if(point[2] == 'in'):
				point[3] += 1
	# print('')

# zero borders
for x in range(max_x):
	num = int(field[x][0][0])
	points[num - 1][3] = 0
	num = int(field[x][max_y - 1][0])
	points[num - 1][3] = 0

for y in range(max_y):
	num = int(field[0][y][0])
	points[num - 1][3] = 0
	num = int(field[max_x - 1][y][0])
	points[num - 1][3] = 0

# print(points)
max_val = max(points, key=lambda point: point[3])
print(max_val)