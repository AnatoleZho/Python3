import requests

import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 使用 Web API

# 1.处理 api 响应

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

print('Status code: ', r.status_code)

response_dict = r.json()

print(response_dict.keys())



# 2. 处理 api 响应字典

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('Repositories returned: ', len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]
print('\nKeys: ', len(repo_dict))
for key in repo_dict.keys():
    print(key)



# 3. 使用 Pygal 可视化仓库

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#336699', base_style=LCS)
'''
# 使用Bar() 创建一个简单的条形图，并向它传递了my_style (见❹)。我们还传递了另外两个样式实参:
# 让标签绕x 轴旋转45度 (x_label_rotation=45 )，并隐藏了图例(show_legend=False )，
# 因为我们只在图表中绘制一个数据系列。
'''
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)

chart.render_to_file('python_repos.svg')


# 4. 改进 Pygal 图表

my_style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
# 设置了图表标题、副标签和主标签的字体大小
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# 将较长的项目名缩短为15字符
my_config.truncate_label = 15
# 隐藏图表中的水平线
my_config.show_y_guides = False
# 设置自定义宽度，让图表充分利用浏览器中可用空间
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)

chart.render_to_file('python_repos.svg')


# 5. 添加自定义工具提示
'''在 Python 中，将鼠标指向条形将显示它表示的信息，通常称为工具提示。'''
'''

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [{'value': 16101, 'label': 'Description of httpie.'},
              {'value': 15028, 'label': 'Description of django.'},
              {'value': 14798, 'label': 'Description of flask.'},
              ]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

'''


# 6. 根据数据绘图


chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'


names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    '''在图表中添加可单击的链接, 添加链接是要去掉 label'''
    plot_dict = {'value': repo_dict['stargazers_count'],
                  # 'label': repo_dict['description'],
                 'xlink': repo_dict['html_url'],
                 }

    plot_dicts.append(plot_dict)

chart.x_labels = names


chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')








