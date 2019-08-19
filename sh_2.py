# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:21:03 2018

@author: spanier
"""
import itertools
from collections import deque
vowels = ['o','i','e','a','u']

def treatline(lineNr, line):
    if (list(filter(lambda x: x>='0' and x<='9', list(line))) !=[]):
        return -1
    L = line.split()
    D = dict(map(lambda x:(x, tuple([list(filter(lambda y: y in vowels, list(x)))\
                                     ,list(filter(lambda y: ord(y) in range(ord('b'),ord('m')+1) and y not in vowels, list(x)))\
                                     ,list(filter(lambda y: ord(y) in range(ord('n'),ord('z')+1) and y not in vowels, list(x)))\
                                     ])),L))
    return [lineNr,D]
   
def treatxtfile(flname):
	file = open(flname, 'r')
	content = file.read()
	file.close()
	L = content.split('\n')
	D = {}
	#in the question is written we can use loop for this program
	for i in range(len(L) - 1):
		Line = treatline(i,L[i])
		D[Line[0]] = Line[1]
	return D

def sikumofayim(D):
	L = dict(map(lambda x:(x,list(map(lambda y:D[x][y][0],D[x]))),D))
	L2 = dict(map(lambda x:(x,list(map(lambda y:D[x][y][1],D[x]))),D))
	L3 = dict(map(lambda x:(x,list(map(lambda y:D[x][y][2],D[x]))),D))
	D = dict(map(lambda x:(x,(list(itertools.chain.from_iterable(L[x]))\
                           ,list(itertools.chain.from_iterable(L2[x]))\
                           ,list(itertools.chain.from_iterable(L3[x])))),range(len(L))))
	return D
	
def main():	
	D = sikumofayim(treatxtfile('file.txt'))
	#max1 = (len(str(((max(D.values(), key=lambda x: x[0]))[0]))))
	#max2 = (len((max(D.values(), key=lambda x: x[1]))[1]))
	str0 = str(len(D)) + ' of Lines in text total'
	len0 = sum(list(map(lambda x:len(x[0]),D.values())))
	len1 = sum(list(map(lambda x:len(x[1]),D.values())))
	len2 = sum(list(map(lambda x:len(x[2]),D.values())))
	deque(map(lambda x:print(str(x),' '*(len(str0)-len(str(x))),D[x][0] , ' '*(30-len(str(D[x][0]))),D[x][1],' '*(30-len(str(D[x][1]))),D[x][2]),D))
	str1 = str(len0) +' of vowels total'
	str2 = str(len1) + ' of b-m consonants total'
	print(str0,str1,' '*(30-len(str1)), str2,' '*(30-len(str2) ) ,   len2 , 'of n-z consonants')
main()