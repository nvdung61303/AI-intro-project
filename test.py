# a = [0,0,0,0]
# def Try(i):
# 	for j in ['covered', 'flag']:
# 		a[i] = j
# 		if i == 3:
# 			print(a)
# 		else:
# 			Try(i + 1)
# Try(0)
# print(a)
a = [1,2,3,4,5]
b = [4,3,2]
for ele in b:
	a.remove(ele)
print(a)