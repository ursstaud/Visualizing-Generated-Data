import matplotlib.pyplot as plt
from die import Die

#create a D6
die_1 = Die()
die_2 = Die()

#make some rolls and store the results in a list
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1): 
#adding 1 in this case so we can make sure it counts 6
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)

#visualize the results
x_values = list(range(2, max_result + 1))


plt.bar(x_values, frequencies, color='pink' )
plt.xlabel('Range')
plt.ylabel('Frequency of Range')
plt.title('Frequency of Adding the outcome of throwing 2 D6 die 1000 times', color ='blue')
plt.show()