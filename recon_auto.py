import pandas as pd
import itertools
# find a way to connect it to Excel sheets
# can use functions to identify strings and assign them
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
Same value date
CSV, PANDA

