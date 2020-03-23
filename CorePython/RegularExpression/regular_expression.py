import re


# 1. 使用 match()方法匹配字符串
'''
# 函数试图从字符串的起始部分对模式进行匹配。
# 如果匹配成功，就返回一个匹配对象;如果 匹配失败，就返回 None，
# 匹配对象的 group()方法能够用于显示那个成功的匹配
'''

m = re.match('foo', 'food on table',)

if m is not None:
    print(m.group())


m = re.match('foo', 'seafood')

if m is None: print(m)


# 2. 使用 search() 在一个字符串中查找模式
'''
# search()会用它的字符串参数，在任意位置对给定正则表达式模式搜索第一次出现的匹配情况。
# 如果搜索到成功的匹配，就会返回一个匹配对象;否则，返回 None。
'''

s = re.search('foo', 'seafoof')
if s is not None: print(s.group())



# 3. 匹配多个字符串

bt = 'bat|bet|bit'

m = re.match(bt, 'bat')

if m is not None:
    print(m.group())


m = re.search(bt, 'He bit me!')

if m is not None: print(m.group())



# 4. 匹配任何单个字符
'''
# 点号(.)不能匹配一个换行符 \n 或者非字符，也就是说, 一个空字符串
'''

anyend = '.end'

m = re.match(anyend, 'bend')  # . 匹配 'b'

if m is not None:
    print(m.string)


m = re.match(anyend, 'end')  # 不匹配任何字符 匹配失败
if m is None:
    print(m)


m = re.match(anyend, '\nend')  # 除了 \n 以外的任何字符

if m is  None:
    print(m)



m = re.search(anyend, 'The end') # 在 搜索中匹配

if m is not None:
    print(m.group())


'''
# 在正则表达式中搜索一个真正的句点(小数点)，通过使用一个反斜线 对句点的功能进行转义
'''

patt314 = '3.14'  # 表示正则表达式的点号

pi_patt = '3\.14' # 表示字面量的点（dec .point）

m = re.match(patt314, '3014')  # 点匹配 0

if m is not None:
    print(m.group())

m = re.match(pi_patt, '3.14')  # 点号匹配 .

if m is not  None:
    print(m.group())



# 5. 创建字符集（[]）

m = re.match('[cr][23][dp][o2]', 'c2do')

if m is not None:
    print(m.group())

m = re.match('r2d2|c3po', 'c2do')

if m is None: print(m)




# 6. 重复、特殊字符以及分组
'''
#  简单电子邮件地址正则表达式  \w+@\w+\.com
#  正则表达式所允许的更多邮件地址,在域名前添加主机名称支持（如www.xxx.com），
#  主机名字是可选的  \w+@(\w+\.)?\w+\.com
'''

patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xxx.com')
if m is not None:
    print(m.group())


m = re.match(patt, 'nobody@www.xxx.com')
if m is not None:
    print(m.group())


'''用以下模式进一步扩展该示例，允许任意数量的中间子域名存在'''
patt = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt, 'nobody@www.xxx.yyy.zzz.com')
if m is not None:
    print(m.group())
'''
# 仅仅使用字母数字字符并不能匹配组成电子 邮件地址的全部可能字符。上述正则表达式不能匹配诸如 
# xxx-yyy.com 的域名或者使用非单 词\W 字符组成的域名
'''


'''
# 正则表达式模式\w+-\d+，它由连字符号分隔的字母数字字符串和数字组成，
# 使用圆括号来匹配和保存子组，以便于后续处理,添加一个子组来构造一个新的正则表达式 (\w+)-(\d+)来完成这项工作
'''
m = re.match('\w\w\w-\d\d\d', 'abc-123')
if m is not None:
    print(m.group())


m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
if m is not None:
    print(m.group())
    print(m.groups())
    print(m.group(2))
'''
# group()通常用于以普通方式显示所有的匹配部分，但也能用于获 取各个匹配的子组。
# 可以使用 groups()方法来获取一个包含所有匹配子字符串的元组
'''

m = re.match('(a(b))', 'ab')
if m is not None:
    print(m.group())
    print(m.groups())




# 7. 匹配字符串的起始和结尾以及单词边界

m = re.search('^The', 'The end.') # 匹配起始
if m is not None: print(m.group())


m = re.search('^The', 'end. The') #不作为起始
if m is None: print(m)


m = re.search(r'\bthe', 'bite the dog')  # 在边界
if m is not None: print(m.group())


m = re.search(r'\bthe', 'bitethe dog')  # 右边界，不作为左边界
if m is None: print(m)


m = re.search(r'\Bthe', 'bitethe dog') # 匹配没有边界
if m is not None: print(m.group())

m = re.search(r'dog$', 'bite the dog')
if m is not None: print(m.group())



# 8. 使用 findall() 和 finditer() 查找每一个出现的位置

m = re.findall('car', 'scary')
print(m)

m = re.findall('car', 'carry the barcarid to the car')
print(m)


'''
#  finditer()函数是在Python 2.2版本中添加回来的，这是一个与findall()函数类似但是更节省内存的变体。
#  两者之间以及和其他变体函数之间的差异(很明显不同于返回的是一个迭代 器还是列表)在于，和返回的
#  匹配字符串相比，finditer()在匹配对象中迭代。
'''
s = 'This and that. There and these'
m = re.findall(r'(th\w+) and (th\w+)', s, re.I)  # r.I 不区分大小写 同 r.IGNORECASE
print(m)


print([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)', s, re.I)])

m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
g = m.__next__()
print(g.group())
print(g.group(1))
print(g.group(2))
print(g.groups())

g = m.__next__()
print(g.group())
print(g.group(1))
print(g.group(2))
print(g.groups())



# 8. 使用 sub() 和 subn() 搜索和替换

'''
# sub()和 subn()。两者几乎一样，都是将某字符串中所有匹配正则表达式的部分进行某种形式的替换
# subn()和 sub()一样，但 subn() 还返回一个表示替换的总数，替换后的字符串和表示替换总数的
# 数字一起作为一个拥有两个 元素的元组返回。
'''

s = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
print(s)

sn = re.subn('X', 'Mr. Smith', 'attm: X\n\nDear X, \n')
print(sn)


s = re.sub('[ae]', 'X', 'abcdef')
print(s)

sn = re.subn('[ae]', 'X', 'abcdef')
print(sn)


t = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')

print(t)


t = re.subn(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')
print(t)



# 9. 在限定模式上使用 split() 分隔字符串
'''
# 如果给定分隔符不是使用特殊符号来匹配多重模式的正则表达式，那么 re.split()与 str.split()
# 的工作方式相同
'''

s = re.split(':', 'str1:str2:str3')
print(s)

DATA = ('Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA',
        )

for datum in DATA:
    print(re.split(', |(?=(?:\d{5}|[A-Z]{2})) ', datum))



# 10. 扩展符号
'''忽略大小写'''
print(re.findall(r'(?i)yes', 'yes? Yes. YES!!'))

print(re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel'))
'''跨行搜索'''
f = re.findall(r'(?im)(^th[\w ]+)', """This line is the first, \nanother line, \nthat line, \nit's the best""")
print(f)


''' re.S/DOTALL。该标记表明点号(.)能够用来表示\n 符号(反之其通常用于表示除了\n 之外的全部字符)'''
print(re.findall(r'th.+', """The first line, \nth\n, \nthe second line, \nthe third line"""))

print(re.findall(r'(?s)th.+', """The first line, \nth\n, \nthe second line, \nthe third line"""))


''' 
#  re.X/VERBOSE 该标记允许用户通过抑制在正则表达式中使用空白符(除了在字符类中或者在反斜线转义中)
#  来创建更易读的正则表达式。此外，散列、注释和井号 也可以用于一个注释的起始，
#  只要它们不在一个用反斜线转义的字符类中
'''
x = re.search(r'''(?x)
                  \((\d{3})\) # 区号
                  [ ]         # 空白符
                  (\d{3})     # 前缀
                  -           # 横线
                  (\d{4})     # 终点数字
                  ''', '(800) 555-1212').groups()
print(x)


'''
#  (?:...)可以对部分正则表达式进行分组，但是并不会保存该分组用于后续的检索或者应用。
#  当不想保存今后永远不会使用的多余匹配时，这个符号就非常有用
'''

s = re.findall(r'http://(?:\w+\.)*(\w+\.com)','http://google.com http://www.google.com http://code.google.com')
print(s)


'''
# (?P<name>) 和 (?P=name)符号。前者通过使用一个名称标 识符而不是使用从 1 开始增加到 N 的
# 增量数字来保存匹配，如果使用数字来保存匹配结 果，我们就可以通过使用\1,\2 ..., \来检索。可以使用一个类似风格的\g<name> 来检索它们。
# 使用后者，可以在一个相同的正则表达式中重用模式，而不必稍后再次在(相同) 正则表达式中指定相同的模式。
'''
s = re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212')
print(s.groupdict())


b = re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)', '(800) 555-1212 800-555-1212 18005551212')

print(bool(b))


'''(?=...) 和 (?!...)符号在目标字符串中实现一个前视匹配，而不必实际上使 用这些字符串。前者是正向前视断言，后者是负向前视断言'''
f = re.findall(r'\w+(?= van Rossum)', '''Guido van Rossum\nTim Peters\nAlex Martelli\nJust van Rossum\nRaymond Hettinger''')
print(f)

f = re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',''' sales@phptr.com \n postmaster@phptr.com \n eng@phptr.com \n noreply@phptr.com \n admin@phptr.com''' )
print(f)

v = ['%s@aw.com' % e.group(1) for e in re.finditer(r'(?m)^\s+(?!noreply|postmaster)(\w+)',''' sales@phptr.com \n postmaster@phptr.com \n eng@phptr.com \n noreply@phptr.com \n admin@phptr.com''' )]
print(v)


'''
# 特殊字符，它仅 仅包含字母“x”和“y”，我们此时仅仅想要这样限定字符串:两字母的字符串必须由一
# 个字母跟着另一个字母。换句话说，不能同时拥有两个相同的字母;要么由“x”跟着 “y”，要么相反。
'''
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))



# 11.杂项
m = re.match('\\bblow', 'blow')

if m: print(m.group())



# 命令行 输入 who 输出数据生成文件
import os

with os.popen('who', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.rstrip()))
















