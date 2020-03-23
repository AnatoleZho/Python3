from distutils.log import warn as printf # 使用distutils.log.warn() 来替代 Python 2 中的 print 和 Python 3 中的 print()
import os
from random import randrange as rand

'''用于找出正确的函数以命名为 scanf() '''
if isinstance(rrrr, dict) and 'raw_input' in __builtins__:
	scanf = raw_input
elif hasattr(__builtins__, 'raw_input'):
	scanf = raw_input
else:
	scanf = input


COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DBNAME = 'test'
DBUSER = 'root'
DB_EXC = None
NAMELEN = 16


tformat = lambda s: str(s).title().ljust(COLSIZ) # 标题样式格式化函数
cformat = lambda s: s.upper().ljust(COLSIZ) # 全大写格式化函数

def setup():
	return RDBMSs[input('''
        Choose a database system:
        (M)ySQL
        (G)adfly
        (S)QLite
        Enter choice: 
		''').strip().lower()[0]]

def connect(db, DBNAME):
	'''数据库一致性访问的核心，尝试加载对应的数据库模块'''
	global DB_EXC # 表示数据库异常
	dbDir = '%s_%s' % (db, DBNAME)
	if db == 'sqlite':
		try:
			import sqlite3
		except ImportError:
			return None

		DB_EXC = sqlite3
		if not os.path.isdir(dbDir):
			os.mkdir(dbDir)
		cxn = sqlite.connect(os.path.join(dbDir, DBNAME))

	elif db == 'mysql':
		try: 
			import MySQLdb
			import _mysql_exceptions as DB_EXC

			try: 
				cxn = MySQLdb.connect(db=DBNAME)
			except DB_EXC.OperationalError:
				try: 
					cxn = MySQLdb.connect(user=DBUSER)
					cxn.query('CREATE DATABASE %s' % DBNAME)
					cxn.commit()
					cxn.close()
					cxn = MySQLdb.connect(db=DBNAME)
				except DB_EXC.OperationalError:
					return None
		except ImportError:
			try:
				import mysql.connector
				import mysql.connector.errors as DB_EXC
				try:
					cxn = mysql.connector.Connect(**{
						'database': DBNAME,
						'user': DBUSER,
						})
				except DB_EXC.InterfaceError:
					return None
			except ImportError:
				return None
	elif db == 'gadfly':
		try:
			from gadfly import gadfly
			DB_EXC = gadfly
		except ImportError:
			return None

		try:
			cxn = gadfly(DBNAME, dbDir)
		except IOError:
			cxn = gadfly()
			if not os.path.isdir(dbDir):
				os.mkdir(dbDir)
			cxn.startup(DBNAME, dbDir)
	else:
		return None

	return cxn

def create(cur):
	'''在数据库中创建一个新表users'''
	try:
		cur.execute('''
			CREATE TABLE users (
			login VARCHAR(%d),
			userid INTEGER,
			projid INTEGER)
			''' % NAMELEN)
	except DB_EXC.OperationalError:
		drop(cur)
		create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')

NAMES = (('aaron', 8312), ('angela', 7603), ('dave', 7306),('davina', 7902), ('elliot', 7911),
	     ('ernie', 7410), ('jess', 7912), ('jim', 7512), ('larry', 7311), ('leslie', 7808),
	     ('melissa', 8607), ('faye', 6812), ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
	    )

def randName():
	'''生成器：将 NAMES 转化成集合，每次从集合中删除一个名字，直到所有名字都耗尽'''
	pick = set(NAMES)
	while  pick:
		yield pick.pop()

def insert(cur, db):
	'''对于每个用户名-用户ID对，都会被分配到一个项目组中，(给予其项目ID， 即proid)。项目ID 是从4个不同的组中随机选出的'''
	if db == 'sqlite':
		cur.executemany("INSERT INTO users VALUES(?, ?, ?)", [(who, uid, rand(1, 5)) for who, uid in randName()])
	elif db == 'gadfly':
		for who, uid in randName():
			cur.execute("INSERT INTO users VALUES(?, ?, ?", (who, uid, rand(1, 5)))
	elif db == 'mysql':
		cur.executemany("INSERT INTO users VALUES(%s, %s, %s)", [(who, uid, rand(1, 5)) for who, uid in randName()])

# 条件运算符，用于返回最后一次操作后影响的行数，不过如果游标对象不支持该属性，则返回-1.
getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
	'''随机选择项目组中的成员。将其从当前组移动到另一个随机选择组中'''
	fr = rand(1, 5)
	to = rand(1, 5)
	cur.execute("UPDATE users SET projid=%d WHERE projid=%d" % (to, fr))
	return fr, to, getRC(cur)

def delete(cur):
	'''最忌选择项目组中的成员，将该组的成员全部删除'''
	rm = rand(1, 5)
	cur.execute('DELETE FROM users WHERE projid=%d' % rm)
	return rm, getRC(cur)

def dbDump(cur):
	'''从数据库中拉去所有行，将其按照打印格式进行格式化，然后显示给用户'''
	cur.execute('SELECT * FROM users')
	printf("\n%s" % ''.join(map(cformat, FIELDS)))
	for data in cur.fetchall():
		printf(''.join(map(tformat, data)))

def main():
	db = setup()
	printf("*** Connect to %r database" % db)
	cxn = connect(db)
	if not cxn:
		printf("ERROR:%r not supported or unreachable, exit" % db)
		return
	cur = cxn.cursor()

	printf("\n*** Creating users table")
	create(cur)

	printf("\n*** Inserting names into table")
	insert(cur, db)
	dbDump(cur)

	printf("\n*** Randomly moving folks")
	fr, to, num = update(cur)
	printf("\t(%d users moved) from (%d) to (%d)" % (num, fr, to))
	dbDump(cur)

	printf('\n*** Randomly choosing group')
	rm, num = delete(cur)
	printf("\t(group #%d; %d users removed)" % (rm, num))
	dbDump(cur)

	printf('\n*** Dropping users table')
	drop(cur)
	print('\n*** Close cxns')
	cur.close()
	cxn.commit()
	cxn.close()

if __name__ == '__main__':
	main()


























