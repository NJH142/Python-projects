
##import pandas 
##
##https://www.datacamp.com/community/tutorials/python-excel-tutorial

# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'SampleData.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)
##
### Load a sheet into a DataFrame by name: df1
##df1 = xl.parse('Sheet1')
