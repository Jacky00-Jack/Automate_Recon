import pandas as pd
import itertools
# find a way to connect it to Excel sheets
# Use panda to import Excel, but how to make it dynamic (User friendly)
# Use the zip function to tie the item ID to the formula used
df = pd.read_csv(r"C:\Users\ADCCYW9\Downloads\Test.csv")
print(df)
df1 = df.query('Type.str.contains("S CR")')
df2 = df.query('Type.str.contains("L DR")')
df_c = pd.concat([df1,df2])
print(df1)
print(df2)
print(df_c)

exit()
l_cr = [float(x) for x in input("L_CR: ").split(" ")]
l_dr = [float(x) for x in input("L_DR: ").split(" ")]
s_cr = [float(x) for x in input("S_CR: ").split(" ")]
s_dr = [float(x) for x in input("S_DR: ").split(" ")]

for i in range(len(l_dr)):
    l_dr[i] = -l_dr[i]
for i in range(len(s_cr)):
    s_cr[i] = -s_cr[i]

main_list = list(l_cr + l_dr + s_cr + s_dr)
# the 2 in range ignores singles
combos = []
for i in range(2, len(main_list)+1):
    combos.extend(list(itertools.combinations(main_list, i)))
# abs() to make it ascending in regard to 0
combo_sums = []
for combo in combos:
    combo_sum = abs(sum(combo))
    combo_sums.append(combo_sum)
combo_sums_sorted, combos_sorted = zip(*sorted(zip(combo_sums, combos)))
for i in range(len(combo_sums_sorted)):
    print(combos_sorted[i], combo_sums_sorted[i])
# Same value date
# CSV, PANDA
# Feed data into this from TLM
# Know python's potential
# Understand TLM completely
# Write off
# 
