#coding=utf-8
dict = {'a' : 123,'b' : 456}
print dict
print dict['a']
dict['a'] = 789
print dict
#字典就是键值对
#字典可以被修改

for key in dict:
	print key,dict[key]