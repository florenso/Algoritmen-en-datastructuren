def herhaaldKwadrateren(grondgetal,macht):
    if macht == 0:
        return 1
    if macht < 0:
        return 1/herhaaldKwadrateren(grondgetal,-macht);

    resultaat = 1
    if(macht % 2 == 1):
        macht -= 1
        resultaat = grondgetal
    dummy = 0
    for dummy in range(0, macht, 2):
        resultaat *= (grondgetal * grondgetal)

    print("Aantal vermenigvuldingen is: ", (dummy/2)+1)
    return resultaat

print("Herhaald kwadrateren: 4005 ^ 465: ", herhaaldKwadrateren(256,7))
