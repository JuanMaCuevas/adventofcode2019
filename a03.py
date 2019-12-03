def line(i,direction,pos):
	delta={'U':(0,1),'R':(1,0),'D':(0,-1),'L':(-1,0)}
	d=tuple([i*x for x in delta[direction]])
	return tuple(map(sum, zip(pos, d)))

def path(wire):
	p = []
	pos=(0,0)
	for move in wire:
		p+=[line(x,move[0],pos) for x in range(1,int(move[1:])+1)]
		pos = p[-1]
	return p

n = open('input03.txt','r').read().split()
n=[x.split(',') for x in n]		
p1,p2=path(n[0]),path(n[1])
crosses = set(p1).intersection(set(p2))
mi= min(p1.index(c)+p2.index(c)+2 for c in crosses)
print(mi)
