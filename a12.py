lines = open('input12.txt','r').read().strip().split('\n')
# lines = """<x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>""".split('\n')

from dataclasses import dataclass
@dataclass
class Moon:
	pos: list
	vel: list
	pot: int
	kin: int


def new_velocity(v,posA,posB): 
	for i in range(3):
		a,b=posA[i],posB[i]
		if a<b:
			v[i] += 1
		elif a>b:
			v[i] -= 1
	return v

def new_pos(pos,vel):
	return [pos[i]+vel[i] for i in range(3)]

def show(moons):
	for m in moons:
		print(m)
	print()

def total_energy(moons):
	return sum(m.kin*m.pot for m in moons)

def step(moons):
	for a in moons:
		for b in moons:
			if a==b:
				continue
			a.vel=new_velocity(a.vel,a.pos,b.pos)
			
	for a in moons:
		a.pos=new_pos(a.pos,a.vel)
		a.pot = sum(abs(x) for x in a.pos)
		a.kin = sum(abs(x) for x in a.vel)

	return moons
# show(moons)


def main():
	
	moons = [[[ int(j[2:]) for j in l[1:-1].split(', ')],[0,0,0]] for l in lines]
	moons = [Moon(pos=m[0],vel=m[1],pot=0,kin=0) for m in moons]
	part2(moons)


def part1(moons):
	for i in range(1000):	
		step(moons)
	print(total_energy(moons))
	
def hash_state(moons):
	flat_list = [item for sublist in [m.pos+m.vel for m in moons] for item in sublist]
	return hash(tuple(flat_list))


def part2(moons):
	states = set()
	stat = hash_state(moons)
	count=0
	while stat not in states:
		states.add(stat)
		moons=step(moons)

		stat = hash_state(moons)
		count+=1
		if count%1000==0:
			print(count)
	print(count)

main()






