import main

def assertEquals(testId, expected, actual):
    if expected == actual:
        print(str(testId) + " - pass")
    else:
        print(str(testId) + " - FAIL - expecting " + str(expected) + " but got " + str(actual))

assertEquals(1, 2, main.calculateFuel(12));
assertEquals(1, 966, main.calculateFuel(1969));
assertEquals(1, 50346, main.calculateFuel(100756));

f = open("python/day1/puzzle.txt", "r")
totalFuel = 0
for line in f:
   totalFuel += main.calculateFuel(int(line))

print("answer is " + str(totalFuel))
