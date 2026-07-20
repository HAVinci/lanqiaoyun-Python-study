for a in range(101):
	if a in [7,17,27,37,47,57,67,77,87,97]:
		continue
	elif a in range(70,80):
		continue
	elif (a%7) == 0:
		continue 
	print(a)
	a = a+1

