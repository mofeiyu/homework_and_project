# -*- coding:utf-8 -*-

# Name: SUN RUI    ID: 18083229g

import pickle
import util

class SeqArm:
    def __init__(self):
        self.util = util.Clean(pickle_file="train_pickle/user_case_train_data.pickle", pickle_type="case")
        self.data = self.util.extract_pickle_data()
        self.sequence_1 = self.util.load_data(self.data)
        self.sequence_phase_table = {1: self.sequence_1}
        self.maximal_sequences = []
        # self.count

    def sequence_phase(self, sequence):
        sequence = list(sequence)
        self.sequence_n = {}
        if type(sequence[0]) != tuple:
            for i in range(len(sequence)):
                for j in range(len(sequence)):
                    count_num = self.count_frequency((sequence[i], sequence[j]))
                    if count_num != 0:
                        self.sequence_n[(sequence[i], sequence[j])] = count_num
            self.sequence_phase_table[2] = self.sequence_n
        else:
            use_judge = False
            for i in range(len(sequence)):
                for j in range(len(sequence)):
                    if sequence[i][:-1] == sequence[j][:-1] and sequence[i][-1] != sequence[j][-1]:
                        # print(list(sequence[i][:-1]),sequence[j][:-1],sequence[i][-1],sequence[j][-1])
                        use_judge = True
                        count_num = self.count_frequency(list(sequence[i]) + [sequence[j][-1]])
                        if count_num != 0:
                            combine_tuple = tuple(list(sequence[i]) + [sequence[j][-1]])
                            self.sequence_n[combine_tuple] = count_num
                if use_judge == False:
                    self.maximal_sequences.append(sequence[i])
            self.sequence_phase_table[len(sequence[0])+1] = self.sequence_n

    def count_frequency(self, sub_sequence):    # sub_sequence: [a,b,c...]
        count = 0
        for each_seq in self.data.values():
            judge = True
            current_position = -1
            for each_web in sub_sequence:
                if each_web not in each_seq:
                    judge = False
                    break
                else:
                    if each_seq.index(each_web) <= current_position:
                        judge = False
                        break
                    else:
                        current_position = each_seq.index(each_web)
            if judge == False:
                continue
            else:
                count += 1
                # print(count)
                # print(sub_sequence)
        return count

    # def find_max_length(self, sequences):
    #     max_length = 0
    #     max_index = 0
    #     for index in range(len(sequences)):
    #         tmp_length = len(sequences[index])
    #         if max_length < tmp_length:
    #             max_length = tmp_length
    #             max_index = index
    #     return max_index, max_length  # no use max_index

def main():
    maximal_dict = {}
    seq_arm_op = SeqArm()
    # max_index, max_length = seq_arm_op.find_max_length(list(seq_arm_op.sequence_1.keys()))
    sequence = list(seq_arm_op.sequence_1.keys())[:10]
    while True:
        seq_arm_op.sequence_phase(sequence)
        sequence = seq_arm_op.sequence_n.keys()
        if not sequence:
            break
    print(seq_arm_op.sequence_phase_table)

    for each in seq_arm_op.maximal_sequences:
        maximal_dict[len(each)] = each

    with open("maximal.pickle", "wb") as f:
        pickle.dump(maximal_dict, f)

    print(maximal_dict)


if __name__ == '__main__':
    main()