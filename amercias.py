# import pygal
#
# wm = pygal.Worldmap()

# 创建一个突出北美、中美和南美的简单地图

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'North,Central,and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
