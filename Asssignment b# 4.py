Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> n=input("Enter a number ")
Enter a number 12
>>> if int(n)%2==0:
	print("The given number is an even number")

	
The given number is an even number
>>> 
>>> n=input("Enter a number ")
Enter a number 11
>>> if int(n)%2==0:
	print("The given number is an even number")
	else:
		
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> else:print("The given number is an odd number")
SyntaxError: invalid syntax
>>> else:
	
SyntaxError: invalid syntax
>>> print("The given number is an odd number")
The given number is an odd number
>>> a=input("Enter first value ")
Enter first value 5
>>> b=input("Enter second value ")
Enter second value 8
>>> if int(a)>int(b) :
	print(a," is greater")

	
>>> elif int(b)>int(a):
	
SyntaxError: invalid syntax
>>> if int(a)>=2
SyntaxError: invalid syntax
>>> if int(a)>=2:
	print(a)

	
5
>>> elif int(b)>=6:
	
SyntaxError: invalid syntax
>>>  if int(a)>int(b) :
	 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> if int(a)>int(b) :
	print(a," is greater")
else:
	if int(b)>int(a) :
		print(b," is greater")
	else:
		print("Both are equal values")

		
8  is greater
>>> 
