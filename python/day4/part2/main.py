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
    matchingDigitCount = 1
    for index in range(1,6):
        digit = int(numberString[index:index+1])
        if digit == previousDigit:
            matchingDigitCount += 1
        else:
            if matchingDigitCount == 2:
                hasDoubleDigit = True
            matchingDigitCount = 1

        previousDigit = digit

    if matchingDigitCount == 2:
        hasDoubleDigit = True

    return hasDoubleDigit