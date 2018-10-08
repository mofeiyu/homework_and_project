import sys
import numpy as np

new_ls = [float(each) for each in sys.argv[1:]]
# c1, c2, c3 = new_ls

sum_ = sum(new_ls)
result = 0
for each in new_ls:
    if each == 0:
        continue
    result += -each/sum_ * np.log2(each/sum_)

# print(-c1/(c1+c2+c3)*np.log2(c1/(c1+c2+c3)))
# print(-c2/(c1+c2+c3)*np.log2(c2/(c1+c2+c3)))
# print(-c3/(c1+c2+c3)*np.log2(c3/(c1+c2+c3)))

# result = -c1/(c1+c2+c3)*np.log2(c1/(c1+c2+c3)) - c2/(c1+c2+c3)*np.log2(c2/(c1+c2+c3)) - c3/(c1+c2+c3)*np.log2(c3/(c1+c2+c3))

print(result)


