import pyglet
import random
import socket
import select
import json

class App(pyglet.window.Window):
    fps = 60

    map_width = 5000

    def __init__(self, scene, width=1000, height=500, caption="pyapp"):
        super().__init__(width=width, height=height, caption=caption)

        self.scene = scene(self)
        self.scene.onStart()

        self.keyIsDown = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.keyIsDown)

        pyglet.clock.schedule(self.onUpdate, 1/self.fps)

    def onUpdate(self, dt, ex_dt):
        self.scene.onUpdate(dt)

    def on_draw(self):
        self.clear()
        self.scene.onDraw()