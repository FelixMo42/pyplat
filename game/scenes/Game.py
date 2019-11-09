import pyglet
import socket
import select
import random
import json

from game.scenes.Scene import Scene
from game.sprites.Player import Player
from game.sprites.Enemy import Enemy
from game.sprites.Platform import Platform

class Game(Scene):
    map_width = 2000

    def onStart(self):
        # sprite managment
        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.middleground = pyglet.graphics.OrderedGroup(1)
        self.foreground = pyglet.graphics.OrderedGroup(2)
        self.sprites = []
        self.players = {}

        # create player
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 10000)
        self.connection.connect(self.server_address)
        self.player = Player(id=self.recv(), world=self, x=5, y=300)

        # generate map
        self.generateMap(10)

    def onDraw(self):
        self.batch.draw()

        pyglet.gl.glTranslatef(self.map_width, 0, 0)
        self.batch.draw()

        pyglet.gl.glTranslatef(-2 * self.map_width, 0, 0)
        self.batch.draw()

    def onUpdate(self, dt):
        for sprite in self.sprites:
            sprite.onUpdate(dt)

        self.player.update(dt)

        readable, _, _  = select.select([self.connection], [], [], 0)
        if readable:
            for update in self.recv().split("\n"):
                update = json.loads(update)
                print(update)
                if update["id"] not in self.players:
                    self.players[update["id"]] = Player(world=self, id=update["id"])
                for key in update:
                    setattr(self.players[update["id"]], key, update[key])
    
    #

    def generateMap(self, seed):
        random.seed(seed)

        for _ in range(3):
            Enemy(world=self, x=random.randint(10, self.map_width-100),y=600)

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

    def recv(self):
        data = ""
        while True:
            data += self.connection.recv(1024).decode()
            if "\n" in data:
                break
        return str(data)[:-1]