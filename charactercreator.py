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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for archetype
                valid = True
                print("Archetypes: ") #aka subclass
                print("\t1. Battle Master\n\t2. Champion\n\t3. Eldritch Knight")
                while not valid_a:
                    num = input("Enter archetype: ")
                    match num:
                        case "1":
                            self.archetype = "Battle Master"
                            valid_a = True
                        case "2":
                            self.archetype = "Champion"
                            valid_a = True
                        case "3":
                            self.archetype = "Eldritch Knight"
                            valid_a = True
                        case _:
                            print("Please enter a valid number.\n")

                
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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Primal paths: ") #aka subclass
                    print("\t1. Berserker\n\t2. Totem Warrior")
                    answer = input("Enter primal path: ")
                    if answer == "1":
                        self.subclass = "Berserker"
                        valid_a = True
                    elif answer == "2":
                        self.subclass = "Totem Warrior"
                        valid_a = True
                    else:
                        print("Enter valid number.\n")
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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level == 3: #if level = 3, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Bard college: ") #aka subclass
                    print("\t1. Lore\n\t2. Valor")
                    num = input("Enter bard college: ")
                    if num == "1":
                        self.subclass = "College of Lore"
                        valid_a = True
                    elif num=="2":
                        self.subclass = "College of Valor"
                        valid_a = True
                    else:
                        print("Please enter valid number.\n")
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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=1: #if level >=1, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Divine domains: ") #aka subclass
                    print("\t1. Knowledge\n\t2. Life\n\t3. Light\n\t4. Nature\n\t5. Tempest\n\t6. Trickery\n\t7. War")
                    num = input("Enter divine domain: ")
                    match num:
                        case "1":
                            self.subclass = "Knowledge Domain"
                            valid_a = True
                        case "2":
                            self.subclass = "Life Domain"
                            valid_a = True
                        case "3":
                            self.subclass = "Light Domain"
                            valid_a = True
                        case "4":
                            self.subclass = "Nature Domain"
                            valid_a = True
                        case "5":
                            self.subclass = "Tempest Domain"
                            valid_a = True
                        case "6":
                            self.subclass = "Trickery Domain"
                            valid_a = True
                        case "7":
                            self.subclass = "War Domain"
                            valid_a = True
                        case _:
                            print("Please enter valid number.\n")
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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Druid circles: ") #aka subclass
                    print("\t1. Land\n\t2. Moon")
                    num = input("Enter druid circle: ")
                    if num=="1":
                        self.subclass = "Circle of the Land"
                        valid_a = True
                    elif num=="2":
                        self.subclass = "Circle of the Moon"
                        valid_a = True
                    else:
                        print("Please enter valid number.\n")
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
        valid_a = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>1:
                self.kiPoints=self.level
            if self.level >=3: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Monastic traditions: ") #aka subclass
                    print("\t1. Four Elements\n\t2. Open Hand\n\t3. Shadow")
                    num = input("Enter monastic tradition: ")
                    if num=="1":
                        self.subclass = "Four Elements"
                        valid_a = True
                    elif num=="2":
                        self.subclass = "Open Hand"
                        valid_a = True
                    elif num=="3":
                        self.subclass = "Shadow"
                        valid_a = True
                    else:
                        print("Please enter valid number.\n")
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
        valid_a = False
        valid_b = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Fighting styles: ") #aka subclass
                    print("\t1. Blessed warrior\n\t2. Blind fighting\n\t3. Defense\m\t4. Dueling\n\t5. Great weapon fighting\n\t6. Interception\n\t7. Protection")
                    num = input("Enter fighting style: ")

                    match num:
                        case "1":
                            self.fightingStyle = "Blessed Warrior"
                            valid_a = True
                        case "2":
                            self.fightingStyle = "Blind Fighting"
                            valid_a = True
                        case "3":
                            self.fightingStyle = "Defense"
                            valid_a = True
                        case "4":
                            self.fightingStyle = "Dueling"
                            valid_a = True
                        case "5":
                            self.fightingStyle = "Great Weapon Fighting"
                            valid_a = True
                        case "6":
                            self.fightingStyle = "Interception"
                            valid_a = True
                        case "7":
                            self.fightingStyle = "Protection"
                            valid_a = True
                        case _:
                            print("Please enter valid number.\n")
            if self.level >=3:
                valid = True
                while not valid_b:
                    print("Sacred oaths:")
                    print("\t1. Ancients\n\t2. Devotion\n\t3. Vengeance")
                    num = input("Enter sacred oath: ")
                    if num=="1":
                        self.subclass = "Oath of the Ancients"
                        valid_b = True
                    elif num=="2":
                        self.subclass = "Oath of Devotion"
                        valid_b = True
                    elif num=="3":
                        self.subclass = "Oath of Vengeance"
                        valid_b = True
                    else:
                        print("Please enter valid number.\n")
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

class Ranger(): #finish switch cases

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
        valid2 = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=3: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid2:
                    print("Roguish archetypes: ") #aka subclass
                    print("\t1. Arcane trickster\n\t2. Assassin\n\t3. Thief")
                    num = input("Enter roguish archetype: ")
                    match num:
                        case "1":
                            self.subclass = "Arcane Trickster"
                            valid2 = True
                        case "2":
                            self.subclass = "Assassin"
                            valid2 = True
                        case "3":
                            self.subclass = "Thief"
                            valid2 = True
                        case _:
                            print("Please enter valid number.")
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

class Sorcerer(): #sorcerer class DONE

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus   
        self.sorceryPoints = 0    
        self.meta1 = "none"
        self.meta2 = "none"

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>1:
                self.sorceryPoints = self.level
            if self.level >=1: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Sorcerous origins: ") #aka subclass
                print("\t- Draconic bloodline\n\t- Wild magic")
                self.subclass = input("Enter sorcerous origin: ")
                if self.level>2:
                    print("Metamagic options: ")
                    print("\t- Careful spell\n\t- Distant spell\n\t- Empowered spell\n\t- Extended spell\n\t- Heightened spell\n\t- Quickened spell\n\t- Seeking spell\n\t- Subtle spell\n\t- Transmuted spell\n\t- Twinned spell\n")
                    self.meta1 = input("Enter first metamagic option: ")
                    self.meta2 = input("Enter second metamagic option: ")
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
        levelfile.write(f"Class: sorcerer\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (sorcerous origin)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        if self.level>=2:
            featuresfile.write("Font of magic\n")
        if self.level>=3:
            featuresfile.write(f"Metamagic: {self.meta1}, {self.meta2}\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Warlock(): #warlock class DONE

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus     
        self.pact = "none"  

        self.subclass = "none"

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=1: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Otherworldly patrons: ") #aka subclass
                print("\t- Archfey\n\t- Fiend\n\t- Great old one")
                self.subclass = input("Enter patron: ")
                if self.level>=3:
                    print("Pact boons: ")
                    print("\t- Pact of the Blade\n\t- Pact of the Chain\n\t- Pact of the Tome\n\t- Pact of the Talisman\n")
                    self.pact = input("Enter pact boon: ")
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
        levelfile.write(f"Class: warlock\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (otherworldly patron)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Pact magic\n")
        if self.level>=2:
            featuresfile.write("Eldritch invocations\n")
        if self.level>=3:
            featuresfile.write(f"Pact boon: {self.pact}\n")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

class Wizard(): #wizard class DONE

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
                print("Arcane traditions: ") #aka subclass
                print("\t- Abjuration\n\t- Conjuration\n\t- Divination\n\t- Enchantment\n\t- Evocation\n\t- Illusion\n\t- Necromancy\n\t- Transmutation")
                self.subclass = input("Enter arcane tradition: ")
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
        levelfile.write(f"Class: wizard\n") #since classes are class-specific, just manual input here
        levelfile.write(f"Subclass: {self.subclass} (arcane tradition)\n")
        levelfile.close()

        with open("level.txt","r") as file:
            filestring = file.read().rstrip()
        return filestring

    def fileInputFeatures(self):
        featuresfile = open("features.txt","a")
        featuresfile.truncate(0)
        featuresfile.write("Arcane recovery\n")
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

def titlePrint():
    print("\t\t\t\t\t\t________     __      ________   ")
    print("\t\t\t\t\t\t`MMMMMMMb.  6MMb     `MMMMMMMb. ")
    print("\t\t\t\t\t\t MM    `Mb 6M' `b     MM    `Mb ")
    print("\t\t\t\t\t\t MM     MM 8M  ,9     MM     MM ")
    print("\t\t\t\t\t\t MM     MM YM.,9  ___ MM     MM ")
    print("\t\t\t\t\t\t MM     MM  `Mb   `M' MM     MM ")
    print("\t\t\t\t\t\t MM     MM ,M'MM   P  MM     MM ")
    print("\t\t\t\t\t\t MM     MM MM  YM. 7  MM     MM ")
    print("\t\t\t\t\t\t MM     MM MM   `Mb   MM     MM ")
    print("\t\t\t\t\t\t MM    .M9 YM.   7MM  MM    .M9 ")
    print("\t\t\t\t\t\t_MMMMMMM9'  YMMM9  YM_MMMMMMM9' ")
                                
    print("   ____   ___                                                                         ____                                                    ")
    print("  6MMMMb/ `MM                                                                        6MMMMb/                                                  ")
    print(" 8P    YM  MM                                           /                           8P    YM                            /                     ")
    print("6M      Y  MM  __      ___   ___  __    ___     ____   /M      ____  ___  __       6M      Y ___  __   ____      ___   /M      _____  ___  __ ")
    print("MM         MM 6MMb   6MMMMb  `MM 6MM  6MMMMb   6MMMMb./MMMMM  6MMMMb `MM 6MM       MM        `MM 6MM  6MMMMb   6MMMMb /MMMMM  6MMMMMb `MM 6MM ")
    print("MM         MMM9 `Mb 8M'  `Mb  MM69 \" 8M'  `Mb 6M'   Mb MM    6M'  `Mb MM69 \"       MM         MM69 \" 6M'  `Mb 8M'  `Mb MM    6M'   `Mb MM69 \" ")
    print("MM         MM'   MM     ,oMM  MM'        ,oMM MM    `' MM    MM    MM MM'          MM         MM'    MM    MM     ,oMM MM    MM     MM MM'    ")
    print("MM         MM    MM ,6MM9'MM  MM     ,6MM9'MM MM       MM    MMMMMMMM MM           MM         MM     MMMMMMMM ,6MM9'MM MM    MM     MM MM   ")  
    print("YM      6  MM    MM MM'   MM  MM     MM'   MM MM       MM    MM       MM           YM      6  MM     MM       MM'   MM MM    MM     MM MM     ")
    print(" 8b    d9  MM    MM MM.  ,MM  MM     MM.  ,MM YM.   d9 YM.  ,YM    d9 MM            8b    d9  MM     YM    d9 MM.  ,MM YM.  ,YM.   ,M9 MM     ")
    print("  YMMMM9  _MM_  _MM_`YMMM9'Yb_MM_    `YMMM9'Yb.YMMMM9   YMMM9 YMMMM9 _MM_            YMMMM9  _MM_     YMMMM9  `YMMM9'Yb.YMMM9 YMMMMM9 _MM_    \n\n\n")


def main():
    '''test = Fighter()
    test.setValues()
    test.printValues()'''

    stats = [0,0,0,0,0,0]
    stats = rollStats()
    print(stats)

    #input for class; based on class certain stats will change
    #similar for race

    titlePrint()

    #get basic info
    print("Please note: if provided a numbered list, please enter corresponding number.\n")
    name = input("Enter character name: ")
    print("Backgrounds: ")
    print("\t- Acolyte\n\t- Charlatan\n\t- Criminal\n\t- Spy\n\t- Entertainer\n\t- Folk hero\n\t- Gladiator\n\t- Guild artisan\n\t- Guild merchant\n\t- Hermit\n\t- Knight\n\t- Noble\n\t- Outlander\n\t- Pirate\n\t- Sage\n\t- Sailor\n\t- Soldier\n\t- Urchin")
    background = input("Enter background: ")

    #get class
    valid = False
    nameblock = ""
    featuresblock = ""
        
    while not valid:
        print("Classes: ")
        print("\t1. Barbarian\n\t2. Bard\n\t3. Cleric\n\t4. Druid\n\t5. Fighter\n\t6. Monk\n\t7. Paladin\n\t8. Ranger\n\t9. Rogue\n\t10. Sorcerer\n\t11. Warlock\n\t12. Wizard")
        num = int(input("Enter class: "))

        match num:
            case 1:
                valid = True
                ch = Barbarian()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 2:
                valid = True
                ch = Bard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 3:
                valid = True
                ch = Cleric()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 4:
                valid = True
                ch = Druid()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 5:
                valid = True
                ch = Fighter()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 6:
                valid = True
                ch = Monk()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 7:
                valid = True
                ch = Paladin()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 8:
                valid = True
                ch = Ranger()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 9:
                valid = True
                ch = Rogue()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 10:
                valid = True
                ch = Sorcerer()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 11:
                valid = True
                ch = Warlock()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case 12:
                valid = True
                ch = Wizard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
            case _:
                print("Please enter a valid number.\n")


                                                                                                                                              



if __name__ == "__main__":
    main()


'''featuresfile = open("features.txt","a")
        featuresfile.write("test\ntest\ntest")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        #print(filestring)'''