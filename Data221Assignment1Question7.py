# Time Conversion Function

def convertSecondsSinceMidnight(secondsSinceMidnight):
    """
     Converts seconds since midnight into: hours minutes seconds AM/PM
     Returns a string like: "5 17 47 AM"
     """

    # Basic validation (0 to 86399 seconds in a day).
    if type(secondsSinceMidnight) != int or secondsSinceMidnight < 0 or secondsSinceMidnight > 86399:
        return "Invalid input: seconds must be an integer from 0 to 86399."

    # Break total seconds into hours, minutes, seconds
    twentyFourHourFormat = secondsSinceMidnight // 3600
    remainingSeconds = secondsSinceMidnight % 3600
    minutesValue = remainingSeconds // 60
    secondsValue = remainingSeconds % 60

    # Decide whether it is  AM or PM
    amOrPmText = "AM" if twentyFourHourFormat < 12 else "PM"

    # Convert to 12-hour clock (0 becomes 12)
    twelveHourFormat = twentyFourHourFormat % 12
    if twelveHourFormat == 0:
        twelveHourFormat = 12

    return f"{twelveHourFormat} {minutesValue} {secondsValue} {amOrPmText}"
"""
I used Google to search up what 5:17:47 AM would be converted into seconds - 
which turns out to be 19,067 seconds
"""
# Example Test Cases
print(convertSecondsSinceMidnight(19067)) # Expected Output: 5 17 47 AM
print(convertSecondsSinceMidnight(76667)) # Expected Output: 9 17 47 PM
print(convertSecondsSinceMidnight(33467)) # Expected Output: 9 17 47 AM
print(convertSecondsSinceMidnight(-1))
