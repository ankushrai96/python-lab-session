a=int(input("enter 1st number :"))
b=int(input("enter 2nd number :"))
c=int(input("enter 3rd number :"))

def max():
	if a>b and a>c:
		print("the largest number is :",a)
	elif b>a and b>c:
		print("the largest number is :",b)
	else:
		print("the largest number is :",c)
max()