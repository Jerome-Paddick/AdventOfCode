import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def read_input():
    folds = []
    lines = []
    data = True
    with open('input.txt') as f:
        while line := f.readline():
            if len(line.strip()) == 0:
                data = False
            elif data:
                lines.append([int(num) for num in line.strip().split(',')])
            else:
                folds.append((int(x) if x.isnumeric() else x for x in line.replace('fold along', '').strip().split('=')))

    return np.array(lines), folds


def part_1():
    lines, folds = read_input()

    x = lines[:, 0]
    y = lines[:, 1]

    for axis, fold in folds:
        if axis == 'x':
            x[x > fold] = 2*fold - x[x > fold]

        else:
            y[y > fold] = 2*fold - y[y > fold]

    print(len(np.unique(lines, axis=0)))


def part_2():
    global x, y, i

    lines, folds = read_input()

    x = lines[:, 0]
    y = lines[:, 1]

    stages = [lines.copy()]

    for axis, fold in folds:
        if axis == 'x':
            x[x > fold] = 2*fold - x[x > fold]
        else:
            y[y > fold] = 2*fold - y[y > fold]
        stages.append(lines.copy())

    # print(stages)

    class AnimatedScatter(object):
        """An animated scatter plot using matplotlib.animations.FuncAnimation."""

        def __init__(self, stages, numpoints=50):
            self.numpoints = stages[0].shape[0]
            self.stream = self.data_stream()
            self.stages = stages
            # Setup the figure and axes...
            self.fig, self.ax = plt.subplots()
            # Then setup FuncAnimation.
            self.ani = animation.FuncAnimation(self.fig, self.update, frames=len(stages), interval=500,
                                               init_func=self.setup_plot, blit=True)

        def setup_plot(self):
            """Initial drawing of the scatter plot."""
            x, y, s, c = next(self.stream).T
            self.scat = self.ax.scatter(x, y, c=c, s=s, vmin=0, vmax=1,
                                        cmap="jet", edgecolor="k")
            self.ax.axis([-10, 10, -10, 10])
            # For FuncAnimation's sake, we need to return the artist we'll be using
            # Note that it expects a sequence of artists, thus the trailing comma.
            return self.scat,

        def data_stream(self):
            """Generate a random walk (brownian motion). Data is scaled to produce
            a soft "flickering" effect."""
            xy = (np.random.random((self.numpoints, 2)) - 0.5) * 10
            for item in self.stages[0]:
                print(item)
            for item in xy:
                print(item)
            i = 0
            xy = self.stages[-1]
            s, c = np.ones((self.numpoints, 2)).T

            print(self.stages[0].shape)
            print(xy.shape)
            print(s.shape)
            print(c.shape)

            curr = 0

            while True:
                if i < len(self.stages) - 1:
                    i += 1

                xy = self.stages[i]
                x = xy[:, 0]
                y = xy[:, 1]

                self.ax.axis([np.min(x) - 10, 2*np.max(x), np.min(y) - 10, 2*np.max(y)])
                # xy += 0.03 * (np.random.random((self.numpoints, 2)) - 0.5)
                # s += 0.05 * (np.random.random(self.numpoints) - 0.5)
                # c += 0.02 * (np.random.random(self.numpoints) - 0.5)
                yield np.c_[xy[:, 0], xy[:, 1], s, c]

        def update(self, i):
            """Update the scatter plot."""
            data = next(self.stream)

            # Set x and y data...
            self.scat.set_offsets(data[:, :2])
            # Set sizes...
            self.scat.set_sizes(abs(data[:, 2]))
            # Set colors..
            self.scat.set_array(data[:, 3])

            # We need to return the updated artist for FuncAnimation to draw..
            # Note that it expects a sequence of artists, thus the trailing comma.
            return self.scat,

    a = AnimatedScatter(stages)
    plt.show()

# part_1()
part_2()
