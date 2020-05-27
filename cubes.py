import matplotlib.pyplot as plt 

x_values = range(0,5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.set_title("Cubed Values up to 5000", fontsize=20)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubed Values", fontsize=14)
ax.scatter(x_values, y_values, s = 5, c=y_values, cmap=plt.cm.nipy_spectral)

plt.show()
