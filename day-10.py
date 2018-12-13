import matplotlib.pyplot as plt

plt.ion()

pos = []
vel = []
pause = 0.01
len = 6

with open('data-10.txt') as f:
	lines = f.read().splitlines()
	for _, line in enumerate(lines):
		x = int(line[10:10+len])
		y = int(line[10+len+1:10+len+1+len+1])
		vx = int(line[-7:-5])
		vy = int(line[-3:-1])
		pos.append([x,y])
		vel.append([vx,vy])
		# print(f'{x};{y} => {vx};{vy}')
		plt.plot(x,y, 'bo')

plt.show()
plt.pause(pause)
plt.clf()

step = 1
time = 0
magnitude = 400
isBlue = False

while True:
	plt.clf()
	print(f'step {step}')
	step += 1
	time += magnitude
	if(step == 28):
		magnitude = 50
	if(step == 32):
		magnitude = 5
	if(step == 70):
		magnitude = 1
	if step == 144:
		magnitude = 1
	color = 'ro'
	if isBlue:
		color = 'bo'
	isBlue = not isBlue
	for i, _ in enumerate(pos):
		pos[i][0] += (vel[i][0] * magnitude)
		pos[i][1] += (vel[i][1] * magnitude)		
		plt.plot(pos[i][0],pos[i][1], color)
	plt.pause(pause)
	plt.show()