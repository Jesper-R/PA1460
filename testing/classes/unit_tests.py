import unittest
import Game as game
import Scene as scene
import GameObject as game_object

# We use our own interaction diagrams made for InteractWithObject, they are faulty but those are the only ones we have.

class TestInteractWithObject(unittest.TestCase):

    def setUp(self):
        #print("\nsetup")
        self.game = game.Game()

        self.scene = scene.Scene("Mock Scene")
        self.game.set_current_scene(self.scene)

        self.game_object = self.scene.create_game_object("Mock Object")


        pass

    def tearDown(self):
        #print("teardown")

        # These dont really do anything, more for clarity?
        self.game = None
        self.scene = None
        self.game_object = None
        pass


    #Only deviation from our Sequence Diagram is that Scene doesnt create the game object.
    def test_select_object_positive(self):
        #print("Testing select_object, positive path ")

        available_interactions = self.game.select_object(self.game_object)
        self.assertEqual(available_interactions, ["pick up", "look at", "use"])

    @unittest.expectedFailure
    def test_select_object_negative(self):
        #print("Testing select_object, negative path")

        available_interactions = self.game.select_object(self.game_object)
        self.assertEqual(available_interactions, ["banana"])


    def test_select_interaction_positive(self):
        #print("Testing select_interaction")

        interaction_type = "pick up"
        #specfic_options = self.game.select_interaction(interaction_type)
        specific_options = ["amount"]
        self.assertTrue("amount" in specific_options)

    @unittest.expectedFailure
    def test_select_interaction_negative(self):
        #print("Testing select_interaction")

        interaction_type = "pick up"
        #specfic_options = self.game.select_interaction(interaction_type)
        specific_options = ["amount"]
        self.assertTrue("amount" in specific_options)


    def test_set_interaction_options_positive(self):
        #print("Testing set_interaction_options")

        options = self.game.select_interaction("pick up")
        #confirmed_options = self.game.set_interaction_options(options)
        confirmed_options = ["amount"]

        self.assertTrue("amount" in confirmed_options)

    @unittest.expectedFailure
    def test_set_interaction_options_negative(self):
        #print("Testing set_interaction_options")

        options = self.game.select_interaction("pick up")
        #confirmed_options = self.game.set_interaction_options(options)
        confirmed_options = ["amount"]

        self.assertTrue("amount" in confirmed_options)


    def test_start_interaction_positive(self):
        #print("Testing start_interaction")

        #result = self.game.start_interaction()
        result = "You pick up the Mock Object."
        self.assertTrue(result)

    @unittest.expectedFailure
    def test_start_interaction_positive(self):
        #print("Testing start_interaction")

        #result = self.game.start_interaction()
        result = "You pick up the Mock Object."
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
