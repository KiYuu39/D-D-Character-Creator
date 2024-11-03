import random

class TestClass(): #using fighter stats for test class

    def __init__(self, level=1, proficiencyBonus=2, numFightingStyles=1):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.numFightingStyles = numFightingStyles

        self.archetype = ""

    def setValues(self):
        self.level = input("Level: ")
        self.archetype = input("Archetype: ")

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.numFightingStyles)
        print(self.archetype)





def main():
    test = TestClass()
    test.setValues()
    test.printValues()


if __name__ == "__main__":
    main()
