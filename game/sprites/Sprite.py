import pyglet

class Sprite:
    mass = 1
    speed = 500

    velX = 0
    velY = 0

    color = (100,100,100,100)
    scale = 1
    gravity = 9.8 * 75
    static = False

    def __init__(self, world, x=0, y=0, width=60, height=60):
        image = pyglet.image.create(
            width=width, height=height, 
            pattern=pyglet.image.SolidColorImagePattern(self.color)
        )
        self.sprite = pyglet.sprite.Sprite(img=image, batch=world.batch, group=world.middleground)
        world.sprites += [self]

        self.x = x
        self.y = y
        self.sprite.position = (x, y)

        self.width = width
        self.height = height

        self.world = world

    def move(self, x, y):
        for sprite in self.world.sprites:
            if sprite == self:
                continue
            if self.x + self.width >= sprite.x and self.x <= sprite.x + sprite.width:
                if y > 0:
                    if self.y + self.height <= sprite.y and self.y + self.height + y >= sprite.y:
                        y = sprite.y - (self.y + self.height)
                        self.velY = 0
                        self.onCollide()
                if y < 0:
                    if self.y >= sprite.y + sprite.height and self.y + y <= sprite.y + sprite.height:
                        y = (sprite.y + sprite.height) - self.y
                        self.velY = 0
                        self.onCollide()
            if self.y + self.height >= sprite.y and self.y <= sprite.y + sprite.height:
                if x > 0:
                    if self.x + self.width <= sprite.x and self.x + self.width + x >= sprite.x:
                        x = sprite.x - (self.x + self.width)
                        self.velX = 0
                        self.onCollide()
                if x < 0:
                    if self.x >= sprite.x + sprite.width and self.x + x <= sprite.x + sprite.width:
                        x = (sprite.x + sprite.width) - self.x
                        self.velX = 0
                        self.onCollide()

        self.x = self.x + x
        self.y = self.y + y

        self.updatePosition()

    def updatePosition(self):
        self.sprite.position = (
            int(self.x),
            int(self.y)
        )

    def onCollide(self):
        pass

    def onUpdate(self, dt):
        if not self.static:
            self.move(
                self.velX * dt,
                self.velY * dt
            )

            self.velX -= 0
            self.velY -= self.gravity * dt