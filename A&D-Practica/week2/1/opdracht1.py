def herhaaldKwadrateren(grondgetal,macht):
    if macht == 0:
        return 1
    resultaat = 1
    if(macht % 2 == 1):
        macht -= 1
        resultaat *= grondgetal

    for dummy in range(0, macht, 2):
        resultaat *= (grondgetal * grondgetal)

    return resultaat

print("Herhaald kwadrateren: 4005 ^ 465: ", herhaaldKwadrateren(4005,465))
