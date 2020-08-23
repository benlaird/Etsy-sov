import matplotlib.pyplot as plt
import numpy as np


class SketchBuilder:

    def __init__(self, line, figure, ax):
        self.lines = [line]
        self.curr_line = line
        self.figure = figure
        self.ax = ax
        self.xs = [] # list(line.get_xdata())
        self.ys = [] # list(line.get_ydata())
        self.draw = False
        self.cidpress = line.figure.canvas.mpl_connect('button_press_event', self.on_click)
        # self.cidrelease = line.figure.canvas.mpl_connect('button_release_event',  self.on_click)
        self.cidmotion = line.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.x0 = 0
        self.y0 = 0

    # We only have to draw the last line
    def render_lines(self):
        line = self.lines[len(self.lines)-1]

        ax.plot(line.get_xdata(), line.get_ydata(), color='black', linewidth=1)
        # for line in self.lines:
        # line.figure.canvas.draw()
        fig.canvas.draw()


    def on_click(self, event):
        # print('mouse down', event)
        self.draw = not self.draw
        if self.draw:
            self.x0 = event.xdata
            self.y0 = event.ydata
            x_values = [self.x0]
            y_values = [self.y0]
            self.xs.extend(x_values)
            self.ys.extend(y_values)
        else:
            self.curr_line, = ax.plot([0], [0])  # empty line
            self.xs = []
            self.ys = []
            self.lines.append(line)

    def on_motion(self, event):
        # print('motion event', event)
        if self.draw:
            x_values = [self.x0, event.xdata]
            y_values = [self.y0, event.ydata]
            self.xs.extend(x_values)
            self.ys.extend(y_values)
            line.set_data(self.xs, self.ys)
            self.render_lines()
        self.x0 = event.xdata
        self.y0 = event.ydata

    # Not currently used
    def button_release(self, event):
        self.draw = False
        self.curr_line, = ax.plot([0], [0])  # empty line
        self.xs = []
        self.ys = []
        self.lines.append(line)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Lamp Sketch')
line, = ax.plot([0], [0])  # empty line
ax.set_autoscaley_on(False)
ax.set_autoscalex_on(False)
linebuilder = SketchBuilder(line, fig, ax)

plt.show()
