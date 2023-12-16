import math
import matplotlib.pyplot as plt

class PointCollection:
    def __init__(self):
        self.xs = []
        self.ys = []
        self.line_froms = []
        self.line_tos = []
        self.annotations = []

        self.axes = plt.subplot(111, aspect="equal")

    def add_point_from_components(self, annotation, x, y):
        self.annotations.append(annotation)
        self.xs.append(x)
        self.ys.append(y)

    def add_point(self, annotation, point):
        self.add_point_from_components(annotation, point[0], point[1])

    def add_line(self, from_idx, to_idx):
        from_pt = (self.xs[from_idx], self.ys[from_idx])
        to_pt = (self.xs[to_idx], self.ys[to_idx])

        self.line_froms.append(from_pt)
        self.line_tos.append(to_pt)

    def plot(self):
        # Plot lines
        for i in range(len(self.line_froms)):
            from_pt = self.line_froms[i]
            to_pt = self.line_tos[i]

            # Get normalized direction
            dx = to_pt[0] - from_pt[0]
            dy = to_pt[1] - from_pt[1]

            length = math.sqrt(dx * dx + dy * dy)
            dx /= length
            dy /= length

            # Rescale arrow
            dx *= 50000
            dy *= 50000

            self.axes.arrow(x=from_pt[0], y=from_pt[1], dx=dx, dy=dy, color="#db4420")

        # Plot points
        self.axes.plot(self.xs, self.ys, 'x')

        for i in range(len(self.annotations)):
            annotation = self.annotations[i]
            x = self.xs[i]
            y = self.ys[i]

            # Add annotation text one unit above the point
            self.axes.annotate(annotation, xy = (x, y), xytext = (x, y + 1))
