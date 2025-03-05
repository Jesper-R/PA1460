import testing.classes.InteractionType as InteractionType
class GameObject:
    def __init__(self, name):
        self.name = name
        self.interactionTypes = ["pick up", "look at", "use"]
        self.currentInteraction = "None"

    def listInteractionTypes(self):
        return self.interactionTypes

    def startInteraction(self, theInteractionType):
        for interaction in self.interactionTypes:
            if theInteractionType == interaction:
                return f"You ${theInteractionType} the ${self.name}."
            else:
                return "Interaction not available."

    def listCurrentInteractionOptions(self):
        pass

    def setCurrentInteractionOptions(self, theOptions):
        self.currentInteraction = theOptions

    def startCurrentInteraction(self):
        return self.startInteraction(self.currentInteraction)

    def abortCurrentInteraction(self):
        pass

def main():
    print("test")

main()