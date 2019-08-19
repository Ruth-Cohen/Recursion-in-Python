# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 12:59:25 2018

@author: Schlossberg
"""
import Targil4input
from functools import reduce

def average1(lst):
    return reduce(lambda x, y:x + y, lst) / len(lst)

def deviation(lst):
    return pow((1/len(lst))*(reduce(lambda x,y:x+y,list(map(lambda i:pow(lst[i]-average1(lst), 2),range(len(lst)))))),0.5)

def myStudentList(list1,list2):
    if list1 == []:
        L = list(map(lambda x:x[1],list2))
        return [average1(L),deviation(L)]
    res = list(map(lambda x:x[0],filter(lambda x:x[2] ==list1[0][1], list2)))
    resTemp = list(map(lambda x:x[1],filter(lambda x:x[2] ==list1[0][1], list2)))
    res2 = []
    if res != []:
        res2= [average1(resTemp),deviation(resTemp)]
    return [[list1[0][0] , [res,res2]]] + myStudentList(list1[1:],list2)


def myStudDict(Lst):
    return dict(map(lambda x:(x[0],tuple(x[1])),filter(lambda x:isinstance(x,list) and isinstance(x[0],str), Lst)))
 

def main():
	L = myStudentList(Targil4input.teacherName,Targil4input.hujiMarks)
	D = myStudDict(L)
	print(D)
	print([L[len(L)-2],L[len(L)-1]])



