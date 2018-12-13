def val(char):
	return ord(char) - ord('A') + 1 + 60

class Node:
	def __init__(self, name):
		self.name = name
		self.isVisited = False
		self.before = []
		self.after = []
		self.timeLeft = val(name)

nodes = []
workersNum = 5
workers = []*workersNum

with open('data-7.txt') as f:
	lines = f.read().splitlines()
	for _, line in enumerate(lines):
		vals = line.split(' ')
		valFrom = vals[1]
		valTo = vals[-3]
		# print(f'{valFrom} => {valTo}')
		nodeFrom = next((node for node in nodes if node.name == valFrom), False)
		if(not nodeFrom):
			nodeFrom = Node(valFrom)
			nodes.append(nodeFrom)
		nodeTo = next((node for node in nodes if node.name == valTo), False)
		if(not nodeTo):
			nodeTo = Node(valTo)
			nodes.append(nodeTo)
		nodeTo.before.append(nodeFrom)
		nodeFrom.after.append(nodeTo)

# print([f'{node.name} {node.timeLeft}' for node in nodes])
result = ''
totalTime = 0
nextNodes = [node for node in nodes if len(node.before) == 0]
nextNodes = sorted(nextNodes, key=lambda node: node.name)
workers = nextNodes[0:workersNum]
print([f'{node.name} {len(node.before)}' for node in workers])
while(len(nextNodes) > 0):
	totalTime += 1
	print(totalTime, end='')
	print(' ', end='')
	for i,work in enumerate(workers):
		work.timeLeft -= 1
		if(work.timeLeft == 0):
			result += work.name
			work.isVisited = True
			nextNodes.extend([node for node in work.after if not node in nextNodes])
			nextNodes = sorted(nextNodes, key=lambda node: node.name)
			nextNodes.remove(work)
		print(work.name, end='')
		print(' ', end='')
	print('')

	workers = [node for node in workers if not node.isVisited]

	if(len(workers) < workersNum):
		nodesToTake = [node for node in nextNodes if not node.isVisited and not node in workers and len([inner for inner in node.before if not inner.isVisited]) == 0]
		workers.extend(nodesToTake[0:(workersNum - len(workers))])

print(result)
print(totalTime)