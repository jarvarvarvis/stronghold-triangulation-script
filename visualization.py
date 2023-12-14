import numpy as np
import matplotlib.pyplot as plt

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

def visualize_results(
        first_eye_pos, first_eye_target,
        second_eye_pos, second_eye_target,
        stronghold_location
):
    # Plot stronghold rings
    for radii in ring_radii:
        theta = np.linspace(0, 2 * np.pi, 50, endpoint = True)
        xs = np.outer(radii, np.cos(theta))
        ys = np.outer(radii, np.sin(theta))

        # Traverse the circle in opposite directions
        xs[1,:] = xs[1,::-1]
        ys[1,:] = ys[1,::-1]

        axes = plt.subplot(111, aspect="equal")
        axes.fill(np.ravel(xs), np.ravel(ys), facecolor="#c181c1", edgecolor="#c181c1")

    # Plot points
    xs = [first_eye_pos[0], first_eye_target[0], second_eye_pos[0], second_eye_target[0], stronghold_location[0]]
    ys = [first_eye_pos[1], first_eye_target[1], second_eye_pos[1], second_eye_target[1], stronghold_location[1]]
    annotations = ["First eye", "First eye target", "Second eye", "Second eye target", "Stronghold"]
    axes = plt.subplot(111, aspect="equal")
    axes.plot(xs, ys, 'x')
   
    # Plot line between throw positions
    axes.plot([first_eye_pos[0], second_eye_pos[0]], [first_eye_pos[1], second_eye_pos[1]])
    
    for i in range(len(annotations)):
        annotation = annotations[i]
        x = xs[i]
        y = ys[i]
        axes.annotate(annotation, xy = (x, y), xytext = (x, y + 1))

    # Finish drawing
    max_radius = 24320.0
    plt.axis([-max_radius, max_radius, -max_radius, max_radius])

    plt.title("Triangulation visualization")
    plt.show()
