def hasNeverDecreasingDigits(number):
    hasNeverDecreasingDigits = True
    previousDigit = 1
    for character in str(number):
        digit = int(character)
        if digit < previousDigit:
            hasNeverDecreasingDigits = False
        previousDigit = digit

    return hasNeverDecreasingDigits


def hasDoubleDigit(number):
    hasDoubleDigit = False
    numberString = str(number)
    previousDigit = int(numberString[0:1])
    for index in range(1,6):
        digit = int(numberString[index:index+1])
        if digit == previousDigit:
            hasDoubleDigit = True
        previousDigit = digit

    return hasDoubleDigit