# -*- coding:utf-8 -*-

import util

clean_attribute = util.Clean("train_data/attributes_train_data", "train_pickle/attributes_train_data.pickle",
                             "attribute")
clean_attribute.pickle_data()

info = clean_attribute.extract_pickle_data()

print(info)
print(len(info))

# clean_case = util.Clean("train_data/user_case_train_data", "train_pickle/user_case_train_data.pickle",
#                              "case")
# clean_case.pickle_data()
#
# info = clean_case.extract_pickle_data()
#
# print(info)
# print("10001" in info)
# print(len(info))

