import unittest
import classes.Game as game
import classes.Scene as scene
import classes.GameObject as game_object

# We use our own interaction diagrams made for InteractWithObject, they are faulty but those are the only ones we have.

class TestInteractWithObject(unittest.TestCase):

    def setUp(self):
        print("\nsetup")
        self.game = game.Game()
        self.scene = scene.Scene("Mock Scene")
        self.game_object = game_object.GameObject("Mock Object")

        # self.game.set_current_scene(self.scene)
        #self.scene.add_game_object(self.game_object)
        pass

    def tearDown(self):
        print("teardown")

        # These dont really do anything, more for clarity?
        self.game = None
        self.scene = None
        self.game_object = None
        pass

    def test_select_object(self):
        print("Testing select_object")

        available_interactions = self.game.select_object(self.game_object)
        self.assertEqual(available_interactions, ["pick up", "look at", "use"])


    def test_select_interaction(self):
        print("Testing select_interaction")

        specfic_options = self.game.select_interaction("pick up")
        self.assertTrue("amount" in specfic_options)


    def test_set_interaction_options(self):
        print("Testing set_interaction_options")

        pass

    def test_start_interaction(self):
        print("Testing start_interaction")

        pass

if __name__ == '__main__':
    unittest.main()