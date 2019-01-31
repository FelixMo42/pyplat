import pyglet

from game.Sprite import Sprite

class Player(Sprite):
    speed = 300
    jump = (9.8 * 75) * .75

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

        k = 1

        if self.grounded and self.world.keyIsDown[pyglet.window.key.UP]:
            self.velY = self.jump
            self.grounded = False

            k = .5

        if self.world.keyIsDown[pyglet.window.key.DOWN]:
            #self.velY -= 100 * dt
            k = .5
            

        self.velY -= k * self.velY * dt

        super().onUpdate(dt)

        # set camera
        pyglet.gl.glLoadIdentity()
        pyglet.gl.glTranslatef(self.offset - self.x - self.width / 2, 0, 0)

    def move(self, x, y):
        super().move(x,y)
        self.x = self.x % 1000
        self.y = self.y % 1000
        self.updatePosition()

    def onCollide(self):
        self.grounded = True

        if self.velX == 0:
            pyglet.app.exit()