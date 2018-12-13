class Node:
	def __init__(self, prev, next, val):
		self.prev = prev
		self.next = next		
		self.val = val

playersNum = 403
maxVal = 7192000

currentPos = 1
zeroVal = Node(0, 0, 0)
firstVal = Node(zeroVal, zeroVal, 1)
zeroVal.next = firstVal
zeroVal.prev = firstVal
currentVal = firstVal
move = 1
currentPlayer = 0
players = [0] * playersNum
circle = [0]

while move <= maxVal:
	move += 1
	if (move) % 23 != 0:
		putAfter = currentVal.next
		newNode = Node(putAfter, putAfter.next, move)
		putAfter.next.prev = newNode
		putAfter.next = newNode
		currentVal = newNode
	else:
		for i in range(7):
			currentVal = currentVal.prev
		players[currentPlayer] += currentVal.val + move
		currentVal = currentVal.next
		currentVal.prev = currentVal.prev.prev
		currentVal.prev.next = currentVal	
	if move % 10000 == 0:
		percent = '{0:.2f}'.format(move / maxVal * 100)
		print(f'Complete: {percent}%        ', end='\r', flush=True)

	# print(f'{currentPlayer + 1} => [', end='')
	# printVal = zeroVal
	# while True:
	# 	print(f'{printVal.val} ', end='')
	# 	printVal = printVal.next
	# 	if(printVal == zeroVal):
	# 		break
	# print(']')
	
	currentPlayer = ( currentPlayer + 1 ) % playersNum	
	
print('')
print(max(players))