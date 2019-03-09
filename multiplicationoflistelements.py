#multiplication of all list elemnts
total = 1
list1 = [1,2,3,4,5] 
def multi():
	for ele in range(0, len(list1)): 
	total = total * list1[ele] 
	print("Sum of all elements in given list: ", total)
multi() 

