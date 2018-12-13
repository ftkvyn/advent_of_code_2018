nums = []
total = 0

def processPosition(pos):
	global nums, total
	childLeft = nums[pos]
	childTotal = childLeft
	children = []
	value = 0
	metaLen = nums[pos + 1]
	pos = pos + 2
	while childLeft > 0:
		pos, childValue = processPosition(pos)
		childLeft = childLeft - 1
		children.append(childValue)
	for i in range(metaLen):
		if childTotal == 0:
			value += nums[pos + i]
		else:
			num = nums[pos + i] - 1
			if num < len(children):
				value += children[num]
	pos = pos + metaLen
	return pos, value

with open('data-8.txt') as f:
	lines = f.read().split(' ')
	for _, line in enumerate(lines):
		nums.append(int(line))

_,value = processPosition(0)
print(value)