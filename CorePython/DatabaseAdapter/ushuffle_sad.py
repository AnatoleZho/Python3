'''首先导入 Python 标准库中的模块，然后是第三方或外部模块，最后是应用的本地模块'''
from distutils.log import warn as printf
from os.path import dirname
from random import randrange as rand
from sqlalchemy import Column, Integer, String, create_engine, exc, orm
from sqlalchemy.ext.declarative import declarative_base
from ushuffle import DBNAME, NAMELEN, randName, FIELDS, tformat, setup

DSNs = {'mysql': 'mysql://root@localhost/%s' % DBNAME, 'sqlite': 'sqlite://memory',}
# Base 类
Base = declarative_base()
# 定义与数据库操作等效的对象，继承自 Base 类
class Users(Base):
	# 属性，定义了映射的数据库表名
	__tablename__ = 'users'
	login = Column(String(NAMELEN))
	userid = Column(Integer, primary_key=True)
	projid = Column(Integer)
	def __str__(self):
		'''返回易于阅读的数据行的字符串格式'''
		return ''.join(map(tformat, (self.login, self.userid, self.projid)))

class SQLAlchemyTest(object):
	def __init__(self, dsn):
		try:
			'''尝试使用DSN创建数据库引擎'''
			eng = create_engine(dsn)
		except ImportError:
			raise RuntimeError()

		try:
			'''尝试数据库连接'''
			eng.connect()
		except exc.OperationalError:
			eng = create_engine(dirname(dsn))
			eng.execute('CREATE DATABASE %s' % DBNAME).close()
			eng = create_engine(dsn)
        '''创建一个会话对象，用于管理单独的事务对象，当涉及一个或多个数据库操作时，可以保证所有要写入的数据都必须提交'''
		Session = orm.sessionmaker(bind=eng)
		self.ses = Session()
		self.users = Users.__table__
		# 用引擎和表的元数据进行了额外的绑定，意味着表的所有操作都会绑定到这个指定的引擎中
		self.eng = self.users.metadata.bind = eng

	def insert(self):
		# 使用迭代的方式产生一系列插入操作
		self.ses.add_all(
			Users(login=who, userid=userid, projid=rand(1,5))
			for who, userid in rangName()
		)
		self.ses.commit()

	def update(self):
		fr = rand(1, 5)
		to = rand(1, 5)
		i = -1
		users = self.ses.query(Users).filter_by(projid=fr).all()
		for i, user in enumerate(users):
			user.projid = to
		self.ses.commit()
		return fr, to, i+1

	def delete(self):
		rm = rand(1,5)
		i = -1
		users = self.ses.query(Users).filter_by(projid=rm).all()
		for i, user in enumerate(users):
			self.ses.delete(user)
			return rm, i+1

	def dbDump(self):
		'''向屏幕上显示正确的输出'''
		printf('\n%s' % ''.join(map(cformat, FIELDS)))
		users = self.ses.query(Users).all()
		for user in users:
			printf(user)
		self.ses.commit()

	def __getattr__(self, attr):  # user for drop/create
	    '''
	    避开创建drop()和create()方法，因为创建这两个方法实际上只是分别调用了表的drop()和create()方法
	    __getattr__()方法只有在属行查找失败时才会被调用
	    当调用 orm.drop()并发现没有这个方法时，就会调用 getattr(orm,'drop').此时，调用 __getattr__(),并将属行名委托给self.users.
	    解释器会发现self.users 存在一个drop属行，然后传递这个方法调用self.users.drop()中。
	    '''
	    return getattr(self, users, attr)

	def finish(self):
		'''关闭连接的清理工作'''
		self.ses.connection().close()

def main():
	printf('*** Connection to %r database' % DBNAME)
	db = setup()
	if db not in DSNs:
		printf("\nERROR: %r not supported, exit" % db)
		return

	try: 
		orm = SQLAlchemyTest(DSNs[db])
	except RuntimeError:
		printf("\nERROR: %r not supported, exit" % db)
		return

	printf("\n*** Create users table (drop old one if appl.)")
	orm.drop(checkfirst=True)
	orm.create()

	printf("\n*** Insert names into table")
	orm.insert()
	orm.dbDump()

	printf('\n*** Move users to a random group')
	fr, to, num = orm.update()
	printf("\t(%d users moved) from (%d) to (%d)" % (num, fr, to))
	orm.dbDump()

	printf('\n*** Randomly delete group')
	rm, num = orm.delete()
	printf('\t(group #%d users removed)' % (rm, num))
	orm.dbDump()

	printf("\n*** Drop users table")
	orm.drop()
	printf("\n*** Close cxns")
	orm.finish()

if __name__ == "__main__":
	main()

