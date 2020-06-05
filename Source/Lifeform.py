# Base class for all lifeforms, this class should only be used for inheritance
class Lifeform(object):
    condition = []

    speed = 0

    # Instance IDs
    parentFather = ""
    parentMother = ""

    # Eat,  drink, reproduce, heal, explore
    goalLife = ""
    goalCurrent = ""

    # (per lifeform) # ageDevelopment = young, teen, adult, elder

    def __init__(self):
        self.x = "Test"

# bug > frog > snake > honey badger
