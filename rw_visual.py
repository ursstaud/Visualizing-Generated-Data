import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#keep making new walks as long as the program is active
while True:
	rw = RandomWalk(100_000)
	rw.fill_walk()

	#plot the points
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(15,9))
	point_numbers = range(rw.num_points)
	ax.scatter(rw.x_values, rw.y_values, s=1, c=point_numbers, cmap=plt.cm.jet,
		edgecolors='none')

	#emphasize the first and last points
	ax.scatter(0, 0, c='green', edgecolors='none', s=100)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='magenta', edgecolors='none',
		s=100)

	#remove axes
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break