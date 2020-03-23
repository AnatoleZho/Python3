import json
import pygal.maps.world
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

'''制作世界人口地图：JSON格式'''

# 1 提取相关数据
'''
filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

    for pop_dic in pop_data:
        if pop_dic['Year'] == '2010':
            country_name = pop_dic['Country Name']
            population = int(float(pop_dic['Value']))
            print(country_name + ': ' + str(population))

'''


# 2. 获取两个字母的国别码
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

'''
filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

    for pop_dic in pop_data:
        if pop_dic['Year'] == '2010':
            country_name = pop_dic['Country Name']
            population = int(float(pop_dic['Value']))
            code = get_country_code(country_name)

            if code:
                print(code + ': ' + str(population))
            else:
                print('Error -' + country_name)

'''



# 3. 制作世界地图

'''
wm = pygal.maps.world.World()

wm.title = 'North, Central, and south America'
'''
# 使用了方法add() ，它接受一个标签和一个列表，其中后者包含我们要突出的国家 的国别码。
# 每次调用add() 都将为指定的国家选择一种新颜色，并在图表左边显示该颜色和指定的标签
'''
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf','gy', 'pe',
                         'py', 'sr', 'uy', 've'])
wm.render_to_file('americas.svg')
'''


# 4. 在世界地图上呈现数字数据

'''
wm = pygal.maps.world.World()

wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 3412600, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
'''


# 5. 绘制完整的世界人口地图

'''
filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country)

            if code:
                cc_populations[code] = population

wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010',cc_populations)

wm.render_to_file('world_population.svg')
'''


# 6. 根据人口数量将国家分组
filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

    cc_populations = {}
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country)

            if code:
                cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop


print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

'''
wm = pygal.maps.world.World()
wm.title = 'World Population in 2010, by Country'

wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('level_world_population.svg')
'''


# 7. 使用 Pygal 设置地图的样式
'''
wm_style = RotateStyle('#336699')

wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('level_world_population.svg')

'''



# 8. 加亮颜色主题
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('level_world_population.svg')

