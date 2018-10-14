# -*- encoding:utf-8 -*-

import pandas as pd
import numpy as np

df_data = pd.read_csv("cardiac.csv")
df_data.columns = ["bhr", "basebp", "basedp", "pkhr", "sbp", "dp", "dose", "maxhr", "%mphr(b)", "mbp", "dpmaxdo",
                    "dobdose", "age", "gender", "baseEF", "dobEF", "chestpain", "posECG", "equivecg", "restwma",
                    "posSE", "newMI", "newPTCA", "newCABG", "hxofHT", "hxofdm", "hxofcig", "hxofMI",
                    "hxofPTCA", "hxofCABG", "death"]


dic_clean_data = {}
# bhr_series = df_data["bhr"]
dic_clean_data["bhr"] = df_data["bhr"]
# basebp_series = df_data["basebp"]
dic_clean_data["basebp"] = df_data["basebp"]
# basedp_series = df_data["basedp"]
dic_clean_data["basedp"] = df_data["basedp"]
# pkhr_series = df_data["pkhr"]
dic_clean_data["pkhr"] = df_data["pkhr"]
# sbp_series = df_data["sbp"]
dic_clean_data["sbp"] = df_data["sbp"]
# dp_series = df_data["dp"]
dic_clean_data["dp"] = df_data["dp"]
# maxhr_series = df_data["maxhr"]
dic_clean_data["maxhr"] = df_data["maxhr"]
# mphr_b_series = df_data["%mphr(b)"]
dic_clean_data["%mphr(b)"] = df_data["%mphr(b)"]
# mbp_series = df_data["mbp"]
dic_clean_data["mbp"] = df_data["mbp"]
# dpmaxdo_series = df_data["dpmaxdo"]
dic_clean_data["dpmaxdo"] = df_data["dpmaxdo"]
# age_series = df_data["age"]
dic_clean_data["age"] = df_data["age"]
# baseEF_series = df_data["baseEF"]
dic_clean_data["baseEF"] = df_data["baseEF"]
# dobEF_series = df_data["dobEF"]
dic_clean_data["dobEF"] = df_data["dobEF"]

for (k, v) in dic_clean_data.items():
    # max_item = max(v)
    # min_item = min(v)
    temp_ls = []
    for each_data in v:
        if max(v) <= 50:
            if 3 <= each_data % 10 <= 7:
                new_data = each_data//10 * 10 + 5
            elif 7 < each_data % 10 <= 9:
                new_data = each_data//10 * 10 + 10
            elif 1 <= each_data % 10 < 3:
                new_data = each_data // 10 * 10
            else:
                new_data = each_data
            temp_ls.append(new_data)
        elif 50 < max(v) <= 100:
            if 1 <= each_data % 10 <= 4:
                new_data = each_data//10 * 10
            elif 5 <= each_data % 10 <= 9:
                new_data = each_data//10 * 10 + 10
            else:
                new_data = each_data
            temp_ls.append(new_data)
        else:
            if each_data < 100:
                if 1 <= each_data % 10 <= 4:
                    new_data = each_data // 10 * 10
                elif 5 <= each_data % 10 <= 9:
                    new_data = each_data // 10 * 10 + 10
                else:
                    new_data = each_data
                temp_ls.append(new_data)
            else:
                num_len = len(str(each_data))
                new_data = (each_data//np.power(10, num_len-2)) * np.power(10, num_len-2)
                temp_ls.append(new_data)
    df_data[k] = temp_ls

df_data.to_csv("nor_data1.csv")    # normalization data
