from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk




#keep making new walks as long as the program is active
while True:
	rw = RandomWalk(100_000)
	rw.fill_walk()

	#visualize
	data = [Scatter(x=rw.x_values, y=rw.y_values)]
	x_axis_config = {'title': 'Horizontal Movement'}
	y_axis_config = {'title': 'Vertical Movement'}
	my_layout = Layout(title = 'Random Walk Generation',
		xaxis=x_axis_config, yaxis = y_axis_config)
	offline.plot({'data': data, 'layout': my_layout}, filename='random_walk_plotly.html')
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break