import pyglet

from game.Sprite import Sprite

class Enemy(Sprite):
    speed = 100
    direction = 1

    def onUpdate(self, dt):
        x = self.direction * self.speed * dt
        #ogx = self.x

        for sprite in self.world.sprites:
            if sprite == self:
                continue
            if self.direction == 1:
                if self.x + self.width  < sprite.x + sprite.width and sprite.x + sprite.width < self.x + self.width +x:
                    self.direction = -1
                    x = sprite.x + sprite.width - self.width - self.x
            if self.direction == -1:
                if sprite.x < self.x and sprite.x > self.x + x:
                    self.direction = 1
                    x = sprite.x - self.x

        self.move(x, 0)
         
        super().onUpdate(dt)
