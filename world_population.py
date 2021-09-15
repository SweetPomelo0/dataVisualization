import json
import pygal
from country_codes import get_country_code
import pygal_maps_world.maps

# 将数据都加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # 消除不能直接将小数的字符串转换为整数的错误
        population = int(float(pop_dict['Value']))
        # 国别码
        code = get_country_code(country_name)
        if code:
            # print(country_name + ' : ' + str(population))
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

wm = pygal_maps_world.maps.World()
wm.title = "World Population in 2010, by Country"
wm.add('2010',cc_populations)

wm.render_to_file('world_population.svg')
