import pandas as pd
import itertools as iter
import numpy as np

file_loc = r"C:\Users\ADCCYW9\Downloads\Tax_Reclaim Test.xlsx"
main = pd.read_excel(file_loc, sheet_name = 'Recon Sheet', skiprows = 4)

# Set the index to be this and don't drop
main.set_index(keys = ['Accounting Number'], drop = False, inplace = True)

# Now we can perform a lookup on a 'view' of the dataframe
imp220t = main.loc[main['Accounting Number'] == 'IMP022T']

ac_ex_date = imp220t['Accounting Ex date'].unique().tolist()

print(ac_ex_date, len(ac_ex_date))