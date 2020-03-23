#!/usr/bin/python
# -*- coding: utf-8 -*-

# 1. 字符串
print "Hello world"

message = "Hello kitty"
print message

# 2.Prthon中可以使用单引号或双引号来包括字符串，可以灵活的在字符串中包含双引号或单引号
string = 'I told my friend, "Python is my favorite language!"'
print string

string = "The language 'Python' is named after Monty Python, not the snake."
print string

# 3. 使用方法修改字符串的大小写
name = "ada lovelace"
print name.title()

name = "Ada Lovelace"
print name.upper()
print name.lower()


# 4. 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print full_name

print "Hello, " + full_name.title() + "!"

message = "Hello, " + full_name.title() + "!"
print message

# 5. 使用制表符或换行符来添加空白
print "Languages:\n\tPython\n\tC++\n\tJavascript"

# 6. 删除空白  "Python " 字符串中的空白是有有意义的, 确保字符窜末尾没有空白使用 rstrip（）
favorite_language = " Python "
print favorite_language.rstrip() #去掉结尾空白
print favorite_language.lstrip() #去掉开头空白


# 7. 使用函数 str() 避免类型错误
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print message








