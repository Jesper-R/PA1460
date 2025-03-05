class scene:
    def __init__(self, name):
        self.name = name
        self.object = {}


    def findObject(self, name):
        return self.objects.get(name)