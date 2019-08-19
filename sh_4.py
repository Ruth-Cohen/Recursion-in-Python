from collections import deque
import random
peopleNames = ("Iosi", "Ety")
verbs = ("sees", "plays", "sings" )
adjectives = ("tall", "small", "red" )
adverbs = ("slowly", "tomorrow", "now", "soon", "suddenly")
animateObjects = ("flowers", "oranges")
inanimateObjects = ("a stone", "a chair" )


def crPoem(N):
	listPeopleNames = list(map(lambda x:peopleNames[random.randrange(len(peopleNames))],range(N)))
	listVerbs = list(map(lambda x:verbs[random.randrange(len(verbs))],range(N)))
	listAdjectives = list(map(lambda x:adjectives[random.randrange(len(adjectives))],range(N)))
	listAdverbs = list(map(lambda x:adverbs[random.randrange(len(adverbs))],range(N)))
	listAnimateObjects = list(map(lambda x:animateObjects[random.randrange(len(animateObjects))],range(N)))
	listInanimateObjects = list(map(lambda x:inanimateObjects[random.randrange(len(inanimateObjects))],range(N)))
	return (list(map(lambda x: [listPeopleNames[x],listVerbs[x],listAdjectives[x],listAdverbs[x],listAnimateObjects[x],listInanimateObjects[x]],range(N))))
	

def theHumbletPoet(N):
	deque(map(lambda x:(deque(map(lambda y:print(y, end=" "),x))and print()),crPoem(N)))
	
	
inp = int(input('enter a valid number> '))
theHumbletPoet(inp)
	