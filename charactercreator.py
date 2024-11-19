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
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: fighter\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.archetype} (archetype)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write(f"Fighting style: {self.fightingStyle1})\nSecond wind")
        if self.level>=2:
            featuresfile.write("Action surge (x1)")
        if self.level>=3:
            featuresfile.write(f"Martial archetype (subclass): {self.archetype}\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Barbarian(): #barbarian class & outline DONE

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
                self.subclass = input("Enter primal path: ")
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
        #level, class and subclass
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: barbarian\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (primal path)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        #print("")
        #class features
        #in this case, action surge (if any), class-specific abilities, etc.

        featuresfile = open("features.txt","a")
        '''featuresfile.truncate(0)
        featuresfile.write("test1")
        featuresfile.write("test2")'''
        featuresfile.truncate(0)
        featuresfile.write(f"Rage (rage count: {self.rageCount})\nUnarmored Defense\n")
        if self.level>=2:
            featuresfile.write("Reckless attack\nDanger sense\n")
        if self.level>=3:
            featuresfile.write(f"Primal path (subclass): {self.subclass}\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Bard(): #bard class DONE

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
        #level, class and subclass
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: bard\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (bard college)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write(f"Bardic die (amount: {self.bardicDie}, d6)\n")
        if self.level>=2:
            featuresfile.write("Jack of all trades\nSong of rest (d6)\n")
        if self.level>=3:
            featuresfile.write(f"Bard college (subclass): {self.subclass}\nExpertise")#expertise
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Cleric(): #cleric class DONE

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
                self.subclass = input("Enter divine domain: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True

    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.subclass)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: cleric\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (divine domain)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        if self.level>=2:
            featuresfile.write(f"Channel divinity (x1)\nDivine domain feature: {self.subclass} domain\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Druid(): #druid class DONE

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
                self.subclass = input("Enter druid circle: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: druid\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (druid circle)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Druidic language\n")
        if self.level>=2:
            featuresfile.write(f"Wild shape\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Monk(): #monk class DONE
    #no armor/shield => AC is 10+DEX+WIS
    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus 
        self.kiPoints = 0

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>1:
                self.kiPoints=self.level
            if self.level >=3: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Monastic traditions: ") #aka subclass
                print("\t- Four Elements\n\t- Open Hand\n\t- Shadow")
                self.subclass = input("Enter monastic tradition: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: monk\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (monastic tradition)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Unarmored defense\nMartial arts\n")
        if self.level>=2:
            featuresfile.write(f"Martial arts: d4\nKi points: {self.kiPoints}\nUnarmored Movement +10ft\n")
        if self.level>=3:
            featuresfile.write("Deflect missiles\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Paladin(): #paladin class DONE

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus    
        self.fightingStyle = "none"   

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Fighting styles: ") #aka subclass
                print("\t- Blessed warrior\n\t- Blind fighting\n\t- Defense\m\t- Dueling\n\t- Great weapon fighting\n\t- Interception\n\t- Protection")
                self.fightingStyle = input("Enter fighting style: ")
            if self.level >=3:
                valid = True
                print("Sacred oaths:")
                print("\t- Ancients\n\t- Devotion\n\t- Vengeance")
                self.subclass = input("Enter sacred oath: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: paladin\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (sacred oath)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Divine sense\nLay on hands\n")
        if self.level>=2:
            featuresfile.write(f"Fighting style: {self.fightingStyle}\nDivine Smite\n")
        if self.level>=3:
            featuresfile.write("Divine health\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Ranger(): #ranger class DONE

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.favoredEnemy = "none"   
        self.fightingStyle = "none"   
        self.favoredTerrain = "none" 

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>=1:
                valid = True
                print("Favored enemy types:")
                print("\t- Aberrations\n\t- Beasts\n\t- Celestials\n\t- Constructs\n\t- Dragons\n\t- Elementals\n\t- Fey\n\t- Fiends\n\t- Giants\n\t- Monstrosities\n\t- Oozes\n\t- Plants\n\t- Undead\n")
                self.favoredEnemy = input("Enter favored enemy: ")

                print("Favored terrain types:")
                print("\t- Arctic\n\t- Coast\n\t- Desert\n\t- Forest\n\t- Grassland\n\t- Mountain\n\t- Mountain\n\t- Swamp\n\t- Underdark\n")
                self.favoredTerrain = input("Enter favored terrain: ")

            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Fighting styles: ")
                print("\t- Archery\n\t- Blind fighting\n\t- Defense\n\t- Druidic warrior\n\t- Dueling\n\t- Thrown weapon fighting\n\t- Two-weapon fighting")
                self.fightingStyle = input("Enter fighting style: ")

            if self.level>=3:
                valid = True
                print("Ranger conclaves: ")
                print("\t- Beast master\n\t- Hunter")
                self.subclass = input("Ranger conclave: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: ranger\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (ranger conclave)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write(f"Favored enemy: {self.favoredEnemy}\nFavored terrain: {self.favoredTerrain}\n")
        if self.level>=2:
            featuresfile.write(f"Fighting style: {self.fightingStyle}\n")
        if self.level>=3:
            featuresfile.write("Primeval awareness\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Rogue(): #rogue class DONE **expertise

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus       

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=3: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Roguish archetypes: ") #aka subclass
                print("\t- Arcane trickster\n\t- Assassin\n\t- Thief")
                self.subclass = input("Enter roguish archetype: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: rogue\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (roguish archetype)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Expertise\nSneak attack\nThieves' cant\n")
        if self.level>=2:
            featuresfile.write(f"Cunning action\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Sorcerer(): #druid class UNFINISHED

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
                self.subclass = input("Enter druid circle: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: monk\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (monastic tradition)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Unarmored defense\nMartial arts\n")
        if self.level>=2:
            featuresfile.write(f"Martial arts: d4\nKi points: {self.kiPoints}\nUnarmored Movement +10ft\n")
        if self.level>=3:
            featuresfile.write("Deflect missiles\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Warlock(): #druid class UNFINISHED

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
                self.subclass = input("Enter druid circle: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: monk\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (monastic tradition)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Unarmored defense\nMartial arts\n")
        if self.level>=2:
            featuresfile.write(f"Martial arts: d4\nKi points: {self.kiPoints}\nUnarmored Movement +10ft\n")
        if self.level>=3:
            featuresfile.write("Deflect missiles\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Wizard(): #druid class UNFINISHED

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
                self.subclass = input("Enter druid circle: ")
            elif self.level>3: #if level>3, loop again
                print("Please enter a number 1-3.")
            else: #allow break loop
                valid = True        
            
    def printValues(self):
        print(self.level)
        print(self.proficiencyBonus)
        print(self.archetype)

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: monk\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (monastic tradition)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Unarmored defense\nMartial arts\n")
        if self.level>=2:
            featuresfile.write(f"Martial arts: d4\nKi points: {self.kiPoints}\nUnarmored Movement +10ft\n")
        if self.level>=3:
            featuresfile.write("Deflect missiles\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring


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

    test = Barbarian()
    test.setValues()
    a = test.fileInputFeatures()
    print(a)

    #input for class; based on class certain stats will change
    #similar for race


if __name__ == "__main__":
    main()


'''featuresfile = open("features.txt","a")
        featuresfile.write("test\ntest\ntest")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        #print(filestring)'''