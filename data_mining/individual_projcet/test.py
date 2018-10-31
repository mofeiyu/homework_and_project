# -*- coding:utf-8 -*-

import util
import fp_growth_tree as fp

# clean_attribute = util.Clean("train_data/attributes_train_data", "train_pickle/attributes_train_data.pickle",
#                              "attribute")
# clean_attribute.pickle_data()

# info = clean_attribute.extract_pickle_data()

# print(info)
# print(len(info))

# clean_case = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")
# # clean_case.pickle_data()
# #
# info = clean_case.extract_pickle_data()
#
# print(info)
# print("10001" in info)
# print(len(info))

# fre_dict = clean_case.load_data(info)
# print(fre_dict)
#
#
# for k, v in info.items():
#     o_length = len(v)
#     n_length = len(set(v))
#     if o_length != n_length:
#         print(o_length, n_length)
#         print(info[k])


ob = fp.FpTree()
ob.create_item_head_table()
# for each in ob.item_head_table:
#     count += each[1]
#     if each[0] == "1034":
#         print(each[1])
#
# print(count)
ob.create_fp_tree()
# for each in ob.head_null_node.children:
#     if each.attribute_no == '1034':
#         print("val:{0}  times:{1}".format(each.attribute_no, each.attribute_times))
# print(len(ob.head_null_node.children))
print(ob.item_head_table[200][0])
print(ob.item_head_table[200][1])
print(len(ob.item_head_table[200][2]))
print("________________________________________")
count = 0
count2 = 0
for each in ob.item_head_table[200][2]:
    # print(each.attribute_no,each.attribute_times)
    count2 += each.attribute_times
    count += 1
print(count, count2)

# print(ob.head_null_node.children[0].children)
# for each in ob.head_null_node.children:
#     print(each.attribute_no)
#     print(each.attribute_times)
#     print(len(each.children))
#     print('\n')

