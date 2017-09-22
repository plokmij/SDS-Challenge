import re
regex = r"([[:blank:]]|[a-zA-Z])=[ ][0-9]*([ ]|[0-9]*|)*"

test_str = (" = 7 18, .=, A=, B=, C=, D= 8, E=, F=, G=, H=, I=, J=, K=, L=, M=, N=, O=, P=, Q=, R=, S= 0 19, T=, U=, V=, W=, X=, Y=, Z=, a=, b=, c= 21, d= 3, e= 4 9 11 15 23, f=, g=, h=, i= 22, j=, k=, l= 12, m=, n= 5, o= 13 20, p= 14, q=, r= 16, s= 17, t= 1 6 24, u= 2, v= 10, w=, x=, y= 25, z=\n"
	"26\n")

matches = re.finditer(regex, test_str)
mydic = {}
max = 0
"""
#To find spaces
spaces = []

for i in range (3, len(test_str)):
	if test_str[i] == ",":
		break
	else:
		spaces.append(test_str[i])
for thing in spaces:
	print thing
	if thing.isdigit():
		mydic[int(thing)] = " "
"""

for thing in list(matches):
	plok = thing.group(0).split(' ')
	for i in range(1,len(plok)):
		mydic[int(plok[i])] = plok[0][0]

for i in range(len(mydic)):
	print mydic[i],
"""
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
"""