# -*- coding:utf-8 -*-

import util


clean_case = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")

info = clean_case.extract_pickle_data()

for k, v in info.items():
    o_length = len(v)
    n_length = len(set(v))
    if o_length != n_length:
        print(o_length, n_length)
        print(info[k])
