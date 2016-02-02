def mybin(invoerGetal):
    if invoerGetal == 0 or invoerGetal == 1:
        return str(int(invoerGetal))
    if invoerGetal > 1:
        if invoerGetal%2 == 0:
            return mybin(invoerGetal/2) + "0"
        else:
            return mybin(int(invoerGetal/2)) + "1"

getal = 23450
print("De binaire representatie van ", getal, " is: ",mybin(getal))