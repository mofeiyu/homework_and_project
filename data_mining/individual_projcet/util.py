# -*- coding:utf-8 -*-
# Name: SUN RUI    ID: 18083229g

import pickle

class Clean:
    def __init__(self, origin_file=None, pickle_file=None, pickle_type=None):
        self.origin_file = origin_file
        self.pickle_file = pickle_file
        self.pickle_type = pickle_type

    def clean_attributes(self):
        data_list = self.read_origin_file(self.origin_file)
        attributes_dic = {}
        for each_attribute in data_list:
            temp_list = each_attribute.strip().split(',')
            temp_list = [item.strip("\"") for item in temp_list]
            attributes_dic[temp_list[1]] = temp_list[-2:]
        return attributes_dic

    def clean_cases(self):
        data_list = self.read_origin_file(self.origin_file)
        cases_dic = {}
        for each_case in data_list:
            temp_list = each_case.strip().split(',')
            if temp_list[0] == 'C':
                user_id = temp_list[2]
                cases_dic[user_id] = []
            if temp_list[0] == 'V':
                if user_id in cases_dic:
                    cases_dic[user_id].append(temp_list[1])
        return cases_dic

    def pickle_data(self):
        if self.pickle_type == "attribute":
            attribute_dic = self.clean_attributes()
            with open(self.pickle_file, "wb") as f:
                pickle.dump(attribute_dic, f, pickle.HIGHEST_PROTOCOL)
        if self.pickle_type == "case":
            case_dic = self.clean_cases()
            with open(self.pickle_file, "wb") as f:
                pickle.dump(case_dic, f, pickle.HIGHEST_PROTOCOL)

    def extract_pickle_data(self):
        with open(self.pickle_file, "rb") as f:
            data = pickle.load(f)
        return data    # format: {"user id": ["web page id", ...... ]}

    def read_origin_file(self, file_path):
        with open(file_path, "r") as f:
            data_list = f.readlines()
        return data_list

    def load_data(self, data):    # data: {"user_id": ["web page id", ...... ]}
        frequency_dict = {}
        web_page_records = data.values()
        for each_record in web_page_records:
            for each_page in each_record:
                if each_page not in frequency_dict:
                    frequency_dict[each_page] = 1
                else:
                    frequency_dict[each_page] += 1
        # tmp_frequency_dict = copy.deepcopy(frequency_dict)
        # for (attr, times) in tmp_frequency_dict.items():
        #     if times < 3:
        #         frequency_dict.pop(attr)
        return frequency_dict
        # return format: {'attribute no.': times} e.g.: {'1000': 912, '1001': 4451, '1002': 749 ......}