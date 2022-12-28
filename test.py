a = [0,0,0,0]
def Try(i):
	for j in [0, 1]:
		a[i] = j
		if i == 3:
			print(a)
		else:
			Try(i + 1)
Try(0)