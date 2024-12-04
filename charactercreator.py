import random

class Fighter(): #fighter class

    def __init__(self, level=1, proficiencyBonus=2, numFightingStyles=1):
        self.level = level
        self.proficiencyBonus = proficiencyBonus
        self.numFightingStyles = numFightingStyles
        self.fightingStyle1 = "none"

        self.archetype = "none"

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

    def setValues(self):
        valid = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level>=1:
                valid = True
                print("Favored enemy types:")
                print("\t1. Aberrations\n\t2. Beasts\n\t3. Celestials\n\t4. Constructs\n\t5. Dragons\n\t6. Elementals\n\t7. Fey\n\t8. Fiends\n\t9. Giants\n\t10. Monstrosities\n\t11. Oozes\n\t12. Plants\n\t13. Undead\n")

                num=0
                while num<1 or num>13:
                    num = int(input("Enter favored enemy: "))
                    match num:
                        case 1:
                            self.favoredEnemy = "aberrations"
                        case 2:
                            self.favoredEnemy = "beasts"
                        case 3:
                            self.favoredEnemy = "celestials"
                        case 4:
                            self.favoredEnemy = "constructs"
                        case 5:
                            self.favoredEnemy = "dragons"
                        case 6:
                            self.favoredEnemy = "elementals"
                        case 7:
                            self.favoredEnemy = "fey"
                        case 8:
                            self.favoredEnemy = "fiends"
                        case 9:
                            self.favoredEnemy = "giants"
                        case 10:
                            self.favoredEnemy = "monstrosities"
                        case 11:
                            self.favoredEnemy = "oozes"
                        case 12:
                            self.favoredEnemy = "plants"
                        case 13:
                            self.favoredEnemy = "undead"
                        case _:
                            print("Please enter valid number.\n")

                print("Favored terrain types:")
                print("\t1. Arctic\n\t2. Coast\n\t3. Desert\n\t4. Forest\n\t5. Grassland\n\t6. Mountain\n\t7. Swamp\n\t8. Underdark\n")
                
                num=0
                while num<1 or num>8:
                    num = int(input("Enter favored terrain: "))
                    match num:
                        case 1:
                            self.favoredTerrain = "arctic"
                        case 2:
                            self.favoredTerrain = "coast"
                        case 3:
                            self.favoredTerrain = "desert"
                        case 4:
                            self.favoredTerrain = "forest"
                        case 5:
                            self.favoredTerrain = "grassland"
                        case 6:
                            self.favoredTerrain = "mountain"
                        case 7:
                            self.favoredTerrain = "swamp"
                        case 8:
                            self.favoredTerrain = "underdark"
                        case _:
                            print("Please enter valid number.\n")

            if self.level >=2: #if level >= 2, allow break loop & ask for subclass
                valid = True
                print("Fighting styles: ")
                print("\t1. Archery\n\t2. Blind fighting\n\t3. Defense\n\t4. Druidic warrior\n\t5. Dueling\n\t6. Thrown weapon fighting\n\t7. Two-weapon fighting")

                num=0
                while num<1 or num>7:
                    num=int(input("Enter fighting style: "))
                    match num:
                        case 1:
                            self.fightingStyle="archery"
                        case 2:
                            self.fightingStyle="blind fighting"
                        case 3:
                            self.fightingStyle="defense"
                        case 4:
                            self.fightingStyle="druidic warrior"
                        case 5:
                            self.fightingStyle="dueling"
                        case 6:
                            self.fightingStyle="thrown weapon fightong"
                        case 7:
                            self.fightingStyle="two-weapon fighting"

            if self.level>=3:
                valid = True
                print("Ranger conclaves: ")
                print("\t1. Beast master\n\t2. Hunter")

                num=0
                while num<1 or num>2:
                    num=int(input("Enter ranger conclave: "))
                    if num==1:
                        self.subclass="Beast master"
                    elif num==2:
                        self.subclass="Hunter"
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

class Rogue(): #rogue class DONE

    def __init__(self, level=1, proficiencyBonus=2):
        self.level = level
        self.proficiencyBonus = proficiencyBonus       

        self.subclass = "none"

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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

    def getLevel(self):
        return self.level

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
    #6 main stats
    stats = [0,0,0,0,0,0]
    stats = rollStats()
    print(stats)

    level = 0

    #default proficiency values
    savethrows = [False,False,False,False,False,False]
    proflist = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

    titlePrint()

    #get name======================================================================================================================
    print("Please note: if provided a numbered list, please enter corresponding number.\n")
    name = input("Enter character name: ")
    
    #get background======================================================================================================================
    print("Backgrounds: ")
    print("\t1. Acolyte\n\t2. Charlatan\n\t3. Criminal\n\t4. Spy\n\t5. Entertainer\n\t6. Folk hero\n\t7. Gladiator\n\t8. Guild artisan\n\t9. Guild merchant\n\t10. Hermit\n\t11. Knight\n\t12. Noble\n\t13. Outlander\n\t14. Pirate\n\t15. Sage\n\t16. Sailor\n\t17. Soldier\n\t18.Urchin")
    bkg = 0
    backgroundString = ""
    while bkg<1 or bkg>18:
        bkg = int(input("Enter background: "))
        if bkg<1 or bkg>18:
            print("Please enter valid number.\n")
        match bkg:
            case 1:
                backgroundString = "Acolyte"
            case 2:
                backgroundString = "Charlatan"
            case 3:
                backgroundString = "Criminal"
            case 4:
                backgroundString = "Spy"
            case 5:
                backgroundString = "Entertainer"
            case 6:
                backgroundString = "Folk Hero"
            case 7:
                backgroundString = "Gladiator"
            case 8:
                backgroundString = "Guild Artisan"
            case 9:
                backgroundString = "Guild Merchant"
            case 10:
                backgroundString = "Hermit"
            case 11:
                backgroundString = "Knight"
            case 12:
                backgroundString = "Noble"
            case 13:
                backgroundString = "Outlander"
            case 14:
                backgroundString = "Pirate"
            case 15:
                backgroundString = "Sage"
            case 16:
                backgroundString = "Sailor"
            case 17:
                backgroundString = "Soldier"
            case 18:
                backgroundString = "Urchin"
    
    #get class, subclass, class features======================================================================================================================
    valid = False
    nameblock = ""      #basic info block that goes with character name
    featuresblock = ""  #block of class-related features (added to end of character sheet with other features)
    num = 0             #temporary class type holder
    ch_class = 0        #class type value
    
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
                level = ch.getLevel()
            case 2:
                valid = True
                ch = Bard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 2
                level = ch.getLevel()
            case 3:
                valid = True
                ch = Cleric()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 3
                level = ch.getLevel()
            case 4:
                valid = True
                ch = Druid()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 4
                level = ch.getLevel()
            case 5:
                valid = True
                ch = Fighter()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 5
                level = ch.getLevel()
            case 6:
                valid = True
                ch = Monk()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 6
                level = ch.getLevel()
            case 7:
                valid = True
                ch = Paladin()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 7
                level = ch.getLevel()
            case 8:
                valid = True
                ch = Ranger()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 8
                level = ch.getLevel()
            case 9:
                valid = True
                ch = Rogue()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 9
                level = ch.getLevel()
            case 10:
                valid = True
                ch = Sorcerer()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 10
                level = ch.getLevel()
            case 11:
                valid = True
                ch = Warlock()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 11
                level = ch.getLevel()
            case 12:
                valid = True
                ch = Wizard()
                ch.setValues()
                nameblock = ch.fileInputLevelClassSubclass()
                featuresblock = ch.fileInputFeatures()
                ch_class = 12
                level = ch.getLevel()
            case _:
                print("Please enter a valid number.\n")

    #get race, race features======================================================================================================================
    racefile = open("race.txt","a")
    racefile.truncate(0)
    raceString=""
    raceblock=""

    tag = ""            #used for specific races
    race = 0            #race type value
    size = "none"
    speed = 0

    print("Races: ")
    print("\t1. Dragonborn\n\t2. Dwarf\n\t3. Elf\n\t4. Gnome\n\t5. Half Elf\n\t6. Halfling\n\t7. Half Orc\n\t8. Human\n\t9. Tiefling")
    while race>9 or race<1:
        race = int(input("Enter race: "))
        if race>9 or race<1:
            print("Please enter valid number.\n")
    
    match race: #get/calculate all race-related stats & proficiencies
        case 1: #dragonborn
            ancestry = 0
            stats[0]+=2
            stats[5]+=1
            size = "medium"
            speed = 30
            raceString="Dragonborn"

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
            racefile.write("\nLanguages: Common, draconic\n")

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
                    raceString="Hill Dwarf"
                elif dtype==2:
                    stats[0]+=2
                    racefile.write("Proficiency in light & medium armor\n")
                    raceString="Mountain Dwarf"

        case 3: #elf
            stats[1]+=2
            size = "medium"
            speed = 30
            racefile.write("Fey ancestry\nTrance\n")
            #darkvision, language

            etype = 0
            print("Elf types:\n\t1. Dark elf\n\t2. High elf\n\t3. Wood elf")
            while etype<1 or etype>3:
                etype = int(input("Enter elf type: "))
                if etype<1 or etype>3:
                    print("Please enter valid number.\n")
                elif etype==1:
                    stats[5]+=1
                    racefile.write("Superior darkvision 120ft\n")
                    racefile.write("Drow magic (dancing lights)\n")
                    racefile.write("Drow weapon training\n")
                    racefile.write("Languages: common, elven")
                    raceString="Dark Elf"
                elif etype==2:
                    stats[3]+=1
                    racefile.write("1 wizard cantrip (INT spellcast ability)\n")
                    racefile.write("Elf weapon training\n")
                    racefile.write("Languages: common, elven, additional language of choice\n")
                    raceString="High Elf"
                elif etype==3:
                    stats[4]+=1
                    racefile.write("Elf weapon training\nMask of the wild\n")
                    speed = 35
                    raceString="Wood Elf"
        
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
                    raceString="Forest Gnome"
                elif gtype==2:
                    stats[2]+=1
                    racefile.write("Artificer's lore\nTinker (clockwork toy, fire starter, music box)\n")
                    raceString="Rock Gnome"

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
                    raceString="Lightfoot Halfling"
                elif htype==2:
                    stats[2]+=1
                    racefile.write("Stout resilience\n")
                    raceString="Stout Halfling"

        case 7: #half orc
            stats[0]+=2
            stats[2]+=1
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nRestless endurance\nSavage attacks\nLanguages: Common, orc\m")
            tag = "orc"
            raceString="Half Orc"
        
        case 8: #human
            for i in range(6):
                stats[i]+=1
            size = "medium"
            speed = 30
            racefile.write("Languages: Common, additional language of choice")
            raceString="Human"

        case 9: #tiefling
            stats[5]+=2
            size = "medium"
            speed = 30
            racefile.write("Darkvision 60ft\nHellish resistance\nLanguages: Common, infernal\n")
            raceString="Tiefling"

    racefile.close()
    with open("race.txt","r") as x:
        raceblock = x.read().rstrip()
    
    #proficiencies======================================================================================================================
    proffile = open("additional_proficiencies.txt","a")
    proffile.truncate(0)

    match ch_class: #saving throw/skill proficiencies per race
        case 1: #barbarian
            savethrows[0]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[7]=True
            proflist[17]=True
        case 2: #bard
            savethrows[1]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons, hand crossbows, longswords, rapiers, shortswords\nTools: three musical instruments of choice\n")
            proflist[12]==True
            proflist[13]==True
            proflist[0]==True
        case 3: #cleric
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: all simple weapons\n")
            proflist[9]=True
            proflist[14]=True
        case 4: #druid
            savethrows[3]=True
            savethrows[4]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields (nothing made of metal for armor and shields)\nWeapon proficiencies: clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears\nTools: herbalism kit\n")
            proflist[1]=True
            proflist[10]=True
        case 5: #fighter
            savethrows[0]=True
            savethrows[2]=True
            proffile.write("Armor proficiencies: all armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[3]=True
            proflist[17]=True
        case 6: #monk
            savethrows[0]=True
            savethrows[1]=True
            proffile.write("Weapon proficiencies: simple weapons, shortswords\nTool proficiencies: A musical instrument\n")
            proflist[0]=True
            proflist[7]=True
        case 7: #paladin
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: all armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[6]=True
            proflist[14]=True
        case 8: #ranger
            savethrows[0]=True
            savethrows[1]=True
            proffile.write("Armor proficiencies: light armor, medium armor, shields\nWeapon proficiencies: simple weapons, martial weapons\n")
            proflist[1]=True
            proflist[8]=True
            proflist[10]=True
        case 9: #rogue
            savethrows[1]=True
            savethrows[3]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons, hand crossbows, longswords, rapiers, shortswords\nTools: thieves' tools")
            proflist[4]=True
            proflist[6]=True
            proflist[15]=True
            proflist[16]=True
        case 10: #sorcerer
            savethrows[2]=True
            savethrows[5]=True
            proffile.write("Weapon proficiencies: daggers, darts, slings, quarterstaffs, light crossbows\n")
            proflist[2]=True
            proflist[14]=True
        case 11: #warlock
            savethrows[4]=True
            savethrows[5]=True
            proffile.write("Armor proficiencies: light armor\nWeapon proficiencies: simple weapons\n")
            proflist[5]=True
            proflist[14]=True
        case 12: #wizard
            savethrows[3]=True
            savethrows[4]=True
            proffile.write("Weapon proficiencies: daggers, darts, slings, quarterstaffs, light crossbows\n")
            proflist[2]=True
            proflist[5]=True

    if tag=="orc":
        proflist[7]==True

    #background-related skill proficiencies & features======================================================================================================================
    match bkg:
        case 1:
            proflist[6]=True
            proflist[14]=True
            proffile.write("Two additional languages known\nShelter of the Faithful\n")
        case 2:
            proflist[4]=True
            proflist[15]=True
            proffile.write("Additional tool proficiencies: disguise kit, forgery kit\n")
        case 3 | 4:
            proflist[4]=True
            proflist[16]=True
            proffile.write("Additional tool proficiencies: gaming set, thieves' tools\n")
        case 5:
            proflist[0]=True
            proflist[12]=True
            proffile.write("Additional tool proficiencies: disguise kit, one additional musical instrument\n")
        case 6|7:
            proflist[1]=True
            proflist[17]=True
            proffile.write("Additional tool proficiencies: artisan's tools, land vehicles\n")
        case 8|9:
            proflist[6]=True
            proflist[13]=True
            proffile.write("Additional tool proficiencies: artisan's tools\nAdditional languages: 1\n")
        case 10:
            proflist[9]=True
            proflist[14]=True
            proffile.write("Additional tool proficiencies: herbalism kit\nAdditional languages: 1\n")
        case 11|12:
            proflist[13]=True
            proflist[5]=True
            proffile.write("Additional tool proficiencies: gaming set\nAdditional languages: 1\n")
        case 13:
            proflist[3]=True
            proflist[17]=True
            proffile.write("Additional tool proficiencies: one additional musical instrument of choice\nAdditional languages: 1\n")
        case 14|16:
            #athletics, perception
            #navigators tools, water vehicles
            proflist[4]=True
            proflist[11]=True
            proffile.write("Additional tool proficiencies: navigator's tools, water vehicles\n")
        case 15:
            #arcana, history
            #2 languages
            proflist[2]=True
            proflist[5]=True
            proffile.write("Additional languages: 2\n")
        case 17:
            proflist[3]=True
            proflist[7]=True
            proffile.write("Additional tool proficiencies: gaming set, land vehicles\n")
        case 18:
            #sleight of hand, stealth
            #disguise kit, thieves' tools
            proflist[15]=True
            proflist[16]=True
            proffile.write("Additional tool proficiencies: thieves' tools\n")

    proffile.close()
    addfeatsblock=""
    with open("additional_proficiencies.txt","r") as x:
        addfeatsblock = x.read().rstrip()

    #spellcasting======================================================================================================================





    #convert main 6 stats via stat table method======================================================================================================================
    convertedstats = [0,0,0,0,0,0]
    for i in range(6):
        if stats[i]==3:
            convertedstats[i] = -4
        elif stats[i]==4 or stats[i]==5:
            convertedstats[i] = -3
        elif stats[i]==7 or stats[i]==7:
            convertedstats[i] = -2
        elif stats[i]==8 or stats[i]==9:
            convertedstats[i] = -1
        elif stats[i]==13 or stats[i]==14:
            convertedstats[i] = 1
        elif stats[i]==15 or stats[i]==16:
            convertedstats[i] = 2
        elif stats[i]==17 or stats[i]==18:
            convertedstats[i] = 3
        elif stats[i]==19:
            convertedstats[i] = 4
        else:
            convertedstats[i] = 5
            
    #HP calculation======================================================================================================================
    hp=0
    match ch_class:
        case 1:
            if level==1:
                hp=12+convertedstats[2]
            elif level==2:
                hp=19+(2*convertedstats[2])
            elif level==3:
                hp=26+(3*convertedstats[2])
        case 2:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 3:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 4:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 5:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 6:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 7:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 8:
            if level==1:
                hp=10+convertedstats[2]
            elif level==2:
                hp=16+(2*convertedstats[2])
            elif level==3:
                hp=22+(3*convertedstats[2])
        case 9:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 10:
            if level==1:
                hp=6+convertedstats[2]
            elif level==2:
                hp=10+(2*convertedstats[2])
            elif level==3:
                hp=14+(3*convertedstats[2])
        case 11:
            if level==1:
                hp=8+convertedstats[2]
            elif level==2:
                hp=13+(2*convertedstats[2])
            elif level==3:
                hp=18+(3*convertedstats[2])
        case 12:
            if level==1:
                hp=6+convertedstats[2]
            elif level==2:
                hp=10+(2*convertedstats[2])
            elif level==3:
                hp=14+(3*convertedstats[2])

    if tag=="hill":
        hp+=level

    #additional skills======================================================================================================================
    bkgfile = open("other_skills","a")
    bkgfile.truncate(0)

    num = 0         #temporary number to hold skill bonus
    box = ""        #proficient/non proficient checkbox string
    for i in range(18):
        num=0
        if proflist[i]==True:
            box="[x]"
            num+=2
        else:
            box="[ ]"

        #STR
        if i==3:
            num+=convertedstats[0]
            bkgfile.write(f"{box} Athletics: ")
            bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #DEX
        elif i==0 or i==15 or i==16:
            num+=convertedstats[1]
            if i==0:
                bkgfile.write(f"{box} Acrobatics: ")
            elif i==15:
                bkgfile.write(f"{box} Sleight of Hand: ")
            elif i==16:
                bkgfile.write(f"{box} Stealth: ")
            bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #no CON based substats
        #INT
        elif i==2 or i==5 or i==8 or i==10 or i==14:
            num+=convertedstats[3]
            if i==2:
                bkgfile.write(f"{box} Arcana: ")
            elif i==5:
                bkgfile.write(f"{box} History: ")
            elif i==8:
                bkgfile.write(f"{box} Investigation: ")
            elif i==10:
                bkgfile.write(f"{box} Nature: ")
            elif i==14:
                bkgfile.write(f"{box} Religion: ")
            bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #WIS
        elif i==1 or i==6 or i==9 or i==11 or i==17:
            num+=convertedstats[4]
            if i==1:
                bkgfile.write(f"{box} Animal Handling: ")
            elif i==6:
                bkgfile.write(f"{box} Insight: ")
            elif i==9:
                bkgfile.write(f"{box} Medicine: ")
            elif i==11:
                bkgfile.write(f"{box} Perception: ")
            elif i==17:
                bkgfile.write(f"{box} Survival: ")
            bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")
        #CHA
        elif i==4 or i==7 or i==12 or i==13:
            num+=convertedstats[5]
            if i==4:
                bkgfile.write(f"{box} Deception: ")
            if i==7:
                bkgfile.write(f"{box} Intimidation: ")
            if i==12:
                bkgfile.write(f"{box} Performance: ")
            if i==13:
                bkgfile.write(f"{box} Persuasion: ")
            bkgfile.write("{0:+}".format(num))
            bkgfile.write("\n")

    bkgfile.close()
    bkgblock=""
    with open("other_skills.txt","r") as x:
        bkgblock = x.read().rstrip()

    
    


    #put everything in a file======================================================================================================================
    bigbar = "-----------------------------------------------------------------------------------------------------\n"
    sheet = open("final_character_sheet.txt","a")
    sheet.truncate(0)

    sheet.write("Character name: ")
    sheet.write(f"{name}\n{nameblock}\nRace: {raceString}\nBackground: {backgroundString}\n")
    sheet.write(bigbar)

    #maxHP
    sheet.write(f"HP: {hp}\n")
    #AC
    ac = 10+convertedstats[1]
    sheet.write(f"Base AC: {ac}\n")

    #initiative
    sheet.write(f"Speed: {speed} ft\n")
    sheet.write(f"Size: {size}\n")
    sheet.write("Initiative: ")
    sheet.write("{0:+}".format(convertedstats[1]))
    sheet.write("\n")
    
    sheet.write(bigbar)

    #6 main stats
    sheet.write(f"STR: {stats[0]}\t\t|DEX: {stats[1]}\t\t|CON: {stats[2]}\t\t|INT: {stats[3]}\t\t|WIS: {stats[4]}\t\t|CHA: {stats[5]}\n")
    sheet.write(bigbar)

    #saving throws
    temp = ""       #temporary bonus number holder
    savestring=""   #string to be written into file
    for i in range(6):
        if savethrows[i]==True:
            box="[x]"
            temp = 2+convertedstats[i]
        else:
            box="[ ]"
            temp = convertedstats[i]
        
        match i:
            case 0:
                savestring=box+" Strength: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 1:
                savestring=box+" Dexterity: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 2:
                savestring=box+" Constitution: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 3:
                savestring=box+" Intelligence: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 4:
                savestring=box+" Wisdom: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)
            case 5:
                savestring=box+" Charisma: "+"{0:+}".format(temp)+"\n"
                sheet.write(savestring)

    #additional proficiencies
    sheet.write(bkgblock)
    sheet.write(bigbar)

    #spellcasting
    sheet.write(bigbar)

    #additional features
    sheet.write(f"{featuresblock}\n")
    sheet.write(f"{raceblock}\n")
    sheet.write(f"{addfeatsblock}\n")
    

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