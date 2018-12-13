def is_react(a,b):
	return a != b and a.upper() == b.upper()

def process_line(line, exclude_char):
	stack = []

	for _,ch in enumerate(line):
		if(ch.lower() == exclude_char):
			continue
		if(len(stack) == 0):
			stack.append(ch)
			continue
		top = stack.pop()
		if(is_react(top, ch)):
			continue
		stack.append(top)
		stack.append(ch)

	return stack

line = ''

with open('data-5.txt') as f:
	line = f.read()

abc = 'qazxswedcvfrtgbnhyujmkiolp'
min_len = len(line)
min_ch = ''

for _,ch in enumerate(abc):
	print(ch)
	result = process_line(line, ch)	
	if(len(result) < min_len):
		min_len = len(result)
		min_ch = ch

print(min_len)
print(min_ch)

