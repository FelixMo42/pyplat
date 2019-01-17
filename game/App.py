import pyglet
from game.Sprite import Sprite

class App(pyglet.window.Window):
    fps = 60 

    def __init__(self):
        super().__init__(width=500, height=500, caption="pyplat")

        self.keyIsDown = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyIsDown)

        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.middleground = pyglet.graphics.OrderedGroup(1)
        self.foreground = pyglet.graphics.OrderedGroup(2)
        self.sprites = []

        Sprite(world=self)

        pyglet.clock.schedule(self.onUpdate, 1/self.fps)

    def onUpdate(self, dt, ex_dt):
        for sprite in self.sprites:
            sprite.onUpdate(dt)

    def on_draw(self):
        self.clear()
        self.batch.draw()