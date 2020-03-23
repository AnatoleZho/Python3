'''
使用上下文管理锁

使用 with 语句，此时每个对象的上下文管理器负责在进入该套件之前调用 acquire() 并在完成执行后调用 release()
threading 模块的对象 Lock，RLock， Condition， Semaphore 和 BoundedSemaphore 都包含上下文管理器
也就是说，它们都可以使用 with 语句。当使用 with 时，可以进一步简化 loop() 循环
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

	with lock:
		remaining.add(myname)
		print("[%s] Started %s" % (ctime(), myname))

	sleep(nsec)

	with lock:
		remaining.remove(myname)
		print("[%s] Completed %s (%d secs)" % (ctime(), myname, nsec))
		print("   (remaining: %s)" % (remaining or "None"))

def main():
	'''派生和执行每个线程'''
	for pause in loops:
		Thread(target=loop, args=(pause, )).start()

if __name__ == "__main__":
	main()

@register # 用来注册 _atexit()函数，以便解释器在脚本退出前执行该函数
def _atexit():
	print("all DONE at:", ctime())

