from random import randint
from time import sleep, ctime
from queue import Queue

import sys
sys.path.append("..")
from myThread import MyThread

def writeQ(queue):
	'''将一个对象放入队列'''
	print("producing object for Q...")
	queue.put("xxx", 1)
	print("size now", queue.qsize())

def readQ(queue):
	'''将一个对象移除移除队列'''
	val = queue.get(1)
	print("consumed object from Q... size now", queue.qsize())

def writer(queue, loops):
	'''向队列中添加一些列对象'''
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1, 3))

def reader(queue, loops):
	'''从队列中移除一系列对象'''
	for i in range(loops):
		readQ(queue)
		sleep(randint(2, 5))

funcs = [writer, reader] # 设置派生线程总数
nfuncs = range(len(funcs)) # 设置执行线程总数

def main():
	nloops = randint(2, 5)
	q = Queue(32)

	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()

	print("all DONE")

if __name__ == "__main__":
	main()





















