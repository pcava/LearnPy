# Progress Bar
import pandas as pd
from tqdm import tqdm

df = pd.DataFrame({'a': [1,2,3],
                   'b': [4,5,6]})

for col in tqdm(df.columns):
    col.capitalize()

