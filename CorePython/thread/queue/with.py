'''
with 语句的原理
1.上下文管理协议（Context Management Protocol）：包含方法__enter__() 和 __exit__(),支持该协议的两个对象要实现这两个方法
2.上下文管理器（Context Manager）：支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__()方法。
  上下文管理器定义执行 with 语句时要建立的运行时上下文，负责执行 with 语句块上下文的进入与退出操作。通常使用 with 语句调用上下文管理器
  也可以通过直接调用其方法来使用。
'''

# with EXPR as VAR:
# 	
# 	BLOCK

'''
其中 EXPR 可以是任意表达式；as VAR 是可选的。其一般的执行过程：
1. 执行 EXPR，生成上下文管理器 context_manager;
2. 获取上下文管理器的__exit__() 方法，并保存起来用于之后的调用
3. 调用上下文管理器的__enter__() 方法，使用了 as 子句，则将__enter__() 方法的返回值赋值给as 子句中的 VAR；
4. 执行 BLOCK 中的表达式；
5. 不管是否执行过程中是否发生了异常，执行上下文管理器的__exit__() 方法，__exit__() 方法负责执行‘清理’工作，
   如释放资源等。如果执行过程中没有出现异常，或者语句体重执行了语句 break/continue/return,则以 None 作为
   参数调用__eixt__(None, None, None);如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用
   __exit__(exc_type, exc_value, exc_traceback);
6. 出现异常时，如果__exit__(type, value, traceback) 返回 False， 则会重新跑出异常，让 with 之外的语句来处理异常，
   这也是通用的做法；如果返回 True，则忽略异常，不再对异常进行处理
'''

# 自定义上下文管理器

class DBManager(object):
	def __init__(self):
		pass

	def __enter__(self):
		print("__enter__")
		return self

	def __exit__(self, exc_type, exc_value, exc_tb):
		print("__exit__")
		return True

def getInstance():
	return DBManager()

with getInstance() as dbManagerIns:
	print("with demo")



class With_work(object):
	def __enter__(self):
		'''进入with语句的时候被调用'''
		print("enter called")
		return "text"

	def __exit__(self, exc_type, exc_value, exc_tb):
		'''离开with的时候被with调用'''
		print("exit called")

with With_work() as f:
	print(f)
	print("Hello with")
	













