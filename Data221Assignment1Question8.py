# Pandas DataFrame with Computed Column
import pandas as pd

# Column Data provided in the question
columnDataDictionary = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210 ]
}

# Create the DataFrame from the dictionary
dataFrameDerivedFromColumns = pd.DataFrame(columnDataDictionary)

# Add a new computed column derived from existing columns (example: A * B)
dataFrameDerivedFromColumns["A_times_B"] = dataFrameDerivedFromColumns["A"] * dataFrameDerivedFromColumns["B"]

# Print final DatafFrame
print(dataFrameDerivedFromColumns)