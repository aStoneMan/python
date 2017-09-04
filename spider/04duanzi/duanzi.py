#coding:utf-8
import urllib2
import re

class Spider:
	'''
		这是一个内涵段子吧的 爬虫类
	'''
	def __init__(self):
		self.enable = True
		self.page = 2 #当前要去爬的第几页

	def load_page(self,page):
		'''
			发送内涵段子url请求，得到HTML源码
		'''
		url = "http://www.neihan8.com/article/index_"+str(page)+".html"
		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
		headers={'User-Agent':user_agent}
		req = urllib2.Request(url,headers = headers)
		response =urllib2.urlopen(req)
		html = response.read()
		#gbk_html = html.decode('gbk').encode('utf-8')
		#防止乱码，但是本程序报错，原因未知

		#用正则表达式过滤
		pattern = re.compile(r'<div class="desc">(.*?)</div>',re.S)
		item_list = pattern.findall(html)

		return item_list

	def deal_one_page(self,item_list,page):
		'''
			处理一页的数据
		'''
		print "***********第%d页的段子正在保存***********" %(page)
		for item in item_list:
			print item.replace("&amp;","").replace("&quot;","").replace("hellip;","")
			self.write_to_file(item)
		print "***********第%d页的段子保存完毕***********" %(page)


	def write_to_file(self,txt):
		'''
			存储文件
		'''
		print "正在存储文件"
		# 1 打开文件
		f = open("./myStory.txt",'a')
		# 2 读写文件
		f.write(txt)
		f.write('.................................')
		# 3 关闭文件
		f.close()

	def do_work(self):
		'''
			提供跟用户交互的过程
			让爬虫去工作
		'''
		while self.enable:
			print "按回车继续"
			print "输入quit退出"
			command = raw_input()
			if (command == "quit"):
				self.enable = False
				break;
			item_list = self.load_page(self.page)
			self.deal_one_page(item_list,self.page)
			self.page += 1



#main
if __name__ == '__main__':
	#创建一个spider对象
	mySpider = Spider()
	mySpider.do_work()
