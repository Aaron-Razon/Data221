# Safe Function Application: Compute Powers x^y

def computePowerForBaseXAndExponentY(baseValue, exponentValue):

    # Returns baseValue raised to the power of exponentValue (baseValue ** exponentValue).

    return baseValue ** exponentValue


pairsList = [[5, 2], [3, -1], [4, 3], [2, 0]]
powerResultsList = []

# Use a for loop with unpacking: each item becomes baseValue and exponentValue
for baseValue, exponentValue in pairsList:

    # Skip pairs where the exponent is negative
    if exponentValue < 0:
        continue

    # Compute and store valid results
    powerResult = computePowerForBaseXAndExponentY(baseValue, exponentValue)
    powerResultsList.append(powerResult)

print(powerResultsList)
