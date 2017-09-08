#coding:utf-8
import urllib2
import re

class icp(object):
	"""爬取数据"""
	def __init__(self):
		self.enable = True

	def read_from_file(self):
		'''
			打开文件
		'''
		f = open("url.txt")
		line = f.readline() 
		while line:  
		    line = f.readline()
		    line =line[:-1]
		    self.load_page(line)

		f.close()  

	def load_page(self,url):
		'''
			获取html源码
		'''
		allurl = "http://icp.chinaz.com/"+str(url)	
		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
		headers={'User-Agent':user_agent}
		req = urllib2.Request(allurl,headers = headers)
		response =urllib2.urlopen(req)
		html = response.read()
		pattern = re.compile(r'<li class="bg-gray clearfix"><span>主办单位名称</span><p>(.*?)<a class="fz12 pl5" id="showVcode" style="cursor:pointer">',re.S)
		item_list = pattern.findall(html)
		for item in item_list:
			self.write_to_file(url,item)
			print item

	def write_to_file(self,url,txt):
		'''
			存储文件
		'''
		print "正在存储文件"
		# 1 打开文件
		f = open("./icp.txt",'a')
		# 2 读写文件
		f.write('-----------'+url+'----------\r\n')
		f.write(txt)
		f.write('\r\n----------------------------\r\n\r\n\r\n')
		# 3 关闭文件
		f.close()
		
if __name__ == '__main__':
	#创建一个对象
	icp = icp()
	icp.read_from_file()