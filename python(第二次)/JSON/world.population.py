import json
import pygal.maps.world

from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)


# 打印每个国家 2010 年的人口数量
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code = get_country_code(country_name)
		if code:
			if population < 10000000:
				cc_pops_1[code] = population
			elif population < 1000000000:
				cc_pops_2[code] = population
			else:
				cc_pops_3[code] = population
		# else:
		# 	print('Error - ' + country_name)

# wm = pygal.maps.world.World()

# wm_style = RotateStyle('#336699')
# 加亮地图的颜色，包括背景色，标签以及各个国家的颜色
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)

wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')

