# import
import tabula as tb
import pdfquery
import PyPDF2
import pandas as pd
import requests
import re
import os


# Download the PDF
url = "https://www.efginternational.com/doc/jcr:9c2ac032-8617-4b71-a226-88771badcb6d/EFGI%202022%20Full_Year_Report_EN.pdf/lang:en/EFGI%202022%20Full_Year_Report_EN.pdf"
response = requests.get(url)
with open("report.pdf", "wb") as pdf_file:
    pdf_file.write(response.content)


# https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-fe2dc96b1e68
# tabula-py
file = "https://www.efginternational.com/doc/jcr:9c2ac032-8617-4b71-a226-88771badcb6d/EFGI%202022%20Full_Year_Report_EN.pdf/lang:en/EFGI%202022%20Full_Year_Report_EN.pdf"
df = tb.read_pdf(file, pages = '88')
df[0]
# doesn't work

file = 'report.pdf'
df = tb.read_pdf(file, pages = '88')
df[0]
# doesn't work

# area (top,left,bottom,right)
df1 = tb.read_pdf(file, area = (150, 40, 550, 550), pages = '88')
df1[0]
# ok

df2 = tb.read_pdf(file, lattice=True, pages='88', area=(150, 40, 550, 550))
df2[0]
# doesn't work

df3 = tb.read_pdf(file, stream=True, pages='88', area=(150, 40, 550, 550))
df3[0]
# ok - same as df1[0]

df4 = tb.read_pdf(file, pages = '88')
df4[0]
# doesn't work

## pro of tabula-py: well formatted pandas df
## con of tabula-py: you need to know the exact page and area of the table - in case it changes from one year to another you need to check and change it manually, not very automated!


# https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-and-pdfquery-d033721c3b28
# PDFQuery - method 1 using TextBox Coordinates
pdf = pdfquery.PDFQuery(file)
pagecount = pdf.doc.catalog['Pages'].resolve()['Count']
pdf.load() # pdf.load(list(range(50,100)))
pdf.tree.write('pdfXML.txt', pretty_print = True)
# [435.9, 467.335, 464.115, 475.315] - cons: you must check the txt file to find the bbox position
operating_income1 = pdf.pq('LTPage[pageid="88"] LTTextLineHorizontal:overlaps_bbox("435.9, 467.335, 464.115, 475.315")').text()
operating_income1

# https://towardsdatascience.com/scrape-data-from-pdf-files-using-python-and-pdfquery-d033721c3b28
# PDFQuery - method 2 using Neighboring Keywords
keyword =  pdf.pq('LTPage[pageid="88"] LTTextLineHorizontal:contains("{}")'.format("Operating income"))[0] 
x0 = float(keyword.get('x0',0)) + 370
y0 = float(keyword.get('y0',0))
x1 = float(keyword.get('x1',0)) + 350
y1 = float(keyword.get('y1',0))
operating_income2 = pdf.pq('LTPage[pageid="88"] LTTextLineHorizontal:overlaps_bbox("%s, %s, %s, %s")' % (x0, y0, x1, y1)).text()
operating_income2

# https://github.com/jcushman/pdfquery
label = pdf.pq('LTPage[pageid="88"] LTTextLineHorizontal:contains("Operating income")')
left_corner = float(label.attr('x0'))
bottom_corner = float(label.attr('y0'))
operating_income3 = pdf.pq('LTPage[pageid="88"] LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (left_corner + 370, bottom_corner, left_corner + 450, bottom_corner+10)).text()
operating_income3

label = pdf.pq('LTTextLineHorizontal:contains("Consolidated income statement for the year")')
pageid = float(label.attr('pageid'))
# doesn't work


# ChatGPT and PDFQuery
# Open the PDF with pdfquery
pdf = pdfquery.PDFQuery("report.pdf")
pdf.load()

# Use XPath to find and extract the value of operating income
operating_income_value = pdf.extract([
    ('with_formatter', 'text'),
    ('operating_income_value', 'LTTextLineHorizontal:contains("Operating income")')
])

# Print the result
if 'operating_income_value' in operating_income_value:
    print("Operating Income Value:", operating_income_value['operating_income_value'])
else:
    print("Operating Income Value not found.")

# Use XPath to find and extract the value of operating income
operating_income_value = pdf.extract([
    ('with_parent', 'LTPage[pageid="88"]'),
    ('with_formatter', 'text'),
    ('operating_income_value', 'LTTextLineHorizontal:in_bbox("435.9, 467.335, 464.115, 475.315")')
])

# Print the result
if 'operating_income_value' in operating_income_value:
    print("Operating Income Value:", operating_income_value['operating_income_value'])
else:
    print("Operating Income Value not found.")
    
    
# ChatGPT and PyPDF2
# Open the PDF and read text
with open("report.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Assuming page 88 is the relevant page
    # page_88_text = pdf_reader.getPage(87).extract_text()
    page_88_text = pdf_reader.pages[87].extract_text()

# Search for operating income in the text using a regular expression
operating_income_match = re.search(r'Operating income\s*([\d,\.]+)', page_88_text)

# Extract and print the operating income value
if operating_income_match:
    operating_income_value = operating_income_match.group(1)
    print("Operating Income Value:", operating_income_value)
else:
    print("Operating Income not found on page 88.")


# ChatGPT and PyPDF2 with keyword2page search
def find_keyword_page(pdf_path, keyword):
    page = []
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page_text = pdf_reader.pages[page_num].extract_text()
            if keyword in page_text:
                page.append(page_num)
                # return page_num

    if len(page) > 1:
        print("Warning: keyword present in multiple pages")
        return None
    else:
        return page[0]

keyword_to_find = "Consolidated income statement for the year \nended"
page_number = find_keyword_page("report.pdf", keyword_to_find)

# Open the PDF and read text
with open("report.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Assuming page 88 is the relevant page
    # page_88_text = pdf_reader.getPage(87).extract_text()
    page_text = pdf_reader.pages[page_number].extract_text()

# Search for operating income in the text using a regular expression
operating_income_match = re.search(r'Operating income\s*([\d,\.]+)', page_text)

# Extract and print the operating income value
if operating_income_match:
    operating_income_value = operating_income_match.group(1)
    print("Operating Income Value:", float(operating_income_value.replace(',','')))
else:
    print("Operating Income not found.")

# Remove the downloaded pdf report
os.remove("report.pdf")
