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
    seen = set()
    uniqDays = []
    numberOfDuplicates = 0
    for onePerson in oneClassRoom:
        if onePerson not in seen:
            if(oneClassRoom.count(onePerson) >= 2):
                uniqDays.append(oneClassRoom.count(onePerson))
                seen.add(onePerson)

    #print(sum(uniqDays))
    peopleSameDate.append(sum(uniqDays))


print("Er zijn 2 mensen op dezelfde dag jarig in ",peopleSameDate.count(2)," klassen van de ", numberOfClassrooms ," klassen met",numberOfPeoplePerClassroom," mensen per klas", )
print("Hoeveel keer zijn er van de ", numberOfClassrooms ," klassen met ",numberOfPeoplePerClassroom," mensen, 3 op dezelfde dag jarig:", peopleSameDate.count(3))

print(len(peopleSameDate),"\n")
print(peopleSameDate)
#print(sorted(peopleSameDate,  key=lambda x: x[1]))