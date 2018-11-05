import eji_data
import eji_data2
import eji_data3

# 1
# A_ls = [1,1,1,1,1,1,1,2,3]
# B_ls = [1,1,1,1,3,1,1,2]
# C_ls = [1,1,2,1,3,1,1]
# D_ls = [1,1,1,2,1,1]
# E_ls = [1,1,1,2,3]
# F_ls = [2,1,1,2]
# G_ls = [1,1,1]
# H_ls = [1,1]
# J_ls = [1]

# 2
# A_ls = [1,1,1,1,1,1,1,1,2]
# B_ls = [1,1,1,1,2,1,1,2]
# C_ls = [1,1,2,1,2,1,2]
# D_ls = [1,1,1,1,1,2]
# E_ls = [1,1,1,1,2]
# F_ls = [1,1,1,2]
# G_ls = [1,1,2]
# H_ls = [1,1]
# J_ls = [1]

# 3
A_ls = [1,1,1,1,1,1,1,1,2]
B_ls = [1,1,1,1,1,1,1,2]
C_ls = [1,1,1,1,1,1,2]
D_ls = [1,1,1,1,1,2]
E_ls = [1,1,1,1,2]
F_ls = [1,1,1,2]
G_ls = [1,1,2]
H_ls = [1,1]
J_ls = [1]
all_ls = A_ls + B_ls + C_ls + D_ls + E_ls + F_ls + G_ls + H_ls + J_ls
AB_ls = eji_data3.JK

betweenness = 0
for (up, down) in zip(AB_ls, all_ls):
    betweenness += up/down
print(betweenness)