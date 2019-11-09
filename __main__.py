import pyglet
import sys

from game.App import App

from game.scenes.Game import Game
from game.scenes.Menu import Menu


if __name__ == "__main__":
    scene = sys.argv[1]
    if scene == "game":
        app = App(Game)
    if scene == "menu":
        app = App(Menu)
    pyglet.app.run()