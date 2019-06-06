# _*_ coding :UTF-8 _*_
# author : momo
# DATE : 2019-06-06 22:23
# desc : input

import datetime

str  = input("name:")

print("name is:",str)


year = int(input("出生年份:"));

print("年龄：",datetime.datetime.now().year - year +1)

if (year >= 18):
    print("已成年")
else:
    print("未成年")
