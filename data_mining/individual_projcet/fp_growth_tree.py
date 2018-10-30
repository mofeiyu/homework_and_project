# -*- coding:utf-8 -*-

# Name: SUN RUI    ID: 18083229g

import util

test_dict={
    '1': ['A','C','E','B','F'],
    '2': ['A','C','G'],
    '3': ['E'],
    '4': ['A', 'C', 'E', 'G','D'],
    '5': ['A', 'C', 'E', 'G'],
    '6': ['E'],
    '7': ['A', 'C', 'E', 'B', 'F'],
    '8': ['A', 'C', 'D'],
    '9': ['A', 'C', 'E', 'G'],
    '10': ['A', 'C', 'E', 'G']
}


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
        self.head_null_node = FpTreeNode(children=[])

    def create_item_head_table(self):    # create two new variables: self.item_head_table and self.new_data
        frequency_dict = self.util.load_data(self.data)
        self.item_head_table = [[each_attr[0], each_attr[1]] for each_attr in sorted(frequency_dict.items(),
                            key=lambda item:item[1], reverse=True)]
                        # sorted by frequency, the format is [[attribute no, frequency times]], des order by frequency
        self.sort_list = [each_attr[0] for each_attr in self.item_head_table]
        self.new_data = {}
        for (user_id, page_ls) in self.data.items():    # sort old data by sort_list (sort_list is an attribute list ordered by item_head_table)
            tmp_page_ls = []
            for each_page in self.sort_list:
                if each_page in page_ls:    # there is no repetition in page_ls, referring to he check script check_whether_repetition.py
                    tmp_page_ls.append(each_page)
            self.new_data[user_id] = tmp_page_ls

    def create_fp_tree(self):
        # for (user_id, page_ls) in self.new_data.items():
        for (user_id, page_ls) in test_dict.items():
            judge = False
            current_node = self.head_null_node    # 首先current_node赋头结点
            if not self.head_null_node.children:  # 如果是第一次，头结点的子节点尚为空值，则从头开始搞
                self.head_null_node.children.append(
                    FpTreeNode(page_ls[0], self.head_null_node.children, [], attribute_times=0))
                current_node = self.head_null_node.children[-1]
                # self.item_head_table[self.sort_list.index(each_page)].append(current_node)
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
                        # continue
            for each_page in page_ls:    # 遍历每一项用户点击页面的列表
                judge2 = False
                if each_page == current_node.attribute_no:    # 当前节点之前已经有过了
                    current_node.attribute_times += 1
                    if current_node.children:    # 如果子节点非空，则寻找是否应该使用下面那个子节点
                        for child in current_node.children:
                            if page_ls.index(each_page) < len(page_ls) - 1:    # 防止越界
                                if child.attribute_no == page_ls[page_ls.index(each_page)+1]:
                                    # 下一个待建树的值是子节点中其中一个
                                    current_node = child
                                    judge2 = True
                                    break
                        if judge2 is False:
                            # 下一个待建树的值在现有子节点中没有，则需要新建一个子节点
                            current_node.children.append(FpTreeNode(each_page, current_node, [], attribute_times=1))
                            current_node = current_node.children[-1]
                else:
                    current_node.children.append(FpTreeNode(each_page, current_node, [], attribute_times=1))
                    current_node = current_node.children[-1]

    def search_node(self, current_node, each_page):
        if current_node.attribute_no == each_page:
            return current_node
        else:
            for each_child in current_node.children:
                self.search_node(each_child, each_page)



    def mine_fp_tree(self):
        pass