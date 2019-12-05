import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))


assertEquals("1", True, main.hasNeverDecreasingDigits("123456"))
assertEquals("2", False, main.hasNeverDecreasingDigits("123454"))
assertEquals("3", False, main.hasNeverDecreasingDigits("121456"))
assertEquals("4", True, main.hasNeverDecreasingDigits("222222"))


assertEquals("5", True, main.hasDoubleDigit("222222"))
assertEquals("6", False, main.hasDoubleDigit("123456"))
assertEquals("7", True, main.hasDoubleDigit("124456"))
assertEquals("8", True, main.hasDoubleDigit("113456"))
assertEquals("9", True, main.hasDoubleDigit("123466"))

total = 0
for number in range(359282, 820401+1):
    if main.hasNeverDecreasingDigits(number):
        if main.hasDoubleDigit(number):
            total += 1

print("the answer is " + str(total))