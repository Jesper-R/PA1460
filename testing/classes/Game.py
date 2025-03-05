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
        return self.current_scene.set_selected_object(game_object)


    def select_interaction(self, interaction_type):
        return self.current_scene.select_interaction(interaction_type)

    def set_interaction_options(self, the_options):
        return self.current_scene.set_interaction_options(the_options)

    def start_interaction(self):
        return self.current_scene.start_interaction()
