# -*- coding:utf-8 -*-

# Name: SUN RUI    ID: 18083229g

import util

# test_dict = {
#     '1': ['A','C','E','B','F'],
#     '2': ['A','C','G'],
#     '3': ['E'],
#     '4': ['A', 'C', 'E', 'G','D'],
#     '5': ['A', 'C', 'E', 'G'],
#     '6': ['E'],
#     '7': ['A', 'C', 'E', 'B', 'F'],
#     '8': ['A', 'C', 'D'],
#     '9': ['A', 'C', 'E', 'G'],
#     '10': ['A', 'C', 'E', 'G']
# }

class FpTreeNode:
    def __init__(self, attribute_no=None, parent=None, children=[], attribute_times=0):
        self.attribute_no = attribute_no
        self.attribute_times = attribute_times
        self.parent = parent
        self.children = children
        self.link = None


class FpTree:
    def __init__(self):
        self.util = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")
        self.data = self.util.extract_pickle_data()
        self.head_null_node = FpTreeNode(attribute_no=-1, children=[])

    def create_item_head_table(self):    # create two new variables: self.item_head_table and self.new_data
        frequency_dict = self.util.load_data(self.data)
        self.item_head_table = [[each_attr[0], each_attr[1], []] for each_attr in sorted(frequency_dict.items(),
                            key=lambda item:item[1], reverse=True)]
        # sorted by frequency, format is [[attribute no, frequency times, [] ], [attribute no, frequency times, [] ] ],
        # des order by frequency
        self.sort_list = [each_attr[0] for each_attr in self.item_head_table]
        self.new_data = {}
        for (user_id, page_ls) in self.data.items():    # sort old data by sort_list (sort_list is an attribute list ordered by item_head_table)
            tmp_page_ls = []
            for each_page in self.sort_list:
                if each_page in page_ls:    # there is no repetition in page_ls, referring to he check script check_whether_repetition.py
                    tmp_page_ls.append(each_page)
            self.new_data[user_id] = tmp_page_ls

    def create_fp_tree(self):
        # print(self.new_data)
        for (user_id, page_ls) in self.new_data.items():
        # for (user_id, page_ls) in test_dict.items():
            judge = False
            current_node = self.head_null_node    # 首先current_node赋头结点
            if not self.head_null_node.children:  # 如果是第一次，头结点的子节点尚为空值，则从头开始搞
                self.head_null_node.children.append(
                    FpTreeNode(page_ls[0], current_node, [], attribute_times=0))
                current_node = self.head_null_node.children[-1]
                self.item_head_table[self.sort_list.index(page_ls[0])][2].append(current_node)
            else:  # 已经不是第一次了
                if current_node is self.head_null_node:
                    for child in current_node.children:
                        if child.attribute_no == page_ls[0]:
                            # 下一个待建树的值是子节点中其中一个
                            # child.attribute_times += 1
                            current_node = child
                            judge = True
                            break
                    # if judge is True:
                    #     count2 += 1
                    #     continue
                    if judge is False:
                        current_node.children.append(FpTreeNode(page_ls[0], current_node, [], attribute_times=0))
                        current_node = current_node.children[-1]
                        self.item_head_table[self.sort_list.index(page_ls[0])][2].append(current_node)
                        # continue
            for each_page in page_ls:    # 遍历每一项用户点击页面的列表
                if each_page == current_node.attribute_no:    # 当前节点之前已经有过了
                    current_node.attribute_times += 1
                    if current_node.children:    # 如果子节点非空，则寻找是否应该使用下面那个子节点
                        for child in current_node.children:
                            if page_ls.index(each_page) < len(page_ls) - 1:    # 防止越界
                                if child.attribute_no == page_ls[page_ls.index(each_page)+1]:
                                    # 下一个待建树的值是子节点中其中一个
                                    current_node = child
                                    break
                        # if judge2 is False:
                        #     # 下一个待建树的值在现有子节点中没有，则需要新建一个子节点
                        #     current_node.children.append(FpTreeNode(each_page, current_node, [], attribute_times=1))
                        #     current_node = current_node.children[-1]
                else:
                    current_node.children.append(FpTreeNode(each_page, current_node, [], attribute_times=1))
                    current_node = current_node.children[-1]
                    self.item_head_table[self.sort_list.index(each_page)][2].append(current_node)

    def search_node(self, current_node, each_page):
        if current_node.attribute_no == each_page:
            return current_node
        else:
            for each_child in current_node.children:
                self.search_node(each_child, each_page)

    def travel_up_tree(self, last_node):
        result_ls = []
        temp_node = last_node
        while True:
            result_ls.append(temp_node)
            temp_node = temp_node.parent
            # try:
            if temp_node.attribute_no == -1:
                break
            # except:
            #     print(temp_node)
            #     # print(temp_node[0].attribute_no)
            #     # print(temp_node[-1].attribute_no)
            #     pass
        return result_ls[::-1]    # [a,b,c,d]

    def search_longest_ls(self, freq_ls):   # [[a,b,c,d],[a,c,d],[...],...]
        max_length = 0
        max_index = 0
        for index in range(len(freq_ls)):
            tmp_length = len(freq_ls[index])
            if max_length < tmp_length:
                max_length = tmp_length
                max_index = index
        return max_index, max_length    # no use max_length

    def change_freq_by_last(self, freq_ls):    # create new data by dict from fp tree, input:[[A,b,c,D],[A,c,D],[...],...], all same first and last
        freq_lists = []
        for each_freq in freq_ls:
            frequency = each_freq[-1].attribute_times
            freq_ls = []
            # print(each_freq[0].attribute_no, each_freq[0].attribute_times)
            for each_node in each_freq:
                freq_ls.append({each_node.attribute_no: frequency})
            freq_lists.append(freq_ls)
        return freq_lists

    def find_node_index(self, node, freq_ls):    # {A:100}    [{A:100},{b:50},{c:10},{D:1}]
        for each_node in freq_ls:
            # print(node.keys(), each_node.keys())
            if node.keys() == each_node.keys():
                # print(freq_ls.index(each_node))
                return freq_ls.index(each_node)

    def combine_freq_lists(self, freq_lists):    # [[{A:100},{b:50},{c:10},{D:1}],[{A:100},{b:50},{D:1}],[...],...]
        max_ls_length_index, max_length = self.search_longest_ls(freq_lists)
        basic_freq_ls = freq_lists[max_ls_length_index]    # [{A:100},{b:50},{c:10},{D:1}]
        for index in range(len(freq_lists)):    # [{A:100},{b:50},{c:10},{D:1}]
            if index == max_ls_length_index:
                continue
            for each_node in freq_lists[index]:    # each_node {A:100}
                node_index = self.find_node_index(each_node, basic_freq_ls)
                # if node_index == 0:
                #     print(each_node)
                # if not node_index:
                #     continue
                if node_index is None:
                    basic_freq_ls.append(each_node)
                    continue
                for (no, times) in basic_freq_ls[node_index].items():
                    # print(basic_freq_ls[node_index])
                    basic_freq_ls[node_index][no] += each_node[no]
                    # print(each_node[no])
                    # print(basic_freq_ls[node_index])
                    # print("----------------------------------------------------------")
        return basic_freq_ls

    def remove_low_support_item(self, freq_lists_set):    # [ [{A:100},{b:50},{c:10},{D:1}],[{A:100},{b:50},{D:1}],[...], ... ]
        max_freq_sets = []
        for freq_ls in freq_lists_set:
            basic_freq = list(freq_ls[-1].values())[0]
            remove_items_ls = []
            for each_item in freq_ls:
                if list(each_item.values())[0] < basic_freq:
                    remove_items_ls.append(each_item)
            for each_remove_item in remove_items_ls:
                freq_ls.remove(each_remove_item)
            max_freq_sets.append(freq_ls)
            del(remove_items_ls)
        return max_freq_sets

    def mine_fp_tree(self):
        all_frequency_ls = []
        for each_item in self.item_head_table[::-1]:
            dict_freq = {}
            for last_node in each_item[2]:
                # try:
                each_freq_ls = self.travel_up_tree(last_node)
                # except:
                #     print(last_node)
                #     break
                    # print(self.item_head_table.index(each_item))
                if each_freq_ls[0].attribute_no not in dict_freq:
                    dict_freq[each_freq_ls[0].attribute_no] = [each_freq_ls]
                else:
                    dict_freq[each_freq_ls[0].attribute_no].append(each_freq_ls)    # {A: [[A,b,c,D],[A,c,D],[...],...], B: [...], ...}
            for (attr_no, freq_lists) in dict_freq.items():
                # with open("test.txt", 'a') as fp:
                #     fp.writelines("attr_no:{}\n".format(attr_no))
                #     for each in freq_lists:
                #         fp.writelines("\t{}, {}\n".format(each[0].attribute_no, each[-1].attribute_no))
                new_freq_lists = self.change_freq_by_last(freq_lists)
                # print(new_freq_lists)
                max_freq_item = self.combine_freq_lists(new_freq_lists)
                # print(max_freq_item)
                all_frequency_ls.append(max_freq_item)
                max_freq_sets = self.remove_low_support_item(all_frequency_ls)
        return max_freq_sets


def main():
    ob = FpTree()
    ob.create_item_head_table()
    ob.create_fp_tree()
    final_result = ob.mine_fp_tree()
    # tmp_ls = []
    # tmp_ls2 = []
    for each in final_result:
        if list(each[-1].values())[0] > 3:
            print(each)
        # tmp_ls.append(each[-1])
        # tmp_ls2.append(each[0])
    #
    # import copy
    # temp_ls = copy.deepcopy(tmp_ls)
    # for each in tmp_ls:
    #     temp_ls.remove(each)
    #     for i in temp_ls:
    #         if each.keys() == i.keys():
    #             print(each.keys(), i.keys())
    #             print(each, tmp_ls2[tmp_ls.index(each)], tmp_ls2[temp_ls.index(i)])


if __name__ == '__main__':
    main()
