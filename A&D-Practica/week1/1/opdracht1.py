def mymax(listOfValues):
    maxValue = 0

    if(len(listOfValues) == 0):
        print("ERROR: LIST IS EMPTY")

    for value in listOfValues:
        if(isinstance(value, (int, float, complex))):
            if (value >= maxValue):
                maxValue = value
        else:
            print("ERROR, value is NAN", value)
    return maxValue

determineMaxValue = [3,5,8,1,4,'asdf']
print(mymax(determineMaxValue))

