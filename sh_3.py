def sortedzip(L):
	return list(zip(*list(map(lambda x:sorted(x),L))))
#print(sortedzip([[3,1,2],[5,6,4],['a','b','c']]))

def reversedZip(L):
	return list(zip(*list(map(lambda x:reversed(x),L))))
#print(reversedZip([[3,1,2],[5,6,4],['a','b','c']]))

def funczip(func,L):
	return func(L)
	
def unzippy(func,L):
	return reversed(list(zip(*L)))
	
def main():
	D = dict([(1,sortedzip),(2,reversedZip)])
	D2 = dict([(1,funczip),(2,unzippy)])
	lists = [[3,1,2],[5,6,4],['a','b','c']]#list(input().split())

	inp = 0
	while inp != -1:
		inp = int(input('enter 1 to zip 2 to unzip to finish -1>> '))
		inp2 = int(input('enter 1 to sort 2 to reverse>> '))
		lists = D2[inp](D[inp2],lists)
		print(lists)
main()