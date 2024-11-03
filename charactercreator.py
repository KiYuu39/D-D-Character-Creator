import random

class TestClass(): #using fighter stats for test class

    def __init__(self, level=1, proficiencyBonus=2, numFightingStyles=1):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.numFightingStyles = numFightingStyles
        self.fightingStyle1 = "none"

        self.archetype = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for archetype
                valid = True
                self.archetype = input("Archetype: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True
        
        count = self.numFightingStyles
        while count>0:
            answer = input(f"You have {count} fighting styles to choose. To get information on fighting styles, type Q. Otherwise, enter fighting style: ")
            if answer == 'Q' or answer == 'q':
                print("information")
            else:
                self.fightingStyle1 = answer
                count-=1
            
            

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
