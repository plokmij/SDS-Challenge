import re
import sys
regex = r"([' ']|[a-zA-Z])=[ ][0-9]*([ ]|[0-9]*|)*"
f = open(sys.argv[1])
test_str = f.read()

matches = re.finditer(regex, test_str)
mydic = {}

for thing in list(matches):
	plok = thing.group(0).split(' ')
	if plok[0] == '':
		for i in range(2,len(plok)):
			mydic[int(plok[i])] = plok[0]
	else:	
		for i in range(1,len(plok)):
			mydic[int(plok[i])] = plok[0][0]

for i in range(len(mydic)):
	print mydic[i],
