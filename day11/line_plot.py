import matplotlib.pyplot as plt

# x values
x = [1, 2, 3, 4, 5]

# y values
y = [10, 20, 30, 40, 50]

# create line plot
plt.plot(x, y)

# add title and labels
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Line Plot Example")

# show the plot
plt.show()