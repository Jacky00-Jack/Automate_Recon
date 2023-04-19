import pandas as pd
import itertools as iter
import numpy as np
# find a way to connect it to Excel sheets
# Use panda to import Excel, but how to make it dynamic (User friendly)
# Use the zip function to tie the item ID to the formula used
df = pd.read_csv(r"C:\Users\ADCCYW9\Downloads\Book1.csv")
# Use this expression to remove ','
df['Amount'] = df['Amount'].str.replace(',', '')
df['Amount'] = df['Amount'].astype(float)

# String cant convert to float when there are special characters
# Filter the Type and then apply function on the Corresponding Value
df['Amount'] = np.where(df['Item Type'].str.contains('S CR'),-1*df['Amount'], np.where(df['Item Type'].str.contains('L DR'),-1*df['Amount'],df['Amount']))
print(df, '\n', '\n')

# the 2 in range ignores singles
combos = []
for i in range(2, df['Amount'].count() + 1):
    combos.extend(list(iter.combinations(df['Amount'], i)))

# abs() to make it ascending in regard to 0
combo_sums = []
for combo in combos:
    combo_sum = abs(sum(combo))
    combo_sums.append(combo_sum)

combo_sums_sorted, combos_sorted = zip(*sorted(zip(combo_sums, combos)))
# Change len(combo_sums_sorted) to an x to print top x result
for i in range(10):
    print(combos_sorted[i], combo_sums_sorted[i])
# Same value date
# CSV, PANDA
# Feed data into this from TLM
# Know python's potential
# Understand TLM completely
# Write off
