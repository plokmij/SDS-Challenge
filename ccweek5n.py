#python2
import re
import sys
regex = r"([' ']|['.']|[a-zA-Z])=[ ][0-9]*([ ]|[0-9]*|)*"
f = open(sys.argv[1])
fstr = f.read()

matches = re.finditer(regex, fstr)
letdic = {}

for thing in list(matches):
	plok = thing.group(0).split(' ')
	if plok[0] == '':
		for i in range(2,len(plok)):
			letdic[int(plok[i])] = ' ' 
	else:	
		for i in range(1,len(plok)):
			letdic[int(plok[i])] = plok[0][0]
letlist = []
for i in range(len(letdic)):
	letlist.append(letdic[i])

output = ''.join(letlist)
print output
