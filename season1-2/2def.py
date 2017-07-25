def p_num():
	num = 5
	print num

num = 10
p_num()
print num
#输出为
#5
#10
#当在函数中出现同名局部变量时，全局变量失效
#测试2def_error.py深入理解