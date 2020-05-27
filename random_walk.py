from random import choice

class RandomWalk:
	"""a class to generate random walks"""

	def __init__(self, num_points = 5000):
		"""initialize attributes of a walk"""
		self.num_points = num_points

		#all walks start at (0,0)
		self.x_values = [0]
		self.y_values = [0]


	def fill_walk(self):
		"""calculate all the points in a walk"""
		#keep taking steps until the walk reaches the desired length
		while len(self.x_values) < self.num_points:

			#decide which direction to go and how far to go in that direction
			x_step = self.get_step()
			y_step = self.get_step()

			#reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			#calculate the new position
			x = self.x_values[-1] + x_step 
			#takes the last value from the list
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)


	def get_step(self):
		"""method to generate the step"""
		direction = choice([1, -1])
		distance = choice([0, 1, 2, 3, 4])
		step = int(direction * distance)
		return step

		