"""
input map
. empty
# asteroid
x,y position

best position monitoring station
detect asteroid line of sight
at angle
"""
import math
import operator

resta = lambda a,b:[x1 - x2 for (x1, x2) in zip(a, b)]
distancia = lambda a,b: math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


mapa = """
.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##
""".strip()


mapa = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()

mapa=open('input10.txt','r').read().strip()

x,y=0,0
ast=[]

for c in mapa:
	if c=='#':
		ast.append((x,y))
	if c=='\n':
		y+=1
		x=0
	else:
		x+=1

dlof={}
for a in ast:
	dlof[a]=set()
	for b in ast:
		if a==b:
			continue
		x,y = resta(a,b)
		dlof[a].add(math.atan2(x,y))
	dlof[a]=len(dlof[a])

def angle(a,b):
	x,y = resta(b,a)
	return math.atan2(x,-y) + (2 * math.pi * 1 if x<0 else 0)

#part1
station = sorted(dlof.items(),key=lambda x:x[1])[-1]
x=station[0]
print(f'Station at {x} can see {station[1]} asteroids')

#part 2
dlof=[]
a=x
for b in ast:
	if a==b:
		continue
	dlof.append([angle(a,b),distancia(a,b),b])
dlof = sorted(dlof, key = lambda x:(x[0],x[1]))

vap=1
pos=0
while dlof:
	cur=dlof.pop(pos)
	if vap==200:
		break
	angle = cur[0]
	while pos<len(dlof) and dlof[pos][0]==angle:
		pos+=1
	if pos==len(dlof):
		pos=0
	vap+=1

x,y=cur[-1]
print(f'200th asteroid {cur[-1]}: {x*100+y}')




