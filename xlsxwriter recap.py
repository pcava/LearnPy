# https://xlsxwriter.readthedocs.io/

# WARNING: XlsxWriter cannot read or modify existing Excel XLSX files!!!
# Use OpenPyXL - example at the end of the OpenPyXL.px file
# or pywin32 - https://pbpython.com/windows-com.html


# Getting Started
# https://xlsxwriter.readthedocs.io/getting_started.html

import xlsxwriter

workbook = xlsxwriter.Workbook('Output/hello.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()

# Tutorial 1: Create a simple XLSX file
# https://xlsxwriter.readthedocs.io/tutorial01.html#tutorial1

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Output/Expenses01.xlsx')
worksheet = workbook.add_worksheet()

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()


# Tutorial 2: Adding formatting to the XLSX File
# https://xlsxwriter.readthedocs.io/tutorial02.html

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Output/Expenses02.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

# Add a number format for cells with money.
money = workbook.add_format({'num_format': '$#,##0'})

# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Cost', bold)

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

# Start from the first cell below the headers.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item, cost in (expenses):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost, money)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total',       bold)
worksheet.write(row, 1, '=SUM(B2:B5)', money)

workbook.close()
 
 
# Tutorial 3: Writing different types of data to the XLSX File
# https://xlsxwriter.readthedocs.io/tutorial03.html
 
from datetime import datetime
import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Output/Expenses03.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Add a number format for cells with money.
money_format = workbook.add_format({'num_format': '$#,##0'})

# Add an Excel date format.
date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

# Adjust the column width.
worksheet.set_column(1, 1, 15)

# Write some data headers.
worksheet.write('A1', 'Item', bold)
worksheet.write('B1', 'Date', bold)
worksheet.write('C1', 'Cost', bold)

# Some data we want to write to the worksheet.
expenses = (
    ['Rent', '2013-01-13', 1000],
    ['Gas',  '2013-01-14',  100],
    ['Food', '2013-01-16',  300],
    ['Gym',  '2013-01-20',   50],
)

# Start from the first cell below the headers.
row = 1
col = 0

for item, date_str, cost in (expenses):
    # Convert the date string into a datetime object.
    date = datetime.strptime(date_str, "%Y-%m-%d")

    worksheet.write_string  (row, col,     item              )
    worksheet.write_datetime(row, col + 1, date, date_format )
    worksheet.write_number  (row, col + 2, cost, money_format)
    row += 1

# Write a total using a formula.
worksheet.write(row, 0, 'Total', bold)
worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

workbook.close()

 
# Working with Pandas and XlsxWriter
# https://xlsxwriter.readthedocs.io/working_with_pandas.html

# Accessing XlsxWriter from Pandas
import pandas as pd
import xlsxwriter

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('Output/pandas_simple.xlsx', engine='xlsxwriter')

# Adding an autofilter to a Dataframe output
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook  = writer.book
worksheet = writer.sheets['Sheet1']
(max_row, max_col) = df.shape
worksheet.autofilter(0, 0, max_row, max_col - 1)
worksheet.filter_column(0, 'Data == 20')
for row_num in (df.index[(df['Data'] != 20)].tolist()):
    worksheet.set_row(row_num + 1, options={'hidden': True})

# Close the Pandas Excel writer and output the Excel file.
writer.close()

# Pandas with XlsxWriter Examples
# https://xlsxwriter.readthedocs.io/pandas_examples.html


# using 'with' - no need to close the writer
df = pd.DataFrame({'DataA': [10, 20, 30, 20, 15, 30, 45],
                   'DataB': [100, 200, 300, 200, 150, 300, 450]})
with pd.ExcelWriter("Output/pandas_simple.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)

