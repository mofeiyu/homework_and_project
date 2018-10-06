# -*- encoding:utf-8 -*-

import pandas as pd
import numpy as np

df_data = pd.read_csv("normalization_data.csv")
df_data.columns = ["bhr", "basebp", "basedp", "pkhr", "sbp", "dp", "dose", "maxhr", "%mphr(b)", "mbp", "dpmaxdo",
                    "dobdose", "age", "gender", "baseEF", "dobEF", "chestpain", "posECG", "equivecg", "restwma",
                    "posSE", "newMI", "newPTCA", "newCABG", "hxofHT", "hxofdm", "hxofcig", "hxofMI",
                    "hxofPTCA", "hxofCABG", "death"]
count = 0
for col in df_data.columns:
    count += 1
    print(df_data[col].value_counts())
print(count)