# Game of Life

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
implemented in Python &amp; pyglet.

## Instalation

You will need Python >= 3.6, numpy and pyglet to run the game. Numpy and pyglet
can be installed via `pip install -r requirements.txt`.

## Run

You can run the game in three ways:

1. `python3 gol.py` with all cells dead
2. `python3 gol.py random` with random initial state
3. `python3 gol.py file examples/lines.npy` with initial state loaded from the file

## Controls

By clicking into the game, you can toggle cell state. You can also
use your keyboard:

* `right arrow` moves you to a next generation
* `space` start/stop
* `up arrow` speed up
* `down arrow` slow down
* `s` save current state to file

## License

MIT
