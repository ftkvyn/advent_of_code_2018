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

class StraightTrack(BaseTrack):

	def __init__(self, x, y, currentCar, direction, before, after):
		BaseTrack.__init__(self, x, y, currentCar)
		self.direction = direction
		self.before = before
		self.after = after

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
					print(val.direction, end='')
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

			if char == '|':
				item = StraightTrack(cn, ln, 0, '|', field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item

			if char == '>' or char == '<':
				item = StraightTrack(cn, ln, 0, '-', field[ln][cn-1], 0)
				if isinstance(field[ln][cn-1], StraightTrack):
					field[ln][cn-1].after = item
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item

				direction = 'right'
				if char == '<':
					direction = 'left'
				car = Car(cn, ln, direction, item)
				item.currentCar = car

			if char == 'v' or char == '^':
				item = StraightTrack(cn, ln, 0, '|', field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item

				direction = 'up'
				if char == 'v':
					direction = 'down'
				car = Car(cn, ln, direction, item)
				item.currentCar = car

			if char == '/':
				item = StraightTrack(cn, ln, 0, '/', 0, 0)

			if char == '\\':
				item = StraightTrack(cn, ln, 0, '\\', 0, 0)

			if char == '+':
				item = CrossTrack(cn, ln, field[ln][cn-1], 0, field[ln-1][cn], 0)
				if isinstance(field[ln-1][cn], StraightTrack):
					field[ln-1][cn].after = item
				elif isinstance(field[ln-1][cn], CrossTrack):
					field[ln-1][cn].bottom = item

				if isinstance(field[ln][cn-1], StraightTrack):
					field[ln][cn-1].after = item
				elif isinstance(field[ln][cn-1], CrossTrack):
					field[ln][cn-1].right = item

			field[ln][cn] =  item
			if car != 0:
				cars.append(car)


printField()