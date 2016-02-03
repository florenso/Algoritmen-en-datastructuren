def getNumbers(s):
    # s.replace('abcdefghijklmnopqrstuvwxyz'," ")
    # s.join([i for i in s if not i.isdigit()])
    # print(' '.join([i for i in s if  i.isdigit()]))
    for i in s:
        if not i.isdigit():
            s = s.replace(i , ' ')
            s = s.replace('  ' , ' ')
    print(s)
    return [int(s) for s in s.split()]


print(getNumbers("een 123 zin 45 6met-632meerdere+7777getallen"))
