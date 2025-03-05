import GameObject

class Scene:
    def __init__(self, name):
        self.name = name
        self.game_objects = []

    def create_game_object(self, name):
        object = GameObject.GameObject(name)
        self.game_objects.append(object)
        return object

        

    def list_available_alements(self, name):
        return list(self.elements.values())


    def is_available():
        return True


    def is_gameObject():
        return
