stateStr = ''
stateBin = 0
count = 0
addedRight = 0
rules = []
rulesDict = [False]*32
steps = 50000000000
results = [0]*1000

def strToBin(str):
	num = 0
	for _,ch in enumerate(str):
		num = num * 2
		if(ch == '#'):
			num += 1
	return num

def printBin(num):
	str = bin(num)[2:]
	for i,ch in enumerate(str):
		if(ch == '1'):
			print('#', end='')
		else:
			print('.', end='')
	print('')
	
def calcTotal(val, added):
	lastNum = added + count - 1
	total = 0
	result = bin(val)[2:][::-1]
	for i,ch in enumerate(result):
		if(ch == '1'):
			total += lastNum
		lastNum -= 1
	return total

with open('data-12.txt') as f:
	lines = f.read().splitlines()
	stateStr = lines[0].split(' ')[2]
	count = len(stateStr)
	for _, line in enumerate(lines[2:]):
		ruleStr = line.split(' ')[0]
		ruleNum = strToBin(ruleStr)
		if(line[-1:] == '#'):
			rulesDict[ruleNum] = True
		else:
			rulesDict[ruleNum] = False

stateBin = strToBin(stateStr)
shift = 3

for i in range(steps):
	newState = 0
	addedRight += shift
	stateBin = stateBin << shift
	for pos in range(2, count + addedRight + shift):
		posMask = 1 << pos
		test = (stateBin >> (pos-2)) & 0b11111
		if(rulesDict[test]):
			newState += posMask
	while(newState & 0b1 == 0):
		newState = newState >> 1
		addedRight -= 1
	printBin(newState)
	if(i & 0b1111111111111 == 0):
		percent = '{0:.2f}'.format( i / steps * 100)
		print(f'Complete: {percent}%      ', end='\r', flush=True)
	if(stateBin == (newState << shift) ):
		erer = 100
	stateBin = newState
	results[i] = calcTotal(stateBin, addedRight)
# 4386
print()
print(addedRight)
lastNum = addedRight + count - 1
total = 0

result = bin(stateBin)[2:][::-1]
for i,ch in enumerate(result):
	if(ch == '1'):
		total += lastNum
	lastNum -= 1

print(total)