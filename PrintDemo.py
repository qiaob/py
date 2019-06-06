# _*_ coding :UTF-8 _*_
# author : momo
# DATE : 2019-06-06 22:10
# desc : print


# 控制台
print("hello")
print(chr(99))


# 输出数据到文件
fp = open("./out/printout.txt", "w+")
print("test print to file", file=fp)
fp.close()


import datetime

print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)


print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))