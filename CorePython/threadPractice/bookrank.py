
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
         "0132269937": "Core Python Programming",
         "0132356139": "Python Web Development with Django",
         "0137143419": "Python Fundamentals",
         }


def getRanking(isbn):
	'''获取排名列表'''
	'''
    根据ISBN，创建与AMazon服务器通信的最终url，然后打开这个地址。一旦服务器连接成功，就可以得到服务器返回的类似文件的对象。
    然后调用 read() 函数下载整个网页，以及关闭这个文件。
    如果正则表达式与预期一样精确，应当有且只有一个匹配
    因此从生成的列表中抓取这个值，并将其返回。
	'''
	page = uopen("%s%s" % (AMZN, isbn)) #str.format()isbn为国际标准书号
	data = page.read()
	page.close()
	return REGEX.findall(data.decode("utf-8"))[0] # 将bytes转变成string

def _showRanking(isbn):
	'''展示排名'''
	'''
	通过ISBN，查询其对应的书名，调用getRank()函数从Amazon 网站上获得这本书的当前排名，然后把这些值输出给用户。
	函数名前面的单下划线表示这是一个特殊函数，只能被模块的代码使用，不能被其他使用本文件作为库或者工具模块的应用导入
	'''
	print("- %r ranked %s" % (ISBNs[isbn], getRanking(isbn)))

def main():
 	print("At", ctime(), "on Amazon...")
 	threads = []
 	for isbn in ISBNs:
 		# _showRanking(isbn) # 单线程
 	  	thread = Thread(target=_showRanking, args=(isbn, ))
 	  	threads.append(thread)
 	  	# thread.start()

 	for t in threads:
 		t.start();


@register # 告知脚本何时结束
def _atexit():
	print("all DONE at:", ctime())

if __name__ == "__main__":
	main()

