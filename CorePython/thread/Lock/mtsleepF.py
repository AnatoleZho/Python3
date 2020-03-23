'''
锁和更多的随机性
'''

from atexit import register
from random import randrange
from threading import Thread, currentThread
from time import sleep, ctime
from threading import Lock

class CleanOutputSet(set):
	'''将默认输出改变为将其所有元素按照逗号分隔的字符串'''
	def __str__(self):
		return ', '.join(x for x in self)

# 随机数量的线程(3~6个线程)，每个线程暂停或睡眠2~4秒
loops = (randrange(2,5) for x in range(randrange(3, 7)))
# 集合类的实例
remaining = CleanOutputSet()
# 锁
lock = Lock()

def loop(nsec):
	'''线程要执行的任务'''
	myname = currentThread().name 	# 线程名
    
	lock.acquire() # 获取锁
	remaining.add(myname) # 添加线程名到 remaining 集合，
	print("[%s] Started %s" % (ctime(), myname))
	lock.release() # 释放锁

	sleep(nsec) # 睡眠几秒

	lock.acquire() # 重新获取线程锁
	remaining.remove(myname) # 从 remaining 集合中移除线程名
	print("[%s] Completed %s (%d secs)" % (ctime(), myname, nsec))
	print("   (remaining: %s)" % (remaining or "None"))
	lock.release() # 释放锁

def main():
	'''派生和执行每个线程'''
	for pause in loops:
		Thread(target=loop, args=(pause, )).start()

if __name__ == "__main__":
	main()

@register # 用来注册 _atexit()函数，以便解释器在脚本退出前执行该函数
def _atexit():
	print("all DONE at:", ctime())

