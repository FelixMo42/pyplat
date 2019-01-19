import pyglet

from game.Sprite import Sprite

class Player(Sprite):
    speed = 300
    jump = (9.8 * 50)

    offset = 250

    velX = 200

    grounded = False

    def onUpdate(self, dt):
        #if self.world.keyIsDown[pyglet.window.key.LEFT]:
        #    self.velX -= self.speed * dt
        #elif self.world.keyIsDown[pyglet.window.key.RIGHT]:
        #    self.velX += self.speed * dt
        #elif self.grounded:
        #    self.velX /= 2 #todo: better drag math

        self.velX += 10 * dt

        if self.grounded and self.world.keyIsDown[pyglet.window.key.UP]:
            self.velY += self.jump
            self.grounded = False

        if self.world.keyIsDown[pyglet.window.key.DOWN]:
            self.velY -= 100 * dt

        super().onUpdate(dt)

        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTranslatef(self.offset - self.x - self.width / 2, 0, 0)

    def onCollide(self):
        self.grounded = True

        if self.velX == 0:
            pyglet.app.exit()