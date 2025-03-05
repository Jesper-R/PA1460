import classes.InteractionTypes
class GameObject:
    def __init__(self, name):
        self.name = name
        self.interactionTypes = ["pick up", "look at", "use"]

    def listInteractionTypes(self):
        return self.interactionTypes

    def startInteraction(self, theInteractionType):
        pass

    def listCurrentInteractionOptions(self):
        pass

    def setCurrentInteractionOptions(self, theOptions):
        pass

    def startCurrentInteraction(self):
        pass
    
    def abortCurrentInteraction(self):
        pass

def main():
    print("test")

main()