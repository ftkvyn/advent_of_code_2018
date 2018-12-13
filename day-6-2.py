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
		points.append([x, y])

max_x = max(points, key=lambda point: point[0])[0] + shift
max_y = max(points, key=lambda point: point[1])[1] + shift

def calc_distance(x,y,point):
	return abs(x - point[0]) + abs(y - point[1])

count = 0

for x in range(max_x):
	for y in range(max_y):
		total_dist = 0
		for _,point in enumerate(points):
			dist = calc_distance(x,y,point)
			total_dist += dist
		if (total_dist < 10000):
			count += 1

print(count)