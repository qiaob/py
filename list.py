#!/usr/bin/env python3

#list--help(list)


intList=[1,2,3,4,5,6,7,8]

print(intList)	#12345678


lists =intList.reverse()

print(lists)	#None

print(intList)	#87654321

print("lenth:",len(intList))

print("lastElement:",intList[-1])


iters =list.__reversed__(intList)

print("type:",type(iters))
#print("len:",len(iters)) ----no method
print(list(iters))


#intList.reverse()等价于
#intList = list(list.__reversed__(intList))
#区别是，第一个直接改变自己的顺序
#第二个不改变自己的顺序

intList[2]= "[1,2]"

print(intList)



