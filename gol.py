#!/usr/bin/env python3

import pyglet
from pyglet.window import key, Window
import numpy
import sys

WIDTH = 800
HEIGHT = 800
CELL_SIZE = 10
SPEED = 0.5

window = Window(WIDTH, HEIGHT)


class Game:
    def __init__(self, size_x, size_y, speed, init=None):
        self.speed = speed
        self.running = False

        if init is None:
            self.state = numpy.zeros((size_x, size_y), dtype='bool')
        elif init == 'random':
            self.state = numpy.random.choice([False, True],
                                             size=(size_x, size_y))

    def toogle_state(self, cell):
        self.state[cell] = not self.state[cell]

    def alive_neighbors_count(self, ri, ci):
        result = 0

        x_max, y_max = self.state.shape

        for x_move in (1, 0, -1):
            for y_move in (1, 0, -1):
                if x_move == y_move == 0:
                    continue
                x_neigh = ri + x_move if ri + x_move < x_max else 0
                y_neigh = ci + y_move if ci + y_move < y_max else 0

                result += int(self.state[x_neigh, y_neigh])

        return result

    def next_generation(self, dt):
        print("Generating next generation: ", end='')
        underpop, overpop, stay, reprod = 0, 0, 0, 0

        next_generation = numpy.zeros_like(self.state, dtype=bool)

        for ri, row in enumerate(game.state):
            for ci, cell in enumerate(row):
                alive_neighbors = self.alive_neighbors_count(ri, ci)
                if cell and alive_neighbors < 2:
                    next_generation[ri, ci] = False
                    underpop += 1
                # This is here only for documentation purpose because it
                # does not change cell state
                elif cell and alive_neighbors in (2, 3):
                    next_generation[ri, ci] = cell
                    stay += 1
                elif cell and alive_neighbors > 3:
                    next_generation[ri, ci] = False
                    overpop += 1
                elif not cell and alive_neighbors == 3:
                    next_generation[ri, ci] = True
                    reprod += 1

        self.state = next_generation

        print(f'UnderPopulation: {underpop}, OverPopulation: {overpop}',
              f'Staied alive: {stay}, Reborn {reprod}')


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


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        if game.running:
            pyglet.clock.schedule_interval(game.next_generation, SPEED)
        else:
            pyglet.clock.unschedule(game.next_generation)
        game.running = not game.running
    if symbol == key.RIGHT:
        game.running = False
        game.next_generation(None)


if __name__ == "__main__":
    init = None
    if len(sys.argv) > 1 and sys.argv[1] == 'random':
        init = 'random'

    game = Game(WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE, SPEED, init=init)
    pyglet.app.run()
