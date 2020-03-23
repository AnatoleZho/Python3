import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
	print("start loop", nloop, 'at:', ctime())
	sleep(nsec)
	print("loop", nloop, 'done at:', ctime())

def main():
	print('starting at:', ctime())
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target=loop, args=(i, loops[i]))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join() # wait for all threads to finished
		'''
        join()方法，其另一个重要方面是其实它根本不需要调用。一旦线程启动，它们就会一直执行，直到给定的函数完成后退出。
        如果主线程还有其他事情要去做，而不是等待这些线程完成，就可以不调用 join()。 join() 方法只有在你需要等待线程完成的时候才是有用的。
		'''

	print("all DONE at：", ctime())


if __name__ == '__main__':
	main()

