# def process_str(str):
# 	has_two = False
# 	has_three = False
# 	for _,char in enumerate(str):
# 		num = str.count(char)
# 		if(num == 2 and not has_two):
# 			has_two = True
# 			print(f'{char}:{num}')
# 		if(num == 3 and not has_three):
# 			has_three = True
# 			# threes += 1
# 			print(f'{char}:{num}')
# 	return has_two, has_three

# twos = 0
# threes = 0

# data_file = open('data-2.txt', 'r', encoding="utf8")
# line = data_file.readline()
# while line:
# 	has_two, has_three = process_str(line)
# 	if(has_two):
# 		twos += 1
# 	if(has_three):
# 		threes += 1
# 	line = data_file.readline()

# print(f'{twos}*{threes}={twos * threes}')

with open('data-2.txt') as f:
	values = f.read().splitlines() 

for _,str1 in enumerate(values):
	for _,str2 in enumerate(values):
		diffs = 0
		diff_num = -1
		for i,_ in enumerate(str2):
			if(str1[i] != str2[i]):
				diffs += 1
				diff_num = i
		if(diffs == 1):
			print(str1)
			print(str2)
			print(f'{diff_num}:{str1[diff_num]},{str2[diff_num]}')
			print('-------------')