bulb = [1 for x in range(100)]
#print bulb


for i in range(2,101):
	for j in range(1,51):
		m = i*j
		if m <= 100:
			bulb[m-1] = not(bulb[m-1])
		#print bulb
		else:
			break
count = 0
for k in range(1,101):
	if bulb[k-1] == 1 :
		count+=1
print count, bulb[63]

