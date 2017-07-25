def p_num():
	print num
	num = 5
	print num

num = 10
p_num()
print num
#报错，因为在函数内发现同名变量，全局变量失效，所以在函数内无法输出num
#测试2def_demo.py 体会正常使用情况