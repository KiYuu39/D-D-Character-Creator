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
            if self.level == 3:                 #if level = 3, allow break loop & ask for archetype
                valid = True
                print("Archetypes: ")           #subclass
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
            else:              #allow break loop
                valid = True
        
        #fighter class has fighting styles
        count = self.numFightingStyles
        num = 0
        while count>0:
            print("Fighting Styles:")
            print("\t1. archery\n\t2. defense\n\t3. dueling\n\t4. great weapon fighting\n\t5. protection\n\t6. two-weapon fighting")
            while num<1 or num>6:
                num=int(input("Enter fighting style: "))
                match num:
                    case 1:
                        self.fightingStyle1="archery"
                        count-=1
                    case 2:
                        self.fightingStyle1="defense"
                        count-=1
                    case 3:
                        self.fightingStyle1="dueling"
                        count-=1
                    case 4:
                        self.fightingStyle1="great weapon fighting"
                        count-=1
                    case 5:
                        self.fightingStyle1="protection"
                        count-=1
                    case 6:
                        self.fightingStyle1="two-weapon fighting"
                        count-=1
                    case _:
                        print("Please enter valid number.\n")

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: fighter\n")
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
            if self.level == 3:                 #if level = 3, allow break loop & ask for subclass
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
            else:              #allow break loop
                valid = True

    def fileInputLevelClassSubclass(self):
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
        featuresfile = open("features.txt","a")
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
            if self.level == 3:                 #if level = 3, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Bard college: ")
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
            else:              #allow break loop
                valid = True

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: bard\n")
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
            if self.level >=1:                  #if level >=1, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Divine domains: ")
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
            else:              #allow break loop
                valid = True

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: cleric\n")
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
            if self.level >=2:                  #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Druid circles: ")
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: druid\n")
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
            if self.level >=3:                  #if level >= 2, allow break loop & ask for subclass
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: monk\n")
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
            if self.level >=2:                  #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid_a:
                    print("Fighting styles: ")
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: paladin\n")
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
                num=0
                print("Favored enemy types:")
                print("\t1. Aberrations\n\t2. Beasts\n\t3. Celestials\n\t4. Constructs\n\t5. Dragons\n\t6. Elementals\n\t7. Fey\n\t8. Fiends\n\t9. Giants\n\t10. Monstrosities\n\t11. Oozes\n\t12. Plants\n\t13. Undead\n")
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

                num=0
                print("Favored terrain types:")
                print("\t1. Arctic\n\t2. Coast\n\t3. Desert\n\t4. Forest\n\t5. Grassland\n\t6. Mountain\n\t7. Swamp\n\t8. Underdark\n")
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
            else:              #allow break loop
                valid = True        
            
    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: ranger\n")
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
        self.arcaneTrickster = False       

        self.subclass = "none"

    def getLevel(self):
        return self.level
    
    def getArcaneTrickster(self):
        return self.arcaneTrickster

    def setValues(self):
        valid = False
        valid2 = False
        while not valid:
            self.level = int(input("Level: "))  #get level (must be 1-3)
            if self.level >=3:                  #if level >= 2, allow break loop & ask for subclass
                valid = True
                while not valid2:
                    print("Roguish archetypes: ")
                    print("\t1. Arcane trickster\n\t2. Assassin\n\t3. Thief")
                    num = input("Enter roguish archetype: ")
                    match num:
                        case "1":
                            self.subclass = "Arcane Trickster"
                            self.arcaneTrickster = True
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: rogue\n")
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
            if self.level >=1:                  #if level >= 2, allow break loop & ask for subclass
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: sorcerer\n")
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
            if self.level >=1:                  #if level >= 2, allow break loop & ask for subclass
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: warlock\n")
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
            if self.level >=2:                  #if level >= 2, allow break loop & ask for subclass
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
            else:              #allow break loop
                valid = True        

    def fileInputLevelClassSubclass(self):
        levelfile = open("level.txt","a")
        levelfile.truncate(0)
        levelfile.write(f"Level: {self.level}\n")
        levelfile.write(f"Class: wizard\n")
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