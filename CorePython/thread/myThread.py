import threading
from time import ctime

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func, args, name=''):
		super(MyThread, self).__init__()
		self.name = name
		self.func = func
		self.args = args
	
	def getResult(self):
		return self.res

	def run(self):
		print("starting", self.name, 'at:', ctime())
		self.res = self.func(*self.args)
		print(self.name, 'finished at:', ctime())
