Create automated unit tests for the use case "Interact with Object" using your favourite unit test framework for your programming language of choice. You may use either the given class diagram and interaction diagrams, or the refactored ones that you produced in a previous assignment. Please indicate which ones you use and include them in your assignment submission.

Test one "positive path" (where everything works as expected) for each of the system events from the use case. Test at least one path that you expect should not work for each of the system events.

Each test should contain the following steps:

Setup -- Make sure the system is in an initial state so that you can run the test. This may include creating some GameObjects, or entering a particular Scene. Since the use cases are "stateful" (you first select an object, then select what to do with the object, etc.), this setup phase will do more and more the further down the use case you get.
Call the system event you are testing, with relevant parameters.
Check that you get the expected return values or state changes in the system.
Teardown -- clean up the system so that it is ready to run the next test.
In order to test these unit tests, you will have to implement parts of the underlying system. Do this either according to your own class diagrams, or the ones provided above.

At the very least, I expect there to be a Game class to start the use case, a Scene class that knows how to find a GameObject, a GameObject class that knows what Interactions are available to it, and a class hierarchy of InteractionTypes (which may internally be able to handle InteractionOptions).

For the sake of testing, you may want to create a game object in every scene that responds with a simple text no matter what you do to it (e.g., "You taste the test object", "you open the test object", "you turn on the test object"). Please note that "turn on" and "turn off" implies a saved state, so when you look at the object, you should also get information about whether it is on or off. You may hard code your scene class such that it always creates this test object, or you may create it as part of the test setup and insert it into the scene.

In the same vein, you may want to create a test Scene that is always available and contains one or more test-gameObjects.