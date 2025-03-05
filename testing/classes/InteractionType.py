class InteractionType:
    def __init__(self):
        self.options = {}

    def get_specific_options(self):
        pass

    def apply_options(self, options):
        pass

class PickUpInteraction(InteractionType):
    def __init__(self):

        self.options = {"amount": 0}

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options
    
    def apply_options(self, options):
        self.options = options
        return self.options
    
class OpenInteraction(InteractionType):
    def __init__(self):
        self.options = {}

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options
    
    def apply_options(self, options):
        self.options = options
        return self.options
    
class LookInteraction(InteractionType):
    def __init__(self):
        self.options = {}

    def execute(self, something):
        #implement
        pass

    def get_specific_options(self):
        return self.options
    
    def apply_options(self, options):
        self.options = options
        return self.options