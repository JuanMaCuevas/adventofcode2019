import collections
import itertools

def value(p,i,arg):
	return p[i+arg] if str(p[i]).zfill(5)[-arg-2]=='1' else p[p[i+arg]]

def add(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	p[p[i+3]]=a+b
	return i+4

def mul(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	p[p[i+3]]=a*b
	return i+4

def read(p,i,inp):
	print('entra datos',inp)
	p[p[i+1]]=inp
	return i+2


def write(p,i,output):
	a=value(p,i,1)
	print('adds to output',a)
	output.append(a)
	return i+2

def jumpEq(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	if a==0:
		return b
	return i+3

def jumpNotEq(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	if a!=0:
		return b
	return i+3

def lt(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	p[p[i+3]]=1 if a<b else 0
	return i+4

def eq(p,i):
	a=value(p,i,1)
	b=value(p,i,2)
	p[p[i+3]]=1 if a==b else 0
	return i+4

ops={1:add,2:mul,4:write,5:jumpNotEq,6:jumpEq,7:lt,8:eq}

def run(prog,inp):
	# print(inp)
	p=list(prog)#.copy()
	output=[]
	i=0
	while i<len(p):
		op=int(str(p[i]).zfill(5)[-2:])
		if op==99:
			break
		if op==3:
			i=read(p,i,inp)
		elif op==4:
			i=write(p,i,output)
		else:	
			f=ops.get(op,None)
			if f:
				i=f(p,i) 
			else:
				print('error: unkown opcode')
				break
	return output

def runIO(prog):
	# print(inp)
	p=list(prog)#.copy()
	output=[]
	i=0
	while i<len(p):
		op=int(str(p[i]).zfill(5)[-2:])
		if op==99:
			break
		if op==3:
			i=read(p,i,int(input()))
		elif op==4:
			i=write(p,i,output)
			print(output[-1])
		else:	
			f=ops.get(op,None)
			if f:
				i=f(p,i) 
			else:
				print('error: unkown opcode')
				break
	return output

def runSequence(p,seq):
	inp = 0
	o=[]
	for s in seq:
		# print(s,inp)
		inp=run(p,[s,inp])[0]
		o.append(inp)
	return inp


def part1(p):
	res=[]
	for c in itertools.permutations([0,1,2,3,4]):
		r = runSequence(p,c)
		res.append(r)
	print(max(res))

def part2(p):
	res=[]
	namps=5
	
	
	for c in itertools.permutations(list(range(5,5+namps))):
		print('--------------------')
		amps = [Amplifier(p) for x in range(namps)]
		prev=0
		for i,s in enumerate(zip(amps,c)):
			s[0].runIn([s[1],prev])	
			prev=s[0].getOut()[0]
		
		i=0
		while True:
			amps[i].runIn(prev)
			prev = amps[i].getOut()
			print('prev',prev)
			i=i+1 if i<namps else 0
		print(prev)
			

	# print(max(res))


def main():
	n = open('input07.txt','r').read().split(',')
	n=[int(x)for x in n]
	x=[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
	# part1(x)
	part2(x)
	# runIO(x)

class Amplifier:
	def __init__(self,program):
		self.program=list(program)
		self.pi=0
		self.output = []
		self.finished = False

	def runIn(self,inp):
		
		while self.pi<len(self.program):
			op=int(str(self.program[self.pi]).zfill(5)[-2:])
			if op==99:
				self.finished=True
				break
			if op==3:
				self.pi=read(self.program,self.pi,inp.pop(0))
			elif op==4:
				self.pi=write(self.program,self.pi,self.output)
				# print(self.output)
				break
			else:	
				f=ops.get(op,None)
				if f:
					self.pi=f(self.program,self.pi) 
				else:
					print('error: unkown opcode')
					break


	def getOut(self):
		return self.output
		






main()
