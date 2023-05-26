import pandas as pd
import itertools as iter
import numpy as np

file_loc = r"C:\Users\ADCCYW9\Downloads\Tax_Reclaim Test.xlsx"
main = pd.read_excel(file_loc, sheet_name = 'Recon Sheet', skiprows = 4)
main_filt = main[~main['Break Type'].isin(['Perfect Match', 'Match', 'Match but Ex date differs'])]
main_filt.set_index(keys = ['Accounting Number'], drop = False, inplace = True)
accounts = main_filt['Accounting Number'].unique().tolist()
for i in accounts:
    work = main_filt.loc[main_filt['Accounting Number'] == i].copy()
    isin = work['ISIN'].unique().tolist()
    for j in isin:
        combo_output = []
        work_isin = work.loc[work['ISIN'] == j].copy()
        for k in range(2, work_isin['Difference in Reclaim (USD)'].count() + 1):
            combos = iter.combinations(work_isin['Difference in Reclaim (USD)'], k)
            for combo in combos:
                combo_sum = abs(sum(combo))
                if combo_sum <= 5:
                    work_isin = work_isin[work_isin['Difference in Reclaim (USD)'].isin(combo) == False]
                    combo_output.append(combo)
        if len(combo_output) != 0:
            print(j, i, '\n', combo_output)
exit()
for i in i:    
    work['Amount'] = np.where(work['Item Type'].str.contains('S CR'),-1*work['Amount'], np.where(work['Item Type'].str.contains('L DR'),-1*work['Amount'],work['Amount']))
    isin = work['ISIN'].unique().tolist()
    output = []
    for i in isin:
        work_isin = work.loc[work['ISIN'] == i]
        for i in range(2, work_isin['Amount'].count() + 1):
            combos = iter.combinations(work_isin['Amount'], i)
            for combo in combos:
                combo_sum = abs(sum(combo))
                if combo_sum <= 5:
                    output.append(combo)
    print(output)
exit()