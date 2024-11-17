import matplotlib.pyplot as plt

x_coords1 = [1, 1, 0, -1, -1, -1, 0, 1]
y_coords1 = [0, 1, 1, 1, 0, -1, -1, -1]
x_coords2 = [2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0, 1, 2, 2, 2]
y_coords2 = [0, 1, 2, 2, 2, 2, 2, 1, 0, -1, -2, -2, -2, -2, -2, -1, 0]

# Plot the first set
plt.scatter(x_coords1, y_coords1, color='blue')

# Plot the second set
plt.scatter(x_coords2, y_coords2, color='red')

# Set the x and y axis ticks to be at intervals of 1
plt.xticks(range(min(x_coords1 + x_coords2), max(x_coords1 + x_coords2) + 1, 1))
plt.yticks(range(min(y_coords1 + y_coords2), max(y_coords1 + y_coords2) + 1, 1))

# Add labels and title
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Multiple Sets of Coordinates with Axis Intervals of 1')

# Show legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()  