import GameObject as game_object
import InteractionType as interaction_type
import Scene as scene

class Game:
    
    def __init__(self):
        self.current_scene = None
        pass

    def set_current_scene(self, scene):
        self.current_scene = scene
        pass

    def select_object(self, game_object):
        
        pass

    def select_interaction(self, interaction_type):
        pass

    def set_interaction_options(self, the_options):
        pass

    def start_interaction(self):
        pass
