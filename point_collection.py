import matplotlib.pyplot as plt

class PointCollection:
    def __init__(self):
        self.xs = []
        self.ys = []
        self.line_xs = []
        self.line_ys = []
        self.annotations = []

        self.axes = plt.subplot(111, aspect="equal")

    def add_point_from_components(self, annotation, x, y):
        self.annotations.append(annotation)
        self.xs.append(x)
        self.ys.append(y)

    def add_point(self, annotation, point):
        self.add_point_from_components(annotation, point[0], point[1])

    def add_line(self, from_idx, to_idx):
        self.line_xs.append(self.xs[from_idx])
        self.line_xs.append(self.xs[to_idx])

        self.line_ys.append(self.ys[from_idx])
        self.line_ys.append(self.ys[to_idx])

    def plot(self):
        # Plot lines
        self.axes.plot(self.line_xs, self.line_ys)

        # Plot points
        self.axes.plot(self.xs, self.ys, 'x')

        for i in range(len(self.annotations)):
            annotation = self.annotations[i]
            x = self.xs[i]
            y = self.ys[i]

            # Add annotation text one unit above the point
            self.axes.annotate(annotation, xy = (x, y), xytext = (x, y + 1))
