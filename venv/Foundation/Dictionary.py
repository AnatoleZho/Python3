#!/usr/bin/python
# -*- coding: utf-8 -*-


#    字典
# 1. 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print alien_0['color']
print alien_0['points']

# 2. 使用字典
# 2.1.  访问字典中的值
new_points = alien_0['points']
print 'You just earned ' + str(new_points) + ' points.'

# 2.2. 添加键--值对
'''
字典是一种动态结构，可以随时在其中添加键--值对。
'''
print alien_0
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print alien_0

# 2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print alien_0

# 2.4 修改字典中的值
alien_0['color'] = 'yellow'
print 'The alien is now ' + alien_0['color'] + '.'

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print 'Original x-position: ' + str(alien_0['x_position'])
# 向右移动外星人
# 拒外星人当前速度决定其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print 'New x-position: ' + str(alien_0['x_position'])

alien_0['speed'] = 'fast'


# 2.5 删除键--值对   删除的键--值对永远消失了
alien_0 = {'points': 5, 'color': 'green'}
print alien_0
del alien_0['points']
print alien_0


# 2.6 由类似对象组成的字典
'''字典可以用来存储一个对象的多种信息，也可以使用字典来存储众多对象的同一种信息'''
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

print "Sarah's favorite language is " + favorite_languages['sarah'].title() + "."


# 3. 遍历字典    遍历字典的所有键--值对，键或值
# 3.1. 遍历所有的键--值对
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
for key, value in user_0.items():
    print '\nKey: ' + key
    print 'Value: ' + value
print '\n'

# 3.2. 遍历字典中的所有键
for name in favorite_languages.keys():
    print name.title()

# 3.3. 按顺序遍历字典中的所有键  使用 sort() 函数获取按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
    print name.title() + ", thank you for taking the poll."

# 3.4. 遍历字典中的所有值
print '\nThe following languages have been mentioned:'
for language in favorite_languages.values():
    print language.title()


# 3.5 遍历字典中所有不重复的值 使用集合 set
print '\nThe following language have been mentioned:'
for language in set(favorite_languages.values()):
    print language.title()


# 4. 嵌套
# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
# 可以在列表中嵌套字典，在字典中嵌套列表，甚至在字典中嵌套字典

# 4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print alien


# 4.2 在字典中存储列表
# 存储所点 pizza 的信息
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
         }
print 'You ordered a ' + pizza['crust'] + 'crust pizza ' + 'with the following toppings:'
for topping in pizza['toppings']:
    print '\t' + topping



# 4.3 在字典中存储字典
users = {'aeinstein':
             {'first': 'albert',
              'last': 'einstein',
              'location': 'princeton',
              },
         'mcurie':
             {'first': 'marie',
              'last': 'curie',
              'location': 'paris',
              },
         }
print '\n'
for username, user_info in users.items():
    print '\nUsername:' + username
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print '\tFull name:' + full_name.title()
    print '\tLocation: ' + location.title()







