class myStack( list):

    def push(self,x):
        self.append(x)

    def peek(self,num):
        return self[num]

    def isEmpty(self):
        if len(self) is 0:
            return True
        return False

def isOpenBracket(br):
    if br is '(':
        return True
    elif br is '<':
        return True
    elif br is '[':
        return True
    else:
        return False

def isCloseBracket(br):
    if br is ')':
        return True
    elif br is '>':
        return True
    elif br is ']':
        return True
    else:
        return False

def getCloseBracket(br):
        if br is '(':
            return ')'
        elif br is '<':
            return '>'
        elif br is '[':
            return ']'
        else:
            return br

def bracketsCheck(brackets):
    print('testing: ', brackets)
    stack = myStack()
    for tmp in brackets:
        if isOpenBracket(tmp):
            stack.push(tmp)
        elif isCloseBracket(tmp):
            if getCloseBracket(stack.peek(-1)) == tmp:
                stack.pop()
            else:
                return False

    return stack.isEmpty()


if bracketsCheck('[d(f<f>g)](banana)(( )( ))'):
    print('passed')
else:
    print('failed')