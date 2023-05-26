import pandas as pd
import itertools as iter
import numpy as np

file_loc = r"C:\Users\ADCCYW9\Downloads\Real Test 2.xlsx"
main = pd.read_excel(file_loc)
# Set the index to be this and don't drop
main.set_index(keys = ['Account'], drop = False, inplace = True)
# Prepare input to split accounts
accounts = input('Accounts: ').split(',')
# For each loop you get one account
for i in accounts:
    work = main.loc[main['Account'] == i]
    print(work)

exit()
# Now we can perform a lookup on a 'view' of the dataframe
imp220t = main.loc[main['Accounting Number'] == 'IMP022T']

ac_ex_date = imp220t['Accounting Ex date'].unique().tolist()

print(ac_ex_date, len(ac_ex_date))