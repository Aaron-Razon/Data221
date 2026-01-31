def buildNestedDictionaryFromStringInfo(listOfStrings):
    """
    Receives a list of strings and returns a dictionary where:
    - each key is a string from the list
    - each value is a dictionary with the string's length and whether that length is even or odd
    """
    nestedStringInfoDictionary = {}

    for currentWord in listOfStrings:
        wordLength = len(currentWord)

        # Decide if the length is even or odd
        if wordLength % 2 == 0:
            lengthParityText = "even"
        else:
            lengthParityText = "odd"

        # Store the info in the required nested dictionary format
        nestedStringInfoDictionary[currentWord] = {
            "length": wordLength,
            "parity": lengthParityText
        }

    return nestedStringInfoDictionary


# Example usage
wordsList = ["data", "science"]
resultDictionary = buildNestedDictionaryFromStringInfo(wordsList)

# Print in the exact format shown in the screenshot
print("{")

dictionaryKeyList = list(resultDictionary.keys())

for keyIndexNumber in range(len(dictionaryKeyList)):
    currentKeyString = dictionaryKeyList[keyIndexNumber]
    innerInfoDictionary = resultDictionary[currentKeyString]

    wordLength = innerInfoDictionary["length"]
    lengthParityText = innerInfoDictionary["parity"]

    # Add a comma after each line except the last one
    commaCharacter = "," if keyIndexNumber < len(dictionaryKeyList) - 1 else ""

    print(f'  "{currentKeyString}": {{"length": {wordLength}, "parity": "{lengthParityText}"}}{commaCharacter}')

print("}")
