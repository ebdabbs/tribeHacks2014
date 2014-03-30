# MentorMatch
# Michael Salita and Lizzie Dabbs
# TribeHacks 2014

# This program analyzes a CSV that contains data of how potential mentors (bigs)
# ranked mentees (littles) and vice versa. It assumes that the number of bigs is
# greater than or equal to the number of littles. Therefore, each little is 
# guaranteed a big. However, each potential big is not guaranteed to be matched 
# with a little. The maximum number of persons that can be preffed is 10, and 
# the minimum is 5. A form for creating the correctly formatted CSV can be found
# at https://docs.google.com/forms/d/17Cu4RSMUK2A_UN2OvHcysxIlv4rwVuZw0dvVqd5csMI/viewform

# Bigs and littles are both stored as instances of a Person class.
# Big and little objects are stored in two dictionaries respectively, so that
# their preferences are accessible by their name. A scores matrix totals the 
# mutual preference values, giving added weight to how a little ranked a big.
# In the case of a tie, matching is determined by how the little ranked the big.

# MentorMatch was developed with the Big/Little relationships associated with 
# sorority and fraternity life in mind. However, it can be used for mutually 
# preferenced mentor/mentee pairings in any organization, sports team, or 
# workplace. It allows for an anonymous submission of rankings by members and a 
# fair, mathematical matching process. 

#spreadsheet = open("mentorMatch.csv", "r")
filename = input("Enter the CSV filename: ")
spreadsheet = open(filename, "r")
BigsDict = {}
LittlesDict = {}
BigsList = []
LittlesList = []
maxPreffed = 10
littlesWeight = 2

print ()

class Person:
    def __init__(self, name, twins, prefs):
        self.name = name
        self.matched = False
        if twins == "Yes":
            self.twins = True
        else:
            self.twins = False
        self.prefs = prefs

def readFile():
    # Add data to Bigs and Littles dictionary and indexed list
    spreadsheet.readline()
    bigCount = 0
    littleCount = 0     
    for line in spreadsheet:
        line = line.strip()
        line = line.split(",")
        if line[2] == "Big":
            prefListb = []
            for i in range(4, len(line)):
                if line[i] != "":
                    prefListb.append(line[i])
            newPerson = Person(line[1], line[3], prefListb)
            BigsDict[newPerson.name] = [newPerson, bigCount]
            bigCount += 1
            BigsList.append(newPerson)
            
        else:
            # newPerson is a Little
            prefListl = []
            for i in range(4, len(line)):
                if line[i] != "":
                    prefListl.append(line[i])
            newPerson = Person(line[1], line[3], prefListl)
            LittlesDict[newPerson.name] = [newPerson, littleCount]
            littleCount += 1
            LittlesList.append(newPerson)  


def create_scoresList():
    # populate 2D array with matching scores
  
    for i in range(len(LittlesList)):
        prefs = LittlesList[i].prefs
        for j in range(len(prefs)):
            #match to bigs index
            nameKey = prefs[j]
            valuesList = BigsDict[nameKey]
            bigsIndex = valuesList[1]           
            scores[i][bigsIndex][0] = maxScore - j
            scores[i][bigsIndex][1] = j
            scores[i][bigsIndex][2] += 1

    for i in range(len(BigsList)):
        prefs = BigsList[i].prefs
        for j in range(len(prefs)):
            #match to littles index
            nameKey = prefs[j]
            valuesList = LittlesDict[nameKey]
            littlesIndex = valuesList[1]
            scores[littlesIndex][i][2] += 1
            scores[littlesIndex][i][0] += maxScore - (j * littlesWeight)

def sortScores():
    # iterates through scores and matches high to low
    for little in range(len(LittlesList)):
        for big in range(len(BigsList)):
            ordScores.append([scores[little][big][0], little, big])
    ordScores.sort(reverse = True)
    
def tieBreaker():   
    for i in range(len(ordScores)):
        theCount = 1
        if (i + theCount < len(ordScores)) and (ordScores[i][0] == ordScores[i + theCount][0]):
            tempScores = [] 
            ranks = []
            ranks.append([scores[ordScores[i][1]][ordScores[i][2]][1], 0])
            tempScores.append(ordScores[i])        
            while (i + theCount < len(ordScores)) and (ordScores[i][0] == ordScores[i + theCount][0]):
                littleIndex = ordScores[i + theCount][1]
                bigIndex = ordScores[i + theCount][2]
                howLittleRankedBig = scores[littleIndex][bigIndex][1]
                ranks.append([howLittleRankedBig, theCount])
                tempScores.append(ordScores[i + theCount])
                theCount += 1
            ranks.sort()
            for j in range(i, i + theCount):
                ordScores[j] = tempScores[ranks[j-i][1]]
            i = i + theCount
        
    
def matchPeople():
    counter = 0
    for i in range(len(ordScores)):
        if(LittlesList[ordScores[i][1]].matched == False) and (BigsList[ordScores[i][2]].matched == False):
            matches[counter][0] = LittlesList[ordScores[i][1]].name
            matches[counter][1] = BigsList[ordScores[i][2]].name
            counter += 1
            LittlesList[ordScores[i][1]].matched = True
            BigsList[ordScores[i][2]].matched = True
            
def displayMatches():
    for k in range(len(matches)):
        print('{}\'s match is: {}'.format(matches[k][0], matches[k][1]))
        

readFile()
maxScore = maxPreffed * (littlesWeight + 1)
scores = [[[0, (maxScore + 1), 0] for y in range(len(BigsList))] for x in range(len(LittlesList))]
create_scoresList()
ordScores = []
sortScores()
tieBreaker()
matches = [["" for i in range(2)] for j in range(len(LittlesList))]
matchPeople()
displayMatches()
