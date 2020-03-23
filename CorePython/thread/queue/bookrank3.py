
from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen
from concurrent.futures import ThreadPoolExecutor

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
 	'''
    ThreadPoolExecutor 参数是线程池的大小，
    这是一个I/O密集型应用，因此多线程更有用。对于计算密集型引用而言，可以使用 concurrent.futures.ProcessPoolExecutor来替代
 	'''
 	# with ThreadPoolExecutor(3) as executor: # with 上下文管理器
 	# 	for isbn in ISBNs:
 	# 		executor.submit(_showRanking, isbn)
 	with ThreadPoolExecutor(3) as executor:
 		for isbn, ranking in zip(ISBNs, executor.map(getRanking, ISBNs)):
 			print("- %r ranked %s" % (ISBNs[isbn], ranking))


@register # 告知脚本何时结束
def _atexit():
	print("all DONE at:", ctime())

if __name__ == "__main__":
	main()


'''
由于 Python 的 GIL 的限制，多线程更适合于I/O密集型应用（I/O释放了GIL，可以允许更多的并发（Global Interpreter Lock，全局解释锁，
保证了同一时刻只有一个线程在一个CPU上执行字节码，无法将多个线程银蛇到多个CPU上。这是CPython解释器的缺陷。
GIL被设计来保护线程安全，由于多线程共享变量，如果不能很好的进行线程同步，多线程很容易将线程改乱）），而不是计算密集型应用。
对于后一种情况，为了更好的实现并发性，需要使用多进程，以便让CPU的其他内核来执行。

subprocess 模块
  这是派生进程的主要替代方案，可以单独地执行任务，或者通过标准文件（stdin，stdout，stderr）进行进程间通信

multiprocessing 模块
   允许为多核或多CPU派生进程，其接口与 threading 模块非常相似。该模块同样也包括在共享任务的进程间传输数据的多种法师。

concurrent.futures 模块
   这是一个新的高级库，它只在‘任务’级别进行操作，不需要过分关注同步和线程/进程的管理。只需要指定一个给定了“worker”数量的线程/进程池，
   提交任务，然后整理结果。
'''
