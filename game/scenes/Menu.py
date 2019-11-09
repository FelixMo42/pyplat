import pyglet

from game.scenes.Scene import Scene


class Menu(Scene):
    def __init__(self, *a, **b):
        super().__init__(*a, **b)

        
        self.image = pyglet.resource.image('resources/startButton.png').get_texture()
        self.image.scale = 10
        #self.seq = pyglet.image.ImageGrid(image, 2, 1)
        ##self.seq.scale = 100

        self.image.width = 32 * self.image.scale
        self.image.height = 32 * self.image.scale
        self.image.texture.width = 32 * self.image.scale
        self.image.texture.height = 32 * self.image.scale

    def onDraw(self):
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
        self.image.get_region(0,0,32,32).blit(0,0)