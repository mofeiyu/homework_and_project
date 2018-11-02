# -*- encoding:utf-8 -*-
# Name: SUN RUI    ID: 18083229g

import pandas as pd

df_data = pd.read_csv("nor_data1.csv")
df_data.columns = ["bhr", "basebp", "basedp", "pkhr", "sbp", "dp", "dose", "maxhr", "%mphr(b)", "mbp", "dpmaxdo",
                    "dobdose", "age", "gender", "baseEF", "dobEF", "chestpain", "posECG", "equivecg", "restwma",
                    "posSE", "newMI", "newPTCA", "newCABG", "hxofHT", "hxofdm", "hxofcig", "hxofMI",
                    "hxofPTCA", "hxofCABG", "death"]
count = 0
for col in df_data.columns:
    count += 1
    print(df_data[col].value_counts())
print(count)