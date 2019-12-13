lines = open('input12.txt','r').read().strip().split('\n')
position = [tuple( int(j[2:]) for j in l[1:-1].split(', ')) for l in lines]
print(position)