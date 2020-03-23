from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime
import re

tlds = ('com', 'edu', 'net', 'org', 'gov')

strs = []

for i in range(randrange(5, 11)):
	dtint = randrange(2**32) # pick date   64位系统，这样得到的maxint值为9223372036854775807 因此用 2**32
	dtstr = ctime(dtint)       # date string 
	llen = randrange(4, 8)     # login is shorter
	login = ''.join(choice(lc) for j in range(llen))
	dlen = randrange(llen, 13) # domain is longer
	dom = ''.join(choice(lc) for j in range(dlen))
	finalStr = dtstr + '::' + login + '@' + dom + '.' + choice(tlds) + '::' + str(dtint) + '-' + str(llen) + '-' + str(dlen)
	strs.append(finalStr)
	print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

print(strs)

with open('rand_data.py', 'w') as f:
	for str in strs:
		f.write(str + '\n')

with open('rand_data.py', 'r') as f:
	lines = f.readlines()

# patt = '.+\d+-\d+-\d+'
# for line in lines:
# 	print(re.match(patt, line).group())


# patt = '.+(\d+-\d+-\d+)'
# for line in lines:
# 	print(re.match(patt, line).group(1))


# patt = '.+?(\d+-\d+-\d+)' # 取d-d-d 分组
# for line in lines:
# 	print(re.match(patt, line).group(1))


patt = '.+-(\d+)-'  # 取中间数字
for line in lines:
	print(re.match(patt, line).group(1))


