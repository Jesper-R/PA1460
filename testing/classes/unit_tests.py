import unittest
import Game as game
import Scene as scene
import GameObject as game_object
import InteractionType as interaction_types

# We use our own interaction diagrams made for InteractWithObject, they are faulty but those are the only ones we have.

class TestInteractWithObject(unittest.TestCase):

    def setUp(self):
        self.game = game.Game()
        self.scene = scene.Scene("Mock Scene")
        self.game.set_current_scene(self.scene)
        self.game_object = self.scene.create_game_object("Mock Object")
        self.available_interactions = self.game.select_object(self.game_object)
        self.interaction_type = interaction_types.PickUpInteraction()
        self.game.select_interaction(self.interaction_type)

    def tearDown(self):
        self.game = None
        self.scene = None
        self.game_object = None
        self.available_interactions = None
        self.interaction_type = None

    #Only deviation from our Sequence Diagram is that Scene doesnt create the game object.
    def test_select_object_positive(self):
        self.assertEqual(self.available_interactions, ["pick up", "look at", "use"])

    @unittest.expectedFailure
    def test_select_object_negative(self):
        self.assertEqual(self.available_interactions, ["melon"])

    
    def test_select_interaction_positive(self):
        self.game.select_object(self.game_object)
        specific_options = self.game.select_interaction(self.interaction_type)
        self.assertEqual(specific_options, {"amount": 0})

    @unittest.expectedFailure
    def test_select_interaction_negative(self):
        specific_options = self.game.select_interaction(self.interaction_type)
        self.assertEqual(specific_options, {})

    
    def test_set_interaction_options_positive(self):
        options = {"amount": 6}
        confirmed_options = self.game.set_interaction_options(options)
        self.assertEqual(confirmed_options, options)

    @unittest.expectedFailure
    def test_set_interaction_options_negative(self):
        options = {"amount": 6}
        confirmed_options = self.game.set_interaction_options(options)
        self.assertEqual(confirmed_options, {"amount": 5})

    
    def test_start_interaction_positive(self):
        result = self.game.start_interaction()
        self.assertEqual(result, -1)

    @unittest.expectedFailure
    def test_start_interaction_negative(self):
        result = self.game.start_interaction()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
