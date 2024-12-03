# DnD-Character-Creator
Final project for ANGM2305. Goal is to create a D&amp;D Character Creator that calculates all starter stats.

**Repository link:** https://github.com/KiYuu39/DnD-Character-Creator.git

## Description
This program will allow someone creating a D&D character to input race, class, etc. to get character stats without doing any math themselves.
I aim to have calculation of all basic stats (STR, DEX, CON, INT, WIS, CHA as well as max HP and default AC).

## Features
This program will feature a text-based input-output system. The user will input race, class, level, subclass, etc. and the program will calculate the necessary values. The program will most likely utilize switch cases and either output directly to console or output to a text file.

## Challenges
Due to the number of classes and features in D&D, the complexity will rapidly increase the more features I add on. I also am not the most experienced in working with large amounts of data and having them interact together. I also think that implementing a point-buy system would be difficult.

## Outcomes
### Minimal Viable Outcome (bare minimum features of this project)
- calculate STR, DEX, CON, INT, WIS, CHA, max HP, and default HP based on 4d6 system
- implement only PHB classes/subclasses/races/backgrounds
- implement only 1st level or 3rd level
- add/calculate proficiency bonuses
- spell slot amount indicator & spell stats calculation (if needed depending on class)
- print 'character sheet' to a file or console

### Ideal Outcome (in addition to Minimal Viable Outcome)
- add option to calculate stats with pointbuy system
- add additional classes/subclasses/races within D&D canon (no UA, etc.)
- add custom background/custom lineage option
- add rolling for personality traits/ideals/bonds/flaws
- any level (1-9 inputted for character, up to 20 if really pushing it)

## Milestones
- Week 1:
    - decide output style of character sheet
    - create output file structure
    - break code down into menu and functions/class functions
    - create barebone menu structure, allow input of character name, race, class, and level
- Week 2:
    - implement classes and subclasses (up to 3rd level only)
    - implement races
    - implement 4d6 system
    - add upper level race features
    - finalize output style/continually test proper output
    - input of any character level (1-20)
- Week 3:
    - calculation of 6 main stats
    - calculation of substats
    - implementation of player choice for race-specific and class-specific substat bonuses
    - implementation of proficiency bonuses
    - add upper level class features
- Week 4:
    - spell slot/stat implementation if needed for class
    - add upper level class features (inc. spell slots)
    - custom lineage/background option
    - any additional classes/subclasses/races
    - roll for traits
- Final Week:
    - code cleanup/output cleanup
    - implement any extra features that can be
    - remove any unfinished/unable to finish features
    - video demonstration & README.md file
