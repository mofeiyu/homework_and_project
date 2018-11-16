# -*- coding:utf-8 -*-

# Name: SUN RUI    ID: 18083229g

import util

class SeqArm:
    def __init__(self):
        self.util = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")
        self.data = self.util.extract_pickle_data()
        self.sequence_1 = self.util.load_data(self.data)
        self.sequence_phase_table = {}

    def sequence_phase(self, sequence):
        sequence_n = {}
        if len(sequence[0]) == 1:
            for i in range(len(sequence)):
                for j in range(len(sequence)):
                    count_num = self.count_fequency((sequence[i], sequence[j]))
                    sequence_n[(sequence[i], sequence[j])] = count_num
        else:
            pass

    def count_fequency(self, sub_sequence):
        for each_seq in self.data.values():
            judge = True
            for each_web in sub_sequence:
                if each_web not in each_seq:
                    judge = False
                    break
            if judge == True:
                # TODO: count ++

        return 0

    def judge_maximal_sequences(self):
        pass

    def find_max_length(self):
        pass


def main():
    pass

if __name__ == '__main__':
    main()