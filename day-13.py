class Car:

	def __init__(self, x, y, direction, track):
		self.x = x
		self.y = y
		self.direction = direction
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

class StraightTrack(BaseTrack):

	def __init__(self, x, y, currentCar, direction, before, after):
		BaseTrack.__init__(self, x, y, currentCar)
		self.direction = direction
		self.before = before
		self.after = after

class CrossTrack(BaseTrack):

	def __init__(self, x, y, currentCar, left, right, top, bottom):
		BaseTrack.__init__(self, x, y, currentCar)
		self.left = left
		self.right = right
		self.top = top
		self.bottom = bottom

# sums = [[''] * 301 for i in range(301)]
field = []

with open('data-13.txt') as f:
	lines = f.read().splitlines()
	for _, line in enumerate(lines):
		vals = line.split(' ')