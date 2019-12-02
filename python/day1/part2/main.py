def calculateFuel(mass) :
    fuel = int(mass / 3) - 2
    if fuel > 0 :
        return fuel + calculateFuel(fuel)
    return 0
