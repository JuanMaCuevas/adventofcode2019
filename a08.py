im = open('input08.txt','r').read().strip()
# print(im[:10])

def part1(im):
	size = (25*6)
	layers = len(im)//size
	minzero=size
	minlay=0
	for layer in range(layers):
		lay = im[layer*size:(layer+1)*size]
		zeros = sum(1 for x in lay if x=='0')
		if zeros<minzero:
			minlay=lay
			minzero=zeros
	print(minlay)
	ones = sum(1 for x in minlay if x=='1')
	twos = sum(1 for x in minlay if x=='2')
	print(ones*twos)
	
def part2(im):
	
	size = (25*6)
	img=['2']*size
	layers = len(im)//size
	# print(''.join(img))
	for layer in range(layers):
		lay = im[layer*size:(layer+1)*size]

		for i,v in enumerate(lay):
			if img[i]=='2':
				img[i]=lay[i]
		# print(''.join(img))

	for i in range(6):
		line = ''.join(img[i*25:(i+1)*25])
		line=line.replace('1','1')
		line=line.replace('0',' ')
		print(line)
	# print(''.join(img))

part2(im)

