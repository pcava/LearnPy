# Pandas Recap
# see also:
# 10 minutes to pandas:
# https://pandas.pydata.org/docs/user_guide/10min.html
# Minimally Sufficient Pandas
# https://www.dunderdata.com/blog/minimally-sufficient-pandas
# 8 Popular SQL Window Functions Replicated In Python
# https://towardsdatascience.com/8-popular-sql-window-functions-replicated-in-python-e17e6b34d5d7


# import
import numpy as np
import pandas as pd
from my_pandas_extensions.database import collect_data
df = collect_data()
df = pd.DataFrame(df)

# python built-in data types
# int, float, bool, str

# data type conversion in python
# use the type prefix eg. str(5)

# python built-in data structures
# list, dict, tuple, set, range

# data structure conversion in python 
# eg1. list(df.columns)
# eg2. df.columns.to_list()

# pandas data types - df.info()
# object, int64, float64, bool, datetime64, timedelta[ns], category

# pandas data structures - type(df)
# array (numpy), Series, DataFrame

# dtype conversion in pandas - https://pbpython.com/pandas_dtypes.html
# In order to convert data types in pandas, there are three basic options:
# A. Use to force an appropriate dtype - eg. df['col'].astype('category') 
# B. Create a custom function to convert the data - 
#   - eg1. df['col'].apply(convert_currency)
#   - eg2. df['colPerc'].apply(lambda x: x.replace('%', '')).astype('float') / 100
#   - eg3. df['col'] = np.where(df['col'] == 'Y', True, False)
# C. Use pandas functions such as to_numeric() or to_datetime() or Categorical()- 
#   - eg1. pd.to_numeric(df['col'], errors='coerce')
#   - eg2. pd.to_datetime(df[['Month', 'Day', 'Year']])
#   - eg3. pd.Categorical(df['category'], categories=..., ordered=True)

# SELECT COLUMNS
# by name:          df[['col1', 'col3']]
# by position:      df.iloc[:, [1,3]]
# by text match:    df.filter(regex='(^col)|(ol[0-9]$)')
# by data type:     df.select_dtypes(include='object')
# by dropping:      df.drop('col2', axis=1)

# FILTER ROWS
# by position:      df.iloc[[1,3,5],-5:]
# simple1:          df[df['order_date'] >= pd.to_datetime("2015-01-01")]
# simple2:          df[df['model'].str.contains("Carbon")]
# query:            var=10; df.query(f"price >= {var}")
# in a list:        df[~df['col1'].isin(['a','b'])]
# top/bottom:       df.nlargest(n = 10, columns='col1')
# sampling:         df.sample(frac = .1, random_state=123)

# ADDING (or REPLACING) COLUMNS
# series notation:  df['new_col'] = df['col1'] * df['col2] - doesn't support chaining
# assign:           df.assign(new_col = lambda x: x['col1'] * x['col2'])

# AGGREGATIONS AND GROUPING
# generic:          df.nunique(); df.isna().sum(); df['col1'].value_counts()
# agg wo/ group:    df.agg([np.sum, np.mean])
# agg w grouping v1:df.groupby('cat').agg([np.sum, np.mean]).reset_index()
# agg w grouping v2:df.groupby('cat').agg(lambda x: np.sum(x['col1'])).reset_index()
# preferred syntax in minimally sufficient pandas - https://www.dunderdata.com/blog/minimally-sufficient-pandas:
# df.groupby('grouping column').agg({'aggregating column': 'aggregating function'})

# TRANSFORMATION AND GROUPING (cannot use groupby + assign)
# resample weekly:  df.set_index('order_date').groupby('cat').resample('W').agg(np.sum).reset_index()
# apply:            df.groupby('cat').apply(lambda x: (x['col1'] - x['col1'].mean()) / x['col1'].std()).reset_index()

# groupby & aggregate (does aggregate) template 
# the function is applied to all elements in each group 
# returns a dataframe with smaller shape vs initial df 
# df \ 
#     .set_index(['date','cat']) \ 
#     .groupby('cat') \ 
#     .agg(lambda x: x.sum) \ 
#     .reset_index() 
     
# groupby & apply (doesn't aggregate) template 
# the function is applied to each element in each group 
# returns a dataframe with same shape as initial df 
# df \ 
#     .set_index(['date','cat']) \ 
#     .groupby('cat') \ 
#     .apply(lambda x: (x - x.mean()) / x.std() ) \ 
#     .reset_index()

# assign vs apply
test_df = pd.DataFrame({'a':[1,2,3],'b':[3,2,1]})
# assign: x refers to the dataframe and support x['col'] 
# cannot be used with groupby
# available as a method for dataframe only
test_df.assign(c=lambda x: type(x))
test_df.assign(c=lambda x: type(x.a))
# apply cycles through each column or element 
# x refers to a single column when applied to a datafreame
# x refers to a single element when applied to a single column (series)
# can be used with groupby
# available as a method for dataframe and series
test_df.apply(lambda x: x - x.mean())
test_df['a'].apply(lambda x: type(x))

# COLUMN RENAMING
test_df = pd.DataFrame({'col1':['A','A','B','B'], 'col2': [2021, 2022, 2021, 2022], 'col3': range(10, 41, 10)})
# specific columns
test_df = test_df.rename(columns={'col1': 'product', 'col2': 'year', 'col3': 'revenue'})
# all columns:
test_df = test_df.rename(columns = lambda x: x.replace("_"," "))

# RESHAPING (MELT & PIVOT)
# from long to wide (prefer the more flexible pivot_table)
test_df_wide = test_df.pivot(index='product', columns='year', values='revenue').reset_index()
# from wide to long: 
test_df_long = test_df_wide.melt(id_vars='product', value_vars=[2021,2022], var_name='year', value_name='revenue')
# excel pivot_table: 
test_df_pivot = test_df.pivot_table(index='product', columns='year', values='revenue', aggfunc=np.sum)
# special case for pivot table: pd.crosstab - https://www.dunderdata.com/blog/minimally-sufficient-pandas
test_df.pivot_table(index='product', columns='year', values='revenue', aggfunc='size') # abs freq
pd.crosstab(index=test_df['product'], columns=test_df['year']) # abs freq
pd.crosstab(index=test_df['product'], columns=test_df['year'], normalize='all') # rel freq
pd.crosstab(index=test_df['product'], columns=test_df['year'], normalize='columns') # rel freq over each col
pd.crosstab(index=test_df['product'], columns=test_df['year'], normalize='index') # rel freq over each row

# STACK & UNSTACK
# Unstack - Pivots Wider 1 Level (Pivot) - move an index to a column
test_df_pivot.unstack(level='product', fill_value=0)
# Stack - Pivots Longer 1 Level (Melt) - move a column to an index
test_df_pivot.stack(level='year')

# JOINING
# merge:        df1.merge(right=df2, how='inner', left_on='col1', right_on='col2')
# concat rows:  pd.concat([df.head(), df.tail()], axis=0)
# concat cols:  pd.concat([df.iloc[:,:5], df.iloc[:,5:]], axis=1)

# SPLITTING & COMBINING COLUMNS
# split:    df[['year', 'month', 'day']] = df['order_date'].astype('str').str.split("-", expand=True)
# combine:  df['order_date'] = df_2['year'] + '-' + df_2['month'] + '-' + df_2['day']
    
# RESETTING MULTI-INDEX
# https://www.dunderdata.com/blog/minimally-sufficient-pandas
# step 1: overwrite column names
df.columns = ['min satmtmid', 'max satmtmid', 'min satvrmid', 'max satvrmid', 'mean ugds']
# step 2: reset_index method to make each index level an actual column.
df.reset_index()

