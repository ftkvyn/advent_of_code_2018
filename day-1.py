values = []
results = {}
sum = 0

data_file = open('data-1.txt', 'r', encoding="utf8")
line = data_file.readline()
while line:
	num = int(line)
	sum += num
	values.append(num)
	line = data_file.readline()

print(sum)
data_file.close()

sum = 0
iterations = 0

while True:
	iterations += 1
	print(f'iterations: {iterations}')
	for i,num in enumerate(values):
		if(sum in results):
			print(sum)
			exit
		results[sum] = True
		sum += num