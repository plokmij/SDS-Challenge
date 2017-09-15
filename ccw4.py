x = int( raw_input('Number : ') )
k = int( raw_input('Number of digits to multiply :') )

def product(list):
	prod = 1
	for thing in list:
		prod = prod * thing
	return prod

list = []
max = 0
while( x!=0 ):
	list.append(int(x%10))
	x = x/10

for i in range(len(list)-k+1):
	new = product(list[i:i+k])
	if new > max:
		max = new


print('Largest product '+str(max))
