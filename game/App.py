import pyglet
import random

from game.Player import Player
from game.Platform import Platform

class App(pyglet.window.Window):
    fps = 60 

    def __init__(self):
        super().__init__(width=1000, height=500, caption="pyplat")

        self.keyIsDown = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyIsDown)

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.middleground = pyglet.graphics.OrderedGroup(1)
        self.foreground = pyglet.graphics.OrderedGroup(2)
        self.sprites = []

        self.player = Player(world=self, x=0, y=150)

        self.pos = 500
        Platform(world=self, x=0, y=0, width=500, height=30)

        pyglet.clock.schedule(self.onUpdate, 1/self.fps)

    def onUpdate(self, dt, ex_dt):
        for sprite in self.sprites:
            sprite.onUpdate(dt)

        if self.width + self.player.x > self.pos:
            width = random.randint(100, 500)
            Platform(world=self, x=self.pos, y=random.randint(30, 250), width=width, height=30)
            self.pos += width + random.randint(0, 100)

    def on_draw(self):
        self.clear()
        self.batch.draw()