import random

def generateRandomList(minNumber, maxNumber, numberOfItems):
    return [random.randrange(minNumber,maxNumber,1) for _ in range (numberOfItems)]

numberOfDays = 365
numberOfPeoplePerClassroom = 23
numberOfClassrooms = 100



schoolOfPeople = []

for i in range(1, numberOfClassrooms):
    schoolOfPeople.append(generateRandomList(1,numberOfDays,numberOfPeoplePerClassroom))

peopleSameDate = []
i = 0;
for oneClassRoom in schoolOfPeople:
    peopleInSameClass = False
    for onePerson in oneClassRoom:
        if not peopleInSameClass:
            if(oneClassRoom.count(onePerson) >= 2):
                peopleInSameClass = True

    #print(sum(uniqDays))
    peopleSameDate.append(peopleInSameClass)


print("Er zijn 2 mensen op dezelfde dag jarig in ",peopleSameDate.count(True)," klassen van de ", numberOfClassrooms ," klassen met",numberOfPeoplePerClassroom," mensen per klas", )

print(peopleSameDate)
#print(sorted(peopleSameDate,  key=lambda x: x[1]))

print("De kans dat er twee mensen in een klas van 23 mensen op dezelfde dag jarig zijn is: ", (peopleSameDate.count(True) / numberOfClassrooms))