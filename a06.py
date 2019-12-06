def part1():
	orbits = open('input06.txt','r').read().split()
	
	orb={'COM':0}
	while orbits:
		cur = orbits.pop(0)
		a,b=cur.split(')')
		if a not in orb:
			orbits.append(cur)
		else:
			orb[b]=orb[a]+1
	print(sum(orb.values()))

def path(orb,leaf):
	# print(orb,leaf)
	s=set()
	while leaf!='COM':
		leaf=orb[leaf]
		s.add(leaf)
	return s

def part2():
	orbits = open('input06.txt','r').read().split()	
	orb={'COM':0}
	for cur in orbits:
		a,b=cur.split(')')
		orb[b]=a
	a = path(orb,'YOU')
	b = path(orb,'SAN')
	common=len(a.intersection(b))
	print(len(a)+len(b)-2*common)
	
	
part1()
part2()