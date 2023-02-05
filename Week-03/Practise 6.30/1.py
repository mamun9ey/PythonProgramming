#Take 10 space-separted integer and make a list.Then find the sum and average of these all numbers.
L = [4, 5, 1, 2, 9, 7, 10, 8,20,85]
sum = 0
for i in L:
	sum += i
avg = sum/len(L)
print("sum = ", sum)
print("average = ", avg)
