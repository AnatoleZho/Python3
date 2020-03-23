import _thread
from time import sleep, ctime

def loop0():
	print("start loop 0 at:", ctime())
	sleep(4)
	print("loop 0 done at:", ctime())

def loop1():
	print("start loop 1 at:", ctime())
	sleep(2)
	print("loop 1 done at:", ctime())

def main():
	print("starting at:", ctime())
	_thread.start_new_thread(loop0, ())
	_thread.start_new_thread(loop1, ())
	sleep(6) # 阻止主线程继续执行，使得子线程执行完毕后再继续执行下一句代码， 否则两个子线程会将直接终止
	print("all DONE at:", ctime())

if __name__ == '__main__':
	main();