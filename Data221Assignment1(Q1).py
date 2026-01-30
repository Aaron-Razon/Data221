# Controlled Multiplication Loop
# Multiply consecutive integers (1 * 2 * 3 * ...) until the product is greater than a threshold.

thresholdValue = 100          # The value we want the product to exceed
runningProduct = 1            # Starts at 1 because multiplying by 1 changes nothing
currentMultiplier = 1         # Tracks the most recent integer used in the product

# Keep multiplying by the next integer until the product becomes greater than the threshold
while runningProduct <= thresholdValue:
    currentMultiplier += 1            # Move to the next integer (2, 3, 4, ...)
    runningProduct *= currentMultiplier

# Output the results
print("Final product:", runningProduct)
print("Integer that caused it to exceed the threshold:", currentMultiplier)
