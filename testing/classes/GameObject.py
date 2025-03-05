import InteractionType as interaction_type
class GameObject:
    def __init__(self, name):
        self.name = name
        self.interaction_types = ["pick up", "look at", "use"]
        self.current_interaction = "None"
        self.state = 1

    def get_interaction_types(self):
        return self.interaction_types

    def start_interaction(self, the_interaction_type):
        for interaction in self.interaction_types:
            if the_interaction_type == interaction:
                return f"You ${the_interaction_type} the ${self.name}."
            else:
                return "Interaction not available."

    def get_interaction_options(self, interaction_type: interaction_type):
        self.current_interaction = interaction_type

        return interaction_type.get_specific_options()
    
    def set_interaction_options(self, the_options):
        return self.current_interaction.apply_options(the_options)

    def execute_interaction(self):
        self.state *= -1
        return self.state

    def list_current_interaction_options(self):
        
        pass

    def set_current_interaction_options(self, theOptions):
        self.current_interaction = theOptions

    def start_current_interaction(self):
        return self.start_interaction(self.current_interaction)

    def abort_current_interaction(self):
        pass
