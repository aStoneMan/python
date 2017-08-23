#coding:utf-8

def load_page(url):
	'''
		发送url请求
		返回url请求的静态html页面
	'''
	import urllib2
	user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
	headers={'User-Agent':user_agent}
	req = urllib2.Request(url,headers = headers)
	response =urllib2.urlopen(req)
	html = response.read()
	print html
	# return html

def write_to_file(file_name,txt):
	'''
		将txt文本 存入到file_name文件中
	'''
	print "正在存储文件" + file_name
	# 1 打开文件
	f = open(file_name,'w')
	# 2 读写文件
	f.write(txt)
	# 3 关闭文件
	f.close()




def tieba_spider(url,begin_page,end_page):
	'''
		贴吧小爬虫
	'''
	for i in range(begin_page,end_page+1):
		# i = 1, pn = 0
		# i = 2, pn = 50
		# i = 3, pn = 100
		pn = 50 * (i - 1)

		#组成一个完整的url
		my_url = url +str(pn)
		print "请求的地址"
		print my_url
		html = load_page(my_url)

		# print "=====================第 %d 页================" %(i)
		# print html
		# print "=============================================" 
		file_name = str(i) + ".html"
		write_to_file(file_name,html)

#main
if __name__ =="__main__":
	url = raw_input('请输入url地址')
	# print url
	begin_page = int(raw_input("请输入起始页码"))
	end_page = int(raw_input("请输入终止页码"))

	# print begin_page
	# print end_page
	tieba_spider(url,begin_page,end_page)