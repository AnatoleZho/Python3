from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread # threading 模块包括两种信号量类：Semaphore 和 BoundedSemaphore 
from time import sleep, ctime

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX) # 计数器的值永远不会超过它的初始值 MAX，可以防范其中信号量释放次数多于获得次数的异常用例

def refill():
	'''糖果机所有者向库存中添加糖果'''
	'''
    临界区，获取锁是执行所有航的仅有方法。
    代码输出用户的行动，并在某人添加的糖果超过最大库存时给予警告
	'''
	lock.acquire()
	print("Refilling candy...."),

	try:
		candytray.release()
	except ValueError:
		print("full, skipping")
	else:
		print("OK")
	lock.release()

def buy():
	'''允许消费者获取一个单位的库存'''
	lock.acquire()
	print("Buying candy...."),
	'''
	这个调用一般会在计数器再次增加之前被阻塞。通过传入非阻塞的标志False，让调用不在阻塞
    而在应当阻塞的时候返回一个False，指明没有更多的资源了。
	'''
	if candytray.acquire(False): # 检测是否所有资源都已经消耗完，计数值不能小于0
		print("OK")
	else:
		print("empty, skipping")
	lock.release()

def producer(loops):
	for i in range(loops):
		refill()
		sleep(randrange(3))

def consumer(loops):
	for i in range(loops):
		buy()
		sleep(randrange(3))

def main():
	print("starting at:", ctime())
	nloops = randrange(4, 6)
	print("THE CANDY MACHINE (full with %d bars)!" % MAX)
	Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start() # buyer
	Thread(target=producer, args=(nloops,)).start() # vndr

@register
def _atexit():
	print("all DONE at:", ctime())

if __name__ == "__main__":
	main()


