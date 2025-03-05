class InteractionType:
    def __init__(self):
        self.options = []
        pass

    def execute(self, something):
        pass

    def get_specific_options(self):
        pass

class PickUpInteraction(InteractionType):
    def __init__(self):
        self.options = ["amount"]

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options
    
class OpenInteraction(InteractionType):
    def __init__(self):
        self.options = ["insert key"]

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options
    
class LookInteraction(InteractionType):
    def __init__(self):
        self.options = ["option1"]

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options