#!/usr/bin/env python3

import pyglet
import numpy
import sys

WIDTH = 800
HEIGHT = 800
CELL_SIZE = 10
SPEED = 0.5

window = pyglet.window.Window(WIDTH, HEIGHT)


class Game:
    def __init__(self, size_x, size_y, speed, init=None):
        self.speed = speed

        if init is None:
            self.state = numpy.zeros((size_x, size_y), dtype='bool')
        elif init == 'random':
            self.state = numpy.random.choice([False, True],
                                             size=(size_x, size_y))

    def toogle_state(self, cell):
        self.state[cell] = not self.state[cell]


def draw_square(x, y, size):
    pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                         ('v2f', [x, y, x+size, y, x+size, y+size, x, y+size]))


@window.event
def on_draw():
    window.clear()

    for ri, row in enumerate(game.state):
        for ci, cell in enumerate(row):
            if cell:
                draw_square(ri*CELL_SIZE, ci*CELL_SIZE, CELL_SIZE)


@window.event
def on_mouse_press(x, y, button, modifiers):
    cell = x // CELL_SIZE, y // CELL_SIZE
    game.toogle_state(cell)


if __name__ == "__main__":
    init = None
    if len(sys.argv) > 1 and sys.argv[1] == 'random':
        init = 'random'

    game = Game(WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE, SPEED, init=init)
    pyglet.app.run()
