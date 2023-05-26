import pandas as pd
import itertools as iter
import numpy as np

file_loc = r"C:\Users\ADCCYW9\Downloads\Tax_Reclaim Test.xlsx"
df = pd.read_excel(file_loc, sheet_name = 'Recon Sheet', skiprows = 4)

df['Accounting Reclaim Local'] = -1*df['Accounting Reclaim Local']
print(df['Accounting Reclaim Local'], '\n', '\n')

combos = []
for i in range(2, df['Accounting Reclaim Local'].count() + 1):
    combos.extend(list(iter.combinations(df['Accounting Reclaim Local'], i)))

combo_sums = []
for combo in combos:
    combo_sum = abs(sum(combo))
    combo_sums.append(combo_sum)

combo_sums_sorted, combos_sorted = zip(*sorted(zip(combo_sums, combos)))

for i in range(10):
    print(combos_sorted[i], combo_sums_sorted[i])