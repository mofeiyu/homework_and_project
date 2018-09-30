# -*- coding:utf-8 -*-

import util

# clean_attribute = util.Clean("train_data/attributes_train_data", "train_pickle/attributes_train_data.pickle",
#                              "attribute")
# clean_attribute.pickle_data()

# info = clean_attribute.extract_pickle_data()

# print(info)
# print(len(info))

clean_case = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")
# clean_case.pickle_data()
#
info = clean_case.extract_pickle_data()
#
# print(info)
# print("10001" in info)
# print(len(info))

# fre_dict = clean_case.load_data(info)
# print(fre_dict)


for k, v in info.items():
    o_length = len(v)
    n_length = len(set(v))
    if o_length != n_length:
        print(o_length, n_length)
        print(info[k])


