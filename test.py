a = [0,0,0,0]
def Try(i):
	for j in ['covered', 'flag']:
		a[i] = j
		if i == 3:
			print(a)
		else:
			Try(i + 1)
Try(0)
print(a)