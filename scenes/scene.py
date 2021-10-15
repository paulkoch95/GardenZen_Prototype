class Scene:
    # Basic Class as boilerplate for all scenes
    def __init__(self):
        self.next = self

    def input(self, event):
        pass

    def render(self, screen):
        pass

    def update(self):
        pass

    def switchScene(self, scene):
        self.next = scene