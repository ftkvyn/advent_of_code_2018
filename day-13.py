from termcolor import colored
import colorama
colorama.init()

class Car:

	def __init__(self, x, y, direction, track):
		self.x = x
		self.y = y
		self.direction = direction # up down left right
		self.currentTrack = track
		self.nextTurn = 'left'
	
	def getTurn(self):
		turn = self.nextTurn
		if turn == 'left':
			self.nextTurn = 'straight'
		elif turn == 'straight':
			self.nextTurn = 'right'
		else:
			self.nextTurn = 'left'
		return turn

class BaseTrack:

	def __init__(self, x, y, currentCar):
		self.x = x
		self.y = y
		self.currentCar = currentCar
		self.direction = '?'
		self.isCollision = False
		self.isVisited = False

class StraightTrack(BaseTrack):

	def __init__(self, x, y, currentCar, direction, before, after):
		BaseTrack.__init__(self, x, y, currentCar)
		self.direction = direction
		self.before = before
		self.after = after

class TurnTrack(BaseTrack):

	def __init__(self, x, y, currentCar, direction, horisontal, vertical):
		BaseTrack.__init__(self, x, y, currentCar)
		self.direction = direction
		self.horisontal = horisontal
		self.vertical = vertical

class CrossTrack(BaseTrack):

	def __init__(self, x, y, left, right, top, bottom):
		BaseTrack.__init__(self, x, y, 0)
		self.left = left
		self.right = right
		self.top = top
		self.bottom = bottom
		self.direction = '+'

field = []
cars = []
linesNum = 0
lineLen = 0

def printField():
	global field, lineLen, linesNum
	for ln in range(linesNum):
		for cn in range(lineLen):
			val = field[ln][cn]
			if isinstance(val, BaseTrack):
				if val.isCollision:
					print(colored('X', 'red'), end='', )
					continue
				if isinstance(val.currentCar, Car):
					char = '>'
					if val.currentCar.direction == 'up':
						char = '^'
					elif val.currentCar.direction == 'down':
						char = 'v'
					elif val.currentCar.direction == 'left':
						char = '<'
					print(colored(char, 'green'), end='', )
				else:
					char = val.direction
					if(val.isVisited):
						char = colored(char, 'yellow')
					print(char, end='')
			else:
				print(val, end='')
		print('')
	print('')


with open('data-13.txt') as f:
	lines = f.read().splitlines()
	linesNum = len(lines)
	lineLen = len(lines[0])
	field = [[''] * lineLen for i in range(linesNum)]
	for ln, line in enumerate(lines):
		for cn, char in enumerate(line):
			item = ' '
			car = 0
			if char == '-':
				item = StraightTrack(cn, ln, 0, '-', field[ln][cn-1], 0)
				if isinstance(field[ln][cn-1], StraightTrack):
					field[ln][cn-1].after = item
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item
				elif isinstance(field[ln][cn-1], TurnTrack):
					field[ln][cn-1].horisontal = item

			elif char == '|':
				item = StraightTrack(cn, ln, 0, '|', field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item
				elif isinstance(field[ln-1][cn], TurnTrack):
					field[ln-1][cn].vertical = item

			elif char == '>' or char == '<':
				item = StraightTrack(cn, ln, 0, '-', field[ln][cn-1], 0)
				if isinstance(field[ln][cn-1], StraightTrack):
					field[ln][cn-1].after = item
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item
				elif isinstance(field[ln][cn-1], TurnTrack):
					field[ln][cn-1].horisontal = item

				direction = 'right'
				if char == '<':
					direction = 'left'
				car = Car(cn, ln, direction, item)
				item.currentCar = car

			elif char == 'v' or char == '^':
				item = StraightTrack(cn, ln, 0, '|', field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item
				elif isinstance(field[ln-1][cn], TurnTrack):
					field[ln-1][cn].vertical = item

				direction = 'up'
				if char == 'v':
					direction = 'down'
				car = Car(cn, ln, direction, item)
				item.currentCar = car

			elif char == '/' or char == '\\':
				item = TurnTrack(cn, ln, 0, char, 0, 0)
				if isinstance(field[ln][cn-1], StraightTrack) and field[ln][cn-1].direction == '-':
					field[ln][cn-1].after = item
					item.horisontal = field[ln][cn-1]
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item
					item.horisontal = field[ln][cn-1]
				elif isinstance(field[ln][cn-1], TurnTrack):
					field[ln][cn-1].horisontal = item
					item.horisontal = field[ln][cn-1]

				if isinstance(field[ln-1][cn], StraightTrack) and field[ln-1][cn].direction == '|':
					field[ln-1][cn].after = item
					item.vertical = field[ln-1][cn]
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item
					item.vertical = field[ln-1][cn]
				elif isinstance(field[ln-1][cn], TurnTrack):
					field[ln-1][cn].vertical = item
					item.vertical = field[ln-1][cn]

			elif char == '+':
				item = CrossTrack(cn, ln, field[ln][cn-1], 0, field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item
				elif isinstance(field[ln-1][cn], TurnTrack):
					field[ln-1][cn].vertical = item

				if isinstance(field[ln][cn-1], StraightTrack):
					field[ln][cn-1].after = item
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item
				elif isinstance(field[ln][cn-1], TurnTrack):
					field[ln][cn-1].horisontal = item

			field[ln][cn] =  item
			if car != 0:
				cars.append(car)

# printField()

def makeMove():
	global field, cars, lineLen, linesNum
	cars = sorted(cars, key=lambda item: (item.y, item.x))
	xx = 10
	for _, car in enumerate(cars):
		cell = car.currentTrack
		nextCell = 0
		if isinstance(cell, StraightTrack):
			if car.direction == 'right' or car.direction == 'down':
				nextCell = cell.after
			else:
				nextCell = cell.before
		if isinstance(cell, TurnTrack):
			if cell.direction == '/':
				if car.direction == 'up':
					car.direction = 'right'
					nextCell = cell.horisontal
				elif car.direction == 'left':
					car.direction = 'down'
					nextCell = cell.vertical
				elif car.direction == 'down':
					car.direction = 'left'
					nextCell = cell.horisontal
				elif car.direction == 'right':
					car.direction = 'up'
					nextCell = cell.vertical
			elif cell.direction == '\\':
				if car.direction == 'up':
					car.direction = 'left'
					nextCell = cell.horisontal
				elif car.direction == 'left':
					car.direction = 'up'
					nextCell = cell.vertical
				elif car.direction == 'down':
					car.direction = 'right'
					nextCell = cell.horisontal
				elif car.direction =='right':
					car.direction = 'down'
					nextCell = cell.vertical
		elif isinstance(cell, CrossTrack):
			moveDir = car.getTurn()
			nextDir = ''
			if moveDir == 'straight':
				nextDir = car.direction
			elif moveDir == 'left':
				if car.direction == 'up':
					nextDir = 'left'
				elif car.direction == 'left':
					nextDir = 'down'
				if car.direction == 'down':
					nextDir = 'right'
				elif car.direction == 'right':
					nextDir = 'up'
			elif moveDir == 'right':
				if car.direction == 'up':
					nextDir = 'right'
				elif car.direction == 'left':
					nextDir = 'up'
				if car.direction == 'down':
					nextDir = 'left'
				elif car.direction == 'right':
					nextDir = 'down'
			car.direction = nextDir
			if car.direction == 'up':
				nextCell = cell.top
			elif car.direction == 'left':
				nextCell = cell.left
			if car.direction == 'down':
				nextCell = cell.bottom
			elif car.direction == 'right':
				nextCell = cell.right

		cell.currentCar = 0
		cell.isVisited = True
		car.currentTrack = nextCell
		car.x = nextCell.x
		car.y = nextCell.y
		if nextCell.currentCar != 0:
			nextCell.isCollision = True
			print(f'{nextCell.x},{nextCell.y}')
			print(f'{cell.x},{cell.y}')
			print(f'{car.x},{car.y}')
			return True
		nextCell.currentCar = car
	
	return False

moves = 0
isCollision = False
while not isCollision:
	isCollision = makeMove()	
	moves += 1
	if moves == 196:
		printField()
	# input("Next")

print(moves)
printField()