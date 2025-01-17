total_pop = 80000

# men and women
tot_men = total_pop * 52 / 100
tot_wom = total_pop - tot_men

# (literate) men and women
tot_lit_peo = total_pop * 48 / 100
tot_lit_men = total_pop * 35 / 100
tot_lit_wom = tot_lit_peo - tot_lit_men

# (illiterate) men and women
tot_illit_men = tot_men - tot_lit_men
tot_illit_wom = tot_wom - tot_lit_wom

print(f"Total Illiterate Men: {tot_illit_men:.0f}")
print(f"Total Illiterate Women: {tot_illit_wom:.0f}")
