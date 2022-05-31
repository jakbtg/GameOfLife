# This is the implementation of the Conway's Game of Life.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class GameOfLife:
    width = 100
    height = 100

    def __init__(self, random_state=False):
        self.grid = np.zeros((self.height, self.width))
        if random_state:
            self.grid = np.random.randint(2, size=(self.height, self.width))
        self.grid_next = np.zeros((self.height, self.width))
        self.fig = plt.figure()

        self.im = plt.imshow(
            self.grid, interpolation='nearest', animated=True, cmap='Greys')
        self.ani = animation.FuncAnimation(
            self.fig, self.update, interval=50, blit=True, frames=1000, repeat=False)
        plt.title('Game of Life')
        self.fig.axes[0].get_xaxis().set_visible(False)
        self.fig.axes[0].get_yaxis().set_visible(False)

        plt.show()

        # self.ax = self.fig.add_subplot(1, 1, 1)
        # self.ax.set_xlim(0, self.width)
        # self.ax.set_ylim(0, self.height)
        # self.ax.set_aspect('equal')
        # self.ax.set_title('Game of Life')
        # self.im = self.ax.imshow(self.grid, interpolation='nearest', cmap='Greys')
        # self.anim = animation.FuncAnimation(self.fig, self.update, interval=100, blit=True)

    def update(self, i):
        self.grid_next = self.grid.copy()
        for x in range(self.width):
            for y in range(self.height):
                self.grid_next[y, x] = self.update_cell(x, y)
        self.grid = self.grid_next.copy()
        self.im.set_data(self.grid)
        return self.im,

    def update_cell(self, x, y):
        n = self.count_neighbors(x, y)
        if self.grid[y, x] == 1:
            if n < 2 or n > 3:
                return 0
            else:
                return 1
        else:
            if n == 3:
                return 1
            else:
                return 0

    def count_neighbors(self, x, y):
        n = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                rowNeighbor = (y + i + self.height) % self.height
                colNeighbor = (x + j + self.width) % self.width
                n += self.grid[rowNeighbor, colNeighbor]
        return n


# Main
if __name__ == '__main__':
    game = GameOfLife(random_state=True)
    # game.save('game_of_life.gif')
    # game.clear()
