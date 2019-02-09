class Scene:
    def __init__(self, app):
        self.app = app

    def onStart(self):
        pass

    def onEnd(self):
        pass
    
    def onDraw(self):
        pass

    def onUpdate(self, dt):
        pass

    #

    def __getattr__(self, name):
        return getattr(self.app, name)