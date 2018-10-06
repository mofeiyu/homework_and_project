str_1 = "你好嗎"
str_to_utf8 = str_1.encode("utf-8")
str_to_big5 = str_1.encode("big5")
print("{0} == {1} : {2}".format(str_to_utf8, str_to_big5, (str_to_utf8 == str_to_big5)))

utf8_to_str = str_to_utf8.decode("utf-8")
big5_to_str = str_to_big5.decode("big5")
print("{0} == {1} : {2}".format(utf8_to_str, big5_to_str, (utf8_to_str == big5_to_str)))


with open("test_gbk.text", 'r', encoding="GBK") as fr:
    content_ls = fr.readlines()
out_ls = []
for each_line in content_ls:
    out_ls.append(each_line.encode("utf-8").decode("utf-8"))

with open("result_file.text", 'a', encoding="utf-8") as fw:
    fw.writelines(out_ls)


# ls = ["凤凰大很费劲啊开来和\n"]*10
# with open("test_gbk.text", "a", encoding="gbk") as fw:
#     fw.writelines(ls)
