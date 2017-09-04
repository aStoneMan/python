#coding:utf-8

#引入正则表达式的包
import re

#创建一个正则表达式对象
#1.213   3.14  123.13  12345
pattern = re.compile('\d+\.\d+')

#提供要匹配的源字符串
src = "3.14,123123.123 1.345,123123, abc,1.23"

result = pattern.findall(src)

print src

print result

for res in result:
	print resduanzi