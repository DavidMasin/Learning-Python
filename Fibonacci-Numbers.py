if __name__ == '__main__':
    firstNumber = 0
    rememberNumber = 0
    while True:
        if firstNumber+rememberNumber>10000:
            break
        print(firstNumber+rememberNumber)
        if firstNumber==0:
            firstNumber = 1
            print(firstNumber)
            print(firstNumber)
        firstNumber+=rememberNumber
        rememberNumber=firstNumber-rememberNumber

