import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation



points = []
colors = []

def add_point(point: [float, float, float]):
    global points, colors
    points.append(point)
    colors.append([1, 0, 0, 1.0])

fig = plt.figure()
ax = p3.Axes3D(fig)

# Initialize a text object
text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes)

# Animation update function
def update(num):
    ax.clear()  # Clear the plot

    # Set the limits of the x, y, and z axes
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])

    points_to_pop = []
    for i in range(len(colors)):
        colors[i][3] -= 0.05
        if colors[i][3] <= 0:
            points_to_pop.append(i)

    # Remove all the points that have faded away.
    for i in sorted(points_to_pop, reverse=True):
        points.pop(i)
        colors.pop(i)

    ##########################################

    # Here's where we can add the PAD vector.

    # For testing, I'm just adding a random point:
    add_point(tuple(np.random.rand(3)))

    ##########################################

    for point, color in zip(points, colors):
        # ax.scatter(data[0, i:i+1], data[1, i:i+1], data[2, i:i+1], color=colors[i])
        ax.scatter(*point, color=color)
    text = ax.text2D(0.05, 0.95, f'Iteration: {num+1}', transform=ax.transAxes)


# Create animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=50)

plt.show()
