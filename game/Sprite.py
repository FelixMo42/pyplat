import pyglet

class Sprite(pyglet.sprite.Sprite):
    mass = 1
    speed = 500

    color = (100,100,100,100)

    scale = 1

    def __init__(self, world, x=0, y=0, width=100, height=100):
        image = pyglet.image.create(
            width=width, height=height, 
            pattern=pyglet.image.SolidColorImagePattern(self.color)
        )
        super().__init__(img=image, batch=world.batch, group=world.foreground)
        world.sprites += [self]

        self.world = world
        self.xPos = x
        self.yPos = y

    def onUpdate(self, dt):
        if self.world.keyIsDown[pyglet.window.key.UP]:
            self.yPos += self.speed * dt
        if self.world.keyIsDown[pyglet.window.key.DOWN]:
            self.yPos -= self.speed * dt
        if self.world.keyIsDown[pyglet.window.key.LEFT]:
            self.xPos -= self.speed * dt
        if self.world.keyIsDown[pyglet.window.key.RIGHT]:
            self.xPos += self.speed * dt

        self.position = (
            int(self.xPos / self.scale) * self.scale,
            int(self.yPos / self.scale) * self.scale
        )
