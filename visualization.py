import numpy as np
import matplotlib.pyplot as plt
from point_collection import *

center = (0.0, 0.0)

ring_radii = [
    [1280.0, 2816.0],
    [4352.0, 5888.0],
    [7424.0, 8960.0],
    [10496.0, 12032.0],
    [13568.0, 15104.0],
    [16640.0, 18176.0],
    [19712.0, 21248.0],
    [22784.0, 24320.0]
]

max_radius = ring_radii[-1][1]

def plot_rings():
    for radii in ring_radii:
        theta = np.linspace(0, 2 * np.pi, 50, endpoint = True)
        xs = np.outer(radii, np.cos(theta))
        ys = np.outer(radii, np.sin(theta))

        # Traverse the circle in opposite directions
        xs[1,:] = xs[1,::-1]
        ys[1,:] = ys[1,::-1]

        axes = plt.subplot(111, aspect="equal")
        axes.fill(np.ravel(xs), np.ravel(ys), facecolor="#c181c1", edgecolor="#c181c1")

def display(title):
    # Finish drawing
    plt.axis([-max_radius, max_radius, -max_radius, max_radius])

    plt.title(title)
    plt.show()

def visualize_results(
        first_eye_pos, first_eye_target,
        second_eye_pos, second_eye_target,
        stronghold_location,
):
    # Plot stronghold rings
    plot_rings()

    # Plot points
    point_collection = PointCollection()
    point_collection.add_point("First eye", first_eye_pos)
    point_collection.add_point("First eye target", first_eye_target)

    point_collection.add_point("Second eye", second_eye_pos)
    point_collection.add_point("Second eye target", second_eye_target)

    point_collection.add_point("Stronghold", stronghold_location)

    # Plot line between throw positions and stronghold
    point_collection.add_line(0, 1) # Eye 1 -> Eye 1 target
    point_collection.add_line(2, 3) # Eye 2 -> Eye 2 target

    point_collection.plot()
    
    display("Triangulation visualization")
