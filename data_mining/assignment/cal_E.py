import sys
import numpy as np

new_ls = [float(each) for each in sys.argv[1:]]

len_ls = len(new_ls)
# print(new_ls[1:3:2])
sum_ = sum([ each for each in new_ls[1:len_ls:2]])
# print(sum_)
result = 0
for i in range(int(len_ls/2)):
    result += new_ls[i*2] * new_ls[i*2+1]/sum_
print(result)