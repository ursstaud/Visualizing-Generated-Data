import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
	rw = RandomWalk(5000)
	rw.fill_walk()

	#plot the points
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9))
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
	
	ax.scatter(0, 0, c='green', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='magenta', edgecolors='none',
		s=100)

	#remove axes
	ax.get_xaxis().set_visible(True)
	ax.get_yaxis().set_visible(True)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break