# RECAP:
# - xlswriter is the fastest but can only create excel files - cannot read nor modify
# - openpyxl is slower but can also read and modify existing excel files
# - xlwings/pywin32 is the slowest but most complete in terms of functionalities - requires installed excel
# While XlsxWriter/OpenPyXL are the best choice if you need to produce reports in a scalable way on your Linux web server, 
# xlwings does have the advantage that it can edit pre-formatted Excel files without losing or destroying anything.
# In a nutsheel:
# - xlswriter might be better if you need to *create* new excel files from scratch
# - openpyxl might be better if you need to *read* existing excel files and import data only
# - xlwings might be better if you need to *modify* existing excel file (eg. add data)

# https://docs.xlwings.org/en/latest/
# see also the more detailed API Reference: https://docs.xlwings.org/en/latest/api/index.html

# Makes it easy to call Python from Excel and vice versa:
# - Scripting: Automate/interact with Excel from Python using a syntax close to VBA.
# - Macros: Replace VBA macros with clean and powerful Python code.
# - UDFs: Write User Defined Functions (UDFs) in Python (Windows only).
# Numpy arrays and Pandas Series/DataFrames are fully supported. 
# xlwings-powered workbooks are easy to distribute and work on Windows and Mac.
# In essence, xlwings is just a smart wrapper around pywin32 on Windows.

import xlwings as xw

# CREATE A NEW BOOK #
# https://docs.xlwings.org/en/latest/quickstart.html
wb = xw.Book()  # this will open a new workbook
sheet = wb.sheets['Sheet1'] # instantiate a sheet object

# Reading/writing values to/from ranges is as easy as:
sheet['A1'].value = 'Foo 1'
sheet['A1'].value

# Convenience features available, e.g. Range expanding:
sheet['A1'].value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
sheet['A1'].expand().value

# Converters handle most data types of interest, including Pandas DataFrames in both directions:
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sheet['A1'].value = df
sheet['A1'].options(pd.DataFrame, expand='table').value

# Matplotlib figures can be shown as pictures in Excel:
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sheet.pictures.add(fig, name='MyPlot', update=True)


# OPEN AN EXISTING BOOK AND ADD DATA #
# https://docs.xlwings.org/en/latest/connect_to_workbook.html
import xlwings as xw
import pandas as pd
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])

with xw.App(visible=False) as app:
    wb = xw.Book(r'Input\Test_xlwings.xlsx')
    last_sheet = wb.sheets.count
    wb.sheets.add(after=last_sheet)
    sheet = wb.sheets[last_sheet]
    sheet['A1'].options(pd.DataFrame, index=False, chunksize=10000).value = df
    wb.save()


# READ FROM AN EXISTING BOOK #
# https://docs.xlwings.org/en/latest/connect_to_workbook.html
import xlwings as xw
import pandas as pd

with xw.App(visible=False) as app:
    wb = xw.Book(r'Input\Test_xlwings.xlsx')
    last_sheet = wb.sheets.count - 1
    sheet = wb.sheets[last_sheet]
    # As DataFrame
    df2 = sheet['A1'].expand().options(pd.DataFrame, chunksize=10000).value
    df2.reset_index(inplace=True)
    # As list of list
    l = sheet['A1'].expand().options(chunksize=10000).value


