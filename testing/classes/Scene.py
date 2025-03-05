import GameObject as game_object

class Scene:
    def __init__(self, name):
        self.name = name
        self.game_objects = []
        self.selected_game_object = None

    def create_game_object(self, name):
        object = game_object.GameObject(name)
        self.game_objects.append(object)
        return object

    def set_selected_object(self, game_object):
        self.selected_game_object = game_object
        available_interactions = self.selected_game_object.get_interaction_types()
        return available_interactions
    
    def select_interaction(self, interaction_type):
        return self.selected_game_object.get_interaction_options(interaction_type)

    def list_available_alements(self, name):
        pass


    def is_available():
        return True


    def is_gameObject():
        return
