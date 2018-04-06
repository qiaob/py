#!/usr/bin/env python3

#input from stdin
inputStr = input("please input a number:")


# try:
#	....code
# except [ExceptionName]:
#	....if exception need to do code
# else:
#	....if no exception to do ..


try:
	#convert str to int 
	inputStr = int(inputStr)
#catch an Exception	
except Exception:
	print("you input number not a int value")
else:
	if inputStr%2==0:
		print(inputStr," is a even")
	else:
		print(inputStr,"is a odd")
