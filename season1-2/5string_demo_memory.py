#coding=utf-8
str = "this is python"
print id(str)
str = "i am py"
print id(str)
#两次的内存地址不一样是因为Python先在内存放入字符串，再把str指向该内存，原来的字符串如果没被再用，会在内存回收的时候清空
var = "this is python"
print id(var)
#和第一次str内存地址一样，证明该字符串还没有被回收。
var2 = 'this is python'
print id(var2)
#两种字符串声明方式（用单引号或者双引号），在内存存储是一样的