import random

class Fighter(): #fighter class

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
                print("Archetypes: ") #aka subclass
                print("\t- Battle Master\n\t- Champion\n\t- Eldritch Knight")
                self.archetype = input("Enter archetype: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True
        
        count = self.numFightingStyles
        while count>0:
            answer = input(f"You have {count} fighting styles to choose. To get information on fighting styles, type Q. Otherwise, enter fighting style: ")
            if answer == 'Q' or answer == 'q':
                print("Fighting Styles:")
                print("\t- archery\n\t- defense\n\t- dueling\n\t- great weapon fighting\n\t- protection\n\t- two-weapon fighting")

            else:
                self.fightingStyle1 = answer
                count-=1
            
            

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.numFightingStyles)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        print("")
        #level, class and subclass

    def fileInputFeatures(self):
        print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

class Barbarian(): #barbarian class UNFINISHED

    def __init__(self, level=1, proficiencyBonus=2, rageDamageBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.rageDamageBonus = rageDamageBonus
        self.rageCount = 2
        

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for subclass
                valid = True
                print("Primal paths: ") #aka subclass
                print("\t- Berserker\n\t- Totem Warrior")
                self.archetype = input("Enter primal path: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True
        
        if self.level>=3 and self.level<6:  #ragecount adjust for lv3+
            self.rageCount = 3
            
            

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.numFightingStyles)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        print("")
        #level, class and subclass

    def fileInputFeatures(self):
        print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

class Bard(): #bard class UNFINISHED

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.bardicDie = 2        

        self.subclass = "none" #bard college

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for subclass
                valid = True
                print("Bard college: ") #aka subclass
                print("\t- Lore\n\t- Valor")
                self.archetype = input("Enter bard college: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.bardicDie)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        print("")
        #level, class and subclass

    def fileInputFeatures(self):
        print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

class Cleric(): #cleric class basics done (add subclass specific shit)

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus       

        self.subclass = "none" #domain

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=1: #if level >=1, allow break loop & ask for subclass
                valid = True
                print("Divine domains: ") #aka subclass
                print("\t- Knowledge\n\t- Life\n\t- Light\n\t- Nature\n\t- Tempest\n\t- Trickery\n\t- War")
                self.archetype = input("Enter divine domain: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.subclass)

    def fileInputLevelClassSubclass(self):
        print("")
        #level, class and subclass

    def fileInputFeatures(self):
        print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

class Druid(): #druid class UNFINISHED

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus       

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Druid circles: ") #aka subclass
                print("\t- Land\n\t- Moon")
                self.archetype = input("Enter druid circle: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        print("")
        #level, class and subclass

    def fileInputFeatures(self):
        print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

def rollStats():
    rolls = []
    stats = [0,0,0,0,0,0]
    for i in range(6):
        for d6 in range(4):
            x = random.randint(1,6)
            #print(x)
            rolls.append(x)
        del rolls[rolls.index(min(rolls))]
        rollSum = sum(rolls)
        #print(rollSum)
        stats[i] = rollSum
        rolls=[]

    return stats




def main():
    '''test = Fighter()
    test.setValues()
    test.printValues()'''

    stats = [0,0,0,0,0,0]
    stats = rollStats()
    print(stats)


if __name__ == "__main__":
    main()
