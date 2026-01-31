# Circle Area Comparison with Validation

# Write a function that takes the two radii of two circles and performs the following:
# - Validates both radii are positive integers
# - Computes the area of the circle
# - Returns the percentage of the larger circle's area that can be covered by the smaller circle

import math

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    # Validate input: both radii must be positive integers

    # Create an empty for error messages
    # So that if a radius is a negative non-integer, it prints both messages

    errorMessageText = ""

    # Check if radii are positive
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        errorMessageText += "Invalid input: both radii must be integers. "
    # Check if radii are integers
    if type(radiusOfCircle1) != int or  type(radiusOfCircle2) != int:
        errorMessageText += "Invalid input: both radii must be positive."

    # If any errors occur, return them
    if errorMessageText != "":
        return errorMessageText.strip()

    # Compute each circle's area (A = pi * r^2)
    areaOfCircle1 = math.pi * radiusOfCircle1 ** 2
    areaOfCircle2 = math.pi * radiusOfCircle2 ** 2

    # Find smaller and larger area
    smallerCircleArea = min(areaOfCircle1, areaOfCircle2)
    largerCircleArea = max(areaOfCircle1, areaOfCircle2)

    # Compute coverage percentage
    percentOfLargerCircleAreaCoveredBySmallerCircle = (smallerCircleArea / largerCircleArea) * 100
    return (f"{percentOfLargerCircleAreaCoveredBySmallerCircle:.2f}%")

# Test Cases:
print(circleAreaCoverage(3, 5)) # Valid: returns 36.0
print(circleAreaCoverage(-3, 5)) # Invalid: negative radius
print(circleAreaCoverage(3.5,5)) # Invalid: non-integer radius
print(circleAreaCoverage(-3.5,5)) # Invalid: non-integer AND negative

