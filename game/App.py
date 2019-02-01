import pyglet
import random

from game.Player import Player
from game.Platform import Platform
from game.Enemy import Enemy

class App(pyglet.window.Window):
    fps = 60

    map_width = 5000

    def __init__(self):
        super().__init__(width=1000, height=500, caption="pyjinja")

        self.keyIsDown = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyIsDown)

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.middleground = pyglet.graphics.OrderedGroup(1)
        self.foreground = pyglet.graphics.OrderedGroup(2)
        self.sprites = []

        for _ in range(3):
            Enemy(world=self, x=random.randint(10, self.map_width-100),y=600)

        self.player = Player(world=self, x=0, y=300)

        pyglet.clock.schedule(self.onUpdate, 1/self.fps)

        x = 0
        while x < self.map_width:
            width = random.randint(100, 500)
            y = random.randint(30, 250)

            width = min(width, self.map_width - x)
            if width < 100:
                break

            if x == 0:
                Platform(world=self, x=x + self.map_width, y=y, width=width, height=30)
            if x + width >= self.map_width:
                Platform(world=self, x=x - self.map_width, y=y, width=width, height=30)

            Platform(world=self, x=x, y=y, width=width, height=30)
            x += width + random.randint(0, 100)

    def onUpdate(self, dt, ex_dt):
        for sprite in self.sprites:
            sprite.onUpdate(dt)

    def on_draw(self):
        self.clear()
        self.batch.draw()

        pyglet.gl.glTranslatef(self.map_width, 0, 0)
        self.batch.draw()

        pyglet.gl.glTranslatef(-2 * self.map_width, 0, 0)
        self.batch.draw()
        