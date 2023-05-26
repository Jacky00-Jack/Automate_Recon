import pandas as pd
import itertools as iter
import numpy as np

file_loc = r"C:\Users\ADCCYW9\Downloads\Test P.xlsx"
main = pd.read_excel(file_loc)

main.set_index(keys = ['Set'], drop = False, inplace = True)
accounts = main['Set'].unique().tolist()
for i in accounts:
    work = main.loc[main['Set'] == i].copy()
    work['Amount'] = np.where(work['Item Type'].str.contains('S CR'),-1*work['Amount'], np.where(work['Item Type'].str.contains('L DR'),-1*work['Amount'],work['Amount']))
    isin = work['Ref 1'].unique().tolist()
    output = []
    for i in isin:
        work_isin = work.loc[work['Ref 1'] == i]
        for i in range(2, work_isin['Amount'].count() + 1):
            combos = iter.combinations(work_isin['Amount'], i)
            for combo in combos:
                combo_sum = abs(sum(combo))
                if combo_sum <= 5:
                    output.append(combo)
    print(output)
exit()
combo_sums_sorted, combos_sorted = zip(*sorted(zip(combo_sums, combos)))
for i in range(10):
    combination = pd.DataFrame(combos_sorted[i])
    for j in range(combination[0].count()):
        z = work[work['Amount'] == combination.iat[j, 0]]
        for item_id in z['Item ID']:
            print(z[['Amount', 'Item ID']])
    print('Outstanding: ', combo_sums_sorted[i])
