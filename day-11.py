grid = [[0] * 300 for i in range(300)]
sums = [[0] * 301 for i in range(301)]
gridId = 8561

def getVal(_x,_y,_id):
	rId = _x + 10
	val = rId * _y + _id
	val = val * rId
	hundr = (val // 100) % 10
	val = hundr - 5
	return val

for x in range(300):
	for y in range(300):
		val = getVal(x+1,y+1,gridId)
		grid[x][y] = val

maxTotal = -1
maxX = -1
maxY = -1
maxS = -1

def calcTotal(x,y,s):
	global grid
	global sums
	sums[x][y] = sums[x][y+1] + sums[x+1][y] - sums[x+1][y+1] + grid[x][y]	
	total = sums[x][y] - sums[x+s][y] - sums[x][y+s] + sums[x+s][y+s]
	
	return total


for x in range(299, -1, -1):
	for y in range(299, -1, -1):
		for s in range(min([300-x, 300-y]), 0, -1):
			total = calcTotal(x,y,s)
			if total > maxTotal:
				maxTotal = total
				maxX = x
				maxY = y
				maxS = s
	percent = '{0:.2f}'.format( (300-x) / 300 * 100)
	print(f'Complete: {percent}%      ', end='\r', flush=True)

print('\n')

print(maxTotal)
print(maxX+1)
print(maxY+1)
print(maxS)
print(f'{maxX+1},{maxY+1},{maxS}')