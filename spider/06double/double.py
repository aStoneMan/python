#coding:utf-8
import urllib2
import re

class double(object):
	"""爬取数据"""
	def __init__(self):
		self.enable = True

	def load_page(self):
		'''
			获取html源码
		'''
		url = "http://datachart.500.com/ssq/history/history.shtml"		
		user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
		headers={'User-Agent':user_agent}
		req = urllib2.Request(url,headers = headers)
		response =urllib2.urlopen(req)
		html = response.read()
		pattern = re.compile(r'<tr class="t_tr1">(.*?)</tr>',re.S)
		item_list = pattern.findall(html)
		for item in item_list:
			item = item.replace("<!--<td>2</td>-->","").replace('<td class="t_cfont2">'," ").replace('<td class="t_cfont4">'," ").replace("</td>"," ").replace("<td>"," ").replace("&nbsp;"," ")
			self.write_to_file(item)

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
		
if __name__ == '__main__':
	#创建一个double对象
	double = double()
	double.load_page()