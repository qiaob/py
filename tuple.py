#!/usr/bin/env python3

#tuple:不可变的list

tt=(1,2,3,4)


print(tt)

try:
	tt[2]=8
except:
	print("modify error")
else:
	print("modify success")

print(tt)


#当只有一个元素的时候 需要定义的时候需要多加，
tt=([1,2,3],)

print(tt)



#不可修改针对的是指向的引用，而不是指向的对象
try:
	tt[0][2]="8888"
except:
	print("modify error")
else:
	print("modify success")

print(tt)



