A_ls = [1,1,1,1,1,1,1,1,2]
B_ls = [1,1,1,1,1,1,1,2]
C_ls = [1,1,1,1,1,1,2]
D_ls = [1,1,1,1,1,2]
E_ls = [1,1,1,1,2]
F_ls = [1,1,1,2]
G_ls = [1,1,2]
H_ls = [1,1]
J_ls = [1]

all_ls = [A_ls, B_ls, C_ls, D_ls, E_ls, F_ls, G_ls, H_ls, J_ls]
columns_ls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K']
for row in range(len(all_ls)):
    for column in range(len(all_ls[row])):
        print("σ{}{}={},".format(columns_ls[row], columns_ls[column+row+1], all_ls[row][column]), end='')
    print()


# from eji_data import AB as eb
# eb_new = [eb[0:9], eb[9:17], eb[17:24], eb[24:30], eb[30:35], eb[35:39], eb[39:42], eb[42:44], eb[44:45]]
# e_name = "AB"
# for row in range(len(eb_new)):
#     for column in range(len(eb_new[row])):
#         print("σ{}{}(e{})={},".format(columns_ls[row], columns_ls[column+row+1], e_name, eb_new[row][column]), end='  ')
#     print()

# from eji_data3 import all_eb
# for j in range(len(all_eb[0])):
#     for i in range(len(all_eb)):
#         print("{},".format(all_eb[i][j]), end='')
#     print()

# for row in range(len(all_ls)):
#     for column in range(len(all_ls[row])):
#         print("{}{}".format(columns_ls[row], columns_ls[column+row+1]))