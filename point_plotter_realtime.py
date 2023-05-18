"""
This script can plot points in 3D space in real time. Calling the add_point() function will plot a point immediately.
"""

import matplotlib.pyplot as plt



points_to_plot = [[1.948137, 0.9972930000000002, -0.05955500000000019], [2.2376240000000003, 1.264372, -0.12164800000000009], [2.373046, 1.1762159999999997, 0.06062600000000007], [2.1845909999999997, 0.8373990000000001, 0.150887], [2.087204, 1.3627760000000002, -0.23255999999999988], [2.431711, 1.0799649999999996, 0.10072300000000012], [2.030116, 0.9672160000000002, 0.05712999999999996], [1.977957, 1.007871, -0.03491899999999992], [2.095288, 1.1944000000000004, -0.116402], [1.998874, 0.7859499999999999, 0.16938000000000009], [1.6352799999999998, 0.9415619999999999, -0.06430999999999992], [1.941618, 0.920706, -0.028326000000000073], [1.7703799999999998, 0.9831240000000001, -0.03151400000000004], [1.708796, 0.6876339999999999, 0.15546800000000005], [1.691228, 0.9677499999999999, -0.147916], [1.9530569999999998, 0.9671010000000001, 0.00371100000000002], [0.623966, 0.32071400000000005, 0.03900799999999999], [0.709324, 0.271142, 0.018186000000000008], [0.7403109999999999, 0.542987, -0.132155], [0.880274, 0.31705, 0.134898], [0.7462539999999999, 0.338572, 0.0010060000000000069], [0.886686, 0.509694, -0.08882399999999999], [0.962987, 0.5719190000000001, 0.0031969999999999776], [0.921448, 0.22559600000000002, 0.14554600000000004], [0.7907, 0.5858920000000001, -0.16785400000000003], [1.0141910000000003, 0.494055, 0.040708999999999995], [0.804905, 0.307181, 0.08017099999999996], [0.700415, 0.358885, -0.039825]]

# Calculate the scales based on the points in the list
x_scale = [min([point[0] for point in points_to_plot]), max([point[0] for point in points_to_plot])]
y_scale = [min([point[1] for point in points_to_plot]), max([point[1] for point in points_to_plot])]
z_scale = [min([point[2] for point in points_to_plot]), max([point[2] for point in points_to_plot])]


######################################################


# Create a new 3D plot
fig = plt.figure()
ax = plt.subplot(projection="3d")

# Keep the plot open
plt.ion()
plt.show()

# Set the limits of the x, y, and z axes
ax.set_xlim(x_scale)
ax.set_ylim(y_scale)
ax.set_zlim(z_scale)

# List to hold the point objects
point_objects = []

def add_point(point: [float, float, float]):
    point_object = ax.scatter(*point, color=[1, 0, 0, 1], edgecolor=[0, 0, 0, 0])
    point_objects.append(point_object)
    plt.draw()



if __name__ == "__main__":
    while len(points_to_plot) > 0 or len(point_objects) > 0:
        points_to_pop = []
        for i in range(len(point_objects)):
            color = point_objects[i].get_facecolor()[0]
            color[3] -= 0.05
            if color[3] <= 0:
                points_to_pop.append(i)
            else:
                point_objects[i].set_facecolor(color)

        # Remove all the points that have faded away.
        for i in sorted(points_to_pop, reverse=True):  # We pop the indices from highest to lowest.
            point_objects[i].remove()
            point_objects.pop(i)

        if points_to_plot:
            add_point(points_to_plot[0])
            points_to_plot.pop(0)

        plt.pause(0.1)


    plt.ioff()
    # plt.show()  # Keep the plot open until the user closes it

