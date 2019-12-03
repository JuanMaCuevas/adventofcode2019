n = open('input01.txt','r').read().split()
n=[int(x)for x in n] 


def fuel(mass):
	s = 0
	f=mass//3-2
	while f>0:
		s+=f
		f=f//3-2
	return s

n=sum(fuel(x) for x in n)
print(n)