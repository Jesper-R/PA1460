class Scene:
    def __init__(self, name):
        self.name = name
        self.elements = {}

    def add_element(self, element):
        self.elements[element.name] = element

    def list_available_alements(self, name):
        return list(self.elements.values())


    def is_available():
        return True


    def is_gameObject():
        return
