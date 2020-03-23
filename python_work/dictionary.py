# 字典

# 1. 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# 2. 使用字典
# 2.1. 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0["color"])
 
# 2.2.  添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 2.3 创建一个空字典
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# 2.4 修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0)

# 2.5 删除键-值对
del alien_0['points']

print(alien_0)

# 2.6 由类似对象组成的字典
#      字典存储可以存储一个对象的多种信息，也可以存储众多对象的同一种信息
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'phil': 'python',
                      }

print("Sarah's favorite is " + favorite_languages['sarah'].title() + '.')


# 3. 遍历字典
# 3.1 遍历所有的键-值对
user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
	
          }

for key, value in user_0.items():
	print('\nKey: ' + key)
	print('Value: ' + value)


for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + '.')

# 3.2 遍历字典中的所有键
for name in favorite_languages.keys():
	print(name.title())

# 3.3 按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title() + ', thank you for taking the poll.')

# 3.4 遍历字典中的所有值
for language in favorite_languages.values():
	print(language.title())


# 4. 嵌套    将一系列字典存储在列表中，获奖列表作为值存储在字典中。
# 4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# 4.1 在字典中存储列表
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra cheese'],
         }

print('You ordered a ' + pizza['crust'] + '-crust pizza ' + 'with the following toppings:')

for topping in pizza['toppings']:	
	print('\t' + topping)


favorite_languages = {'jen': ['python', 'ruby'],
                      'sarah': ['c'],
                      'edward': ['ruby', 'go'],
                      'phil': ['python', 'haskell'],
                      }

for name, languages in favorite_languages.items():
	print('\n' + name.title() + "'s favorite languages are:")
	for language in languages:
		print('\t' + language.title())

# 4.3 在字典中存储字典
users = {'aeinstein': {'first': 'albert', 'last': 'einstein', 'location': 'princeton',},
         'mcurie': {'first': 'marie', 'last': 'curie', 'location': 'paris',},
         }

for username, user_info in users.items(): 
	print('\nUsername: ' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']

	print('\tFull name: ' + full_name.title())
	print('\tLocation: ' + location.title())


