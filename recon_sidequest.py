import itertools as iter
import pandas as pd

df = pd.read_csv(r"C:\Users\ADCCYW9\Downloads\Real Test side quest.csv")

df['Net Amount Local'] = df['Net Amount Local'].str.replace(',', '')
df['Net Amount Local'] = df['Net Amount Local'].astype(float)

combos = []
for i in range(2, 4):
    combos.extend(list(iter.combinations(df['Net Amount Local'], i)))
# abs() to make it ascending in regard to 0
combo_sums = []
want = float(input('Look for?  '))
for combo in combos:
    combo_sum = abs(sum(combo))
    if combo_sum == want:
        print(combo)
exit()
combo_sums_sorted, combos_sorted = zip(*sorted(zip(combo_sums, combos)))
# Change len(combo_sums_sorted) to an x to print top x result
for i in range(10):
    if combo_sums == want:
        print(combos_sorted[i], combo_sums_sorted[i])

print('hello')