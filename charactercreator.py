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
        valid2 = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>1:
                self.sorceryPoints = self.level
            if self.level >=1: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid2:
                    print("Sorcerous origins: ") #aka subclass
                    print("\t1. Draconic bloodline\n\t2. Wild magic")
                    num = input("Enter sorcerous origin: ")
                    if num=="1":
                        self.subclass = "Draconic Bloodline"
                        valid2 = True
                    elif num=="2":
                        self.subclass = "Wild Magic"
                        valid2 = True
                    else:
                        print("Please enter valid number.\n")
                valid2 = False
                count = 2
                if self.level>2:
                    while not valid2:
                        print("Metamagic options: ")
                        print("\t1. Careful spell\n\t2. Distant spell\n\t3. Empowered spell\n\t4. Extended spell\n\t5. Heightened spell\n\t6. Quickened spell\n\t7. Seeking spell\n\t8. Subtle spell\n\t9. Transmuted spell\n\t10. Twinned spell\n")
                        while count>0:
                            num = int(input("Enter metamagic option: "))
                            match num:
                                case 1:
                                    self.meta1 = "Careful spell"
                                    count-=1
                                case 2:
                                    self.meta1 = "Distant spell"
                                    count-=1
                                case 3:
                                    self.meta1 = "Empowered spell"
                                    count-=1
                                case 4:
                                    self.meta1 = "Extended spell"
                                    count-=1
                                case 5:
                                    self.meta1 = "Heightened spell"
                                    count-=1
                                case 6:
                                    self.meta1 = "Quickened spell"
                                    count-=1
                                case 7:
                                    self.meta1 = "Seeking spell"
                                    count-=1
                                case 8:
                                    self.meta1 = "Subtle spell"
                                    count-=1
                                case 9:
                                    self.meta1 = "Transmuted spell"
                                    count-=1
                                case 10:
                                    self.meta1 = "Twinned spell"
                                    count-=1
                                case _:
                                    print("Please enter valid number.\n")
                        if count<1:
                            valid2=True
                        
                        print("\t1. Careful spell\n\t2. Distant spell\n\t3. Empowered spell\n\t4. Extended spell\n\t5. Heightened spell\n\t6. Quickened spell\n\t7. Seeking spell\n\t8. Subtle spell\n\t9. Transmuted spell\n\t10. Twinned spell\n")
                        while count>1:
                            num = input("Enter first metamagic option: ")
                            match num:
                                case "1":
                                    self.meta2 = "Careful spell"
                                    count-=1
                                case "2":
                                    self.meta2 = "Distant spell"
                                    count-=1
                                case "3":
                                    self.meta2 = "Empowered spell"
                                    count-=1
                                case "4":
                                    self.meta2 = "Extended spell"
                                    count-=1
                                case "5":
                                    self.meta2 = "Heightened spell"
                                    count-=1
                                case "6":
                                    self.meta2 = "Quickened spell"
                                    count-=1
                                case "7":
                                    self.meta2 = "Seeking spell"
                                    count-=1
                                case "8":
                                    self.meta2 = "Subtle spell"
                                    count-=1
                                case "9":
                                    self.meta2 = "Transmuted spell"
                                    count-=1
                                case "10":
                                    self.meta2 = "Twinned spell"
                                    count-=1
                                case _:
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
        valid2 = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=1: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid2:
                    print("Otherworldly patrons: ") #aka subclass
                    print("\t1. Archfey\n\t2. Fiend\n\t3. Great old one")
                    num = input("Enter patron: ")
                    if num=="1":
                        self.subclass = "Archfey Patron"
                        valid2 = True
                    elif num=="2":
                        self.subclass = "Fiend Patron"
                        valid2 = True
                    elif num=="3":
                        self.subclass = "Great Old One Patron"
                        valid2 = True
                    else:
                        print("Please enter valid number.\n")
                if self.level>=3:
                    valid2 = False
                    while not valid2:
                        print("Pact boons: ")
                        print("\t1. Pact of the Blade\n\t2. Pact of the Chain\n\t3. Pact of the Tome\n\t4. Pact of the Talisman\n")
                        num = input("Enter pact boon: ")

                        match num:
                            case "1":
                                self.pact = "Pact of the Blade"
                                valid2 = True
                            case "2":
                                self.pact = "Pact of the Chain"
                                valid2 = True
                            case "3":
                                self.pact = "Pact of the Tome"
                                valid2 = True
                            case "4":
                                self.pact = "Pact of the Talisman"
                                valid2 = True
                            case _:
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
        valid2 = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid2:
                    print("Arcane traditions: ") #aka subclass
                    print("\t1. Abjuration\n\t2. Conjuration\n\t3. Divination\n\t4. Enchantment\n\t5. Evocation\n\t6. Illusion\n\t7. Necromancy\n\t8. Transmutation")
                    num = input("Enter arcane tradition: ")
                    match num:
                        case "1":
                            self.subclass = "Abjuration"
                            valid2 = True 
                        case "2":
                            self.subclass = "Conjuration"
                            valid2 = True 
                        case "3":
                            self.sublcass = "Divination"
                            valid2 = True
                        case "4":
                            self.subclass = "Enchantment"
                            valid2 = True
                        case "5":
                            self.subclass = "Evocation"
                            valid2 = True 
                        case "6":
                            self.subclass = "Illusion"
                            valid2 = True 
                        case "7":
                            self.subclass = "Necromancy"
                            valid2 = True
                        case "8":
                            self.subclass = "Transmutation"
                            valid2 = True
                        case _:
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

    #default proficiency values
    #proficient = [False,False,False,False,False,False]
    savethrows = [False,False,False,False,False,False]
    proflist = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    #input for class; based on class certain stats will change
    #similar for race

    titlePrint()

    #get basic info
    print("Please note: if provided a numbered list, please enter corresponding number.\n")
    name = input("Enter character name: ")
    print("Backgrounds: ")
    print("\t- Acolyte\n\t- Charlatan\n\t- Criminal\n\t- Spy\n\t- Entertainer\n\t- Folk hero\n\t- Gladiator\n\t- Guild artisan\n\t- Guild merchant\n\t- Hermit\n\t- Knight\n\t- Noble\n\t- Outlander\n\t- Pirate\n\t- Sage\n\t- Sailor\n\t- Soldier\n\t- Urchin")
    background = input("Enter background: ")

    #get class & text blocks for name info and feature info; add class proficiencies
    valid = False
    nameblock = ""
    featuresblock = ""
    num = 0 #num is class type number
    ch_class = 0
    
    #add class variable (to access class type outside of this while loop)
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
                ch_class = 1
            case 2:
                valid = True
                ch = Bard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 2
            case 3:
                valid = True
                ch = Cleric()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 3
            case 4:
                valid = True
                ch = Druid()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 4
            case 5:
                valid = True
                ch = Fighter()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 5
            case 6:
                valid = True
                ch = Monk()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 6
            case 7:
                valid = True
                ch = Paladin()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 7
            case 8:
                valid = True
                ch = Ranger()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 8
            case 9:
                valid = True
                ch = Rogue()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 9
            case 10:
                valid = True
                ch = Sorcerer()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 10
            case 11:
                valid = True
                ch = Warlock()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 11
            case 12:
                valid = True
                ch = Wizard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 12
            case _:
                print("Please enter a valid number.\n")

    #default HP/AC calculation
    #get race (speed as well), inc. subrace as needed
        #18 substats, make list of ints for the + or - buffs to substats

    tag = "" #used for specific races
    race = 0
    size = "none"
    speed = 0
    print("Races: ")
    print("\t1. Dragonborn\n\t2. Dwarf\n\t3. Elf\n\t4. Gnome\n\t5. Half Elf\n\t6. Halfling\n\t7. Half Orc\n\t8. Human\n\t9. Tiefling")
    while race>9 or race<1:
        race = int(input("Enter race: "))
        if race>9 or race<1:
            print("Please enter valid number.\n")

    #main access variable initialization
    speed = 0
    size = ""
    
    #file for all race related features
    racefile = open("race.txt")
    racefile.truncate(0)

    #STR DEX CON INT WIS CHA
    #switch case for all race stats
    match race:
        case 1: #dragonborn
            ancestry = 0
            stats[0]+=2
            stats[5]+=1
            size = "medium"
            speed = 30

            print("Draconic ancestry colors:")
            print("\t1. Black\n\t2. Copper\n\t3. Blue\n\t4. Bronze\n\t5. Brass\n\t6. Gold\n\t7. Red\n\t8. Green\n\t9. Silver\n\t10. White")
            while ancestry<1 or ancestry>10:
                ancestry = int(input("Enter draconic ancestry: "))
                if ancestry<1 or ancestry>10:
                    print("Please enter valid number.\n")
                elif ancestry==1 or ancestry==2:
                    element = "acid\tBreath weapon: 5x30ft line, DEX save\nResistance to acid\n"
                elif ancestry==3 or ancestry==4:
                    element = "lightning\tBreath weapon: 5x30ft line, DEX save\nResistance to lightning"
                elif ancestry==5:
                    element = "fire\tBreath weapon: 5x30ft line, DEX save\nResistance to fire\n"
                elif ancestry==6 or ancestry==7:
                    element = "fire\tBreath weapon: 15ft cone, DEX save\nResistance to fire\n"
                elif ancestry==8:
                    element = "poison\tBreath weapon: 15ft cone, DEX save\nResistance to poison"
                elif ancestry==9 or ancestry==10:
                    element = "cold\tBreath weapon: 15ft cone, CON save\nResistance to cold\n"

            racefile.write(element)
            racefile.write("Languages: Common, draconic\n")

        case 2: #dwarf
            stats[2]+=2
            size = "medium"
            racefile.write("Speed not reduced by heavy armor\n")
            racefile.write("Darkvision 60ft\n")
            racefile.write("Dwarven resilience\nDwarven combat training\nStonecunning\nTool proficiency: Mason's tools\n")
            racefile.write("Languages: Common, dwarvish\n")

            dtype = 0
            print("Dwarf types:\n\t1. Hill dwarf\n\t2. Mountain dwarf")
            while dtype<1 or dtype>2:
                dtype = int(input("Enter dwarf type: "))
                if dtype<1 or dtype>2:
                    print("Please enter valid number.\n")
                elif dtype==1:
                    stats[4]+=1
                    tag = "hill"
                elif dtype==2:
                    stats[0]+=2
                    racefile.write("Proficiency in light & medium armor\n")

        case 3: #elf
            stats[1]+=2
            size = "medium"
            speed = 30
            racefile.write("Fey ancestry\nTrance\n")
            #darkvision, language

            etype = 0
            print("Elf types:\n\t1. Dark elf\n\t2. High elf\n\t3. Wood elf")
            while etype<1 or dtype>3:
                etype = int(input("Enter elf type: "))
                if etype<1 or etype>3:
                    print("Please enter valid number.\n")
                elif etype==1:
                    stats[5]+=1
                    racefile.write("Superior darkvision 120ft\n")
                    racefile.write("Drow magic (dancing lights)\n")
                    racefile.write("Drow weapon training\n")
                    racefile.write("Languages: common, elven")
                elif etype==2:
                    stats[3]+=1
                    racefile.write("1 wizard cantrip (INT spellcast ability)\n")
                    racefile.write("Elf weapon training\n")
                    racefile.write("Languages: common, elven, additional language of choice\n")
                elif etype==3:
                    stats[4]+=1
                    racefile.write("Elf weapon training\nMask of the wild\n")
                    speed = 35
        #STR DEX CON INT WIS CHA
        case 4: #gnome
            stats[3]+=2
            size = "small"
            speed = 25
            racefile.write("Darkvision 60ft\nGnome cunning\n")
            racefile.write("Languages: Common, gnomish\n")

            gtype = 0
            print("Gnome types:\n\t1. Forest gnome\n\t2. Rock gnome")
            while gtype<1 or gtype>2:
                gtype = int(input("Enter gnome type: "))
                if gtype<1 or gtype>2:
                    print("Please enter valid number.\n")
                elif gtype==1:
                    stats[1]+=1
                    racefile.write("Natural illusionist (INT)\nSpeak with small beasts\n")
                elif gtype==2:
                    stats[2]+=1
                    racefile.write("Artificer's lore\nTinker (clockwork toy, fire starter, music box)\n")

        case 5: #half elf
            stats[5]+=2
            stats[1]+=1
            stats[3]+=1
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nFey ancestry\nLanguages: Common, elven, additional language of choice\n")
            racefile.write("Half-elf versatility\n")

        case 6: #halfling
            stats[1]+=2
            size = "small"
            speed = 25
            racefile.write("Lucky\nBrave\nNimble\nLanguages: Common, halfling\n")

            htype = 0
            print("Halfling types:\n\t1. Lightfoot halfling\n\t2. Stout halfling")
            while htype<1 or htype>2:
                htype = int(input("Enter halfling type: "))
                if htype<1 or htype>2:
                    print("Please enter valid number.\n")
                elif htype==1:
                    stats[5]+=1
                    racefile.write("Naturally stealthy\n")
                elif htype==2:
                    stats[2]+=1
                    racefile.write("Stout resilience\n")

        case 7: #half orc
            stats[0]+=2
            stats[2]+=1
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nRestless endurance\nSavage attacks\nLanguages: Common, orc\m")
            tag = "orc"

        
        case 8: #human
            for i in range(6):
                stats[i]+=1
            size = "medium"
            speed = 30
            racefile.write("Languages: Common, additional language of choice")

        case 9: #tiefling
            stats[5]+=2
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nHellish resistance\nLanguages: Common, infernal\n")

    racefile.close

    #proficiencies
    proffile = open("additional_proficiencies.txt")
    proffile.truncate(0)
    #STR DEX CON INT WIS CHA
    if ch_class==1:
        savethrows[0]=True
        savethrows[2]=True
        proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
        proflist[7]=True
        proflist[17]=True
    if ch_class==2:
        print()

        





    #spellcasting


    #put everything in a file
    bigbar = "-----------------------------------------------------------------------------------------------------\n"
    sheet = open("final_character_sheet.txt")
    sheet.truncate(0)

    sheet.write("Character name: ")
    sheet.write(f"{name}\n{nameblock}\nRace: {race}\nBackground: {background}")
    sheet.write(bigbar)

    #maxHP
    #AC
    #initiative
    sheet.write(f"Speed: {speed}\n")
    sheet.write(bigbar)

    #STR DEX CON INT WIS CHA
    sheet.write(f"STR: {stats[0]}\t\t|DEX: {stats[1]}\t\t|CON: {stats[2]}\t\t|INT: {stats[3]}\t\t|WIS: {stats[4]}\t\t|CHA: {stats[5]}\n")
    sheet.write(bigbar)

    #saving throws

    #ability checks
    sheet.write(bigbar)

    #spellcasting
    sheet.write(bigbar)

    #additional features
    sheet.write(f"{featuresblock}\n")
        #also race features need to be written
    

    sheet.close()
    print("\n\nCharacter sheet complete.\n")
    print(sheet)



                                                                                                                                              



if __name__ == "__main__":
    main()


'''featuresfile = open("features.txt","a")
        featuresfile.write("test\ntest\ntest")
        featuresfile.close()

        with open("features.txt","r") as file:
            filestring = file.read().rstrip()
        #print(filestring)'''