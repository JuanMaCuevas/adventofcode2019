import collections

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

def read(p,i):
	p[p[i+1]]=int(input())
	return i+2


def write(p,i):
	a=value(p,i,1)
	print(a)
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

ops={1:add,2:mul,3:read,4:write,5:jumpNotEq,6:jumpEq,7:lt,8:eq}

def run(p):
	i=0
	while i<len(p):
		op=int(str(p[i]).zfill(5)[-2:])
		if op==99:
			break
		f=ops.get(op,None)
		if f:
			i=f(p,i) 
		else:
			print('error: unkown opcode')
			break
	return p

def main():
	n = open('input05.txt','r').read().split(',')
	n=[int(x)for x in n]
	run(n)

main()
