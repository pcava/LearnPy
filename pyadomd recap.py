# https://pypi.org/project/pyadomd/
# https://pyadomd.readthedocs.io/en/latest/index.html
# https://github.com/Andboye/Pyadomd
# https://allentseng92.medium.com/querying-a-ssas-tabular-model-using-r-or-python-1edf46b25c63


# Working Example to query SSAS Multidim or Tabular cubes

# Installation
# pip install pyadomd

# Import packages
from sys import path
path.append('C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')
from pyadomd import Pyadomd

# Build connection string
conn_str = 'Provider=MSOLAP;Data Source=DESKTOP-6E2P52R;Catalog=AWDW2019Multidimensional-SE;'

# Enter DAX or MDX query
# query = """Your DAX or MDX query here"""
query = """
        SELECT
        [Measures].[Internet Sales Amount] ON COLUMNS,
        NON EMPTY [Product].[Product Categories].[Category] ON ROWS
        FROM [Adventure Works]
        """

# with Pyadomd(conn_str) as conn:
#     with conn.cursor().execute(query) as cur:
#         print(cur.fetchall())
        
# Integrates easily with pandas
import pandas as pd

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        df = pd.DataFrame(cur.fetchone(),
        columns=[i.name for i in cur.description])

df

# Rename Columns
df.rename(columns={'[Product].[Product Categories].[Category].[MEMBER_CAPTION]':'Category',
                   '[Measures].[Internet Sales Amount]':'Internet Sales Amount'},
          inplace = True)

df.head()
