import matplotlib.pyplot as plt 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues) 
#s is size of the dots plotted
#for rgb, use values between 0 and 1, the smaller the value, the darker it is

#set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#set the range for each axis
ax.axis([0, 1100, 0, 1100000]) #([x min, x max, y min, y max])
#plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()