a=int(input("enter a number : "))

try:
	if a<=5:
		raise NameError
except NameError:
	print("Error................................. the number is less than or equal to 5")
else:
	print("no error")
finally:
	print("the execution is completed")