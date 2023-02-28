# hometask
# # 1
# file = "first_task.txt"
# read_file = open(file, "r", encoding="UTF-8")
# for line in read_file:
#     print(line.strip() + "!")
# read_file.close()
# ================
# # 2
# file_inp = "input.txt"
# file_out = "output.txt"
# file_input = open(file_inp, "r", encoding="UTF-8")
# file_output = open(file_out, "w", encoding="UTF-8")
# lst = []
# mltp = 1
# for line in file_input:
#     lst = list(map(int, line.strip().split()))
# for i in range(len(lst)):
#     mltp *= lst[i]
# file_output.write(f"Multiplay of the numbers {lst} is {mltp}")
# file_output.close()
# file_input.close()
# =================
# # 3 third task
# import datetime
#
# file = "third_task.txt"
# file_in = open(file, "r", encoding="UTF-8")
# date_now = datetime.datetime.now()
# for line in file_in:
#     value = line.strip().split()[2]
#     date = line.strip().split()[3]
#     date_day = int(date[:2])
#     date_month = int(date[3:5])
#     date_year = int(date[6:])
#
#     if int(value) > 1000000 and int(str(date_now.date() - datetime.date(date_year, date_month, date_day)).split()[0]) >= 30:
#         print(line.strip().split())
#         print(date_now.date() - datetime.date(date_year, date_month, date_day))
# file_in.close()
# ====================
# # 4
# file_qastions = "qastions.txt"
# file_answers = "answers.txt"
# file_qa = open(file_qastions, "r", encoding="UTF-8")
# file_ans= open(file_answers, "r", encoding="UTF-8")
# count_answers = 0
# for line, line_second in zip(file_qa, file_ans):
#     print(line.strip())
#     answer = input("Enter the answer(да/нет): ")
#     if answer.lower() == line_second.strip().lower():
#         count_answers += 1
#
# print(f"correct answers is {count_answers} of 11 qastions")
# file_qa.close()
# file_ans.close()
# ===============
# # 5
# import json
#
# file = "dct_json.json"
# file_json = open(file, "w", encoding="UTF-8")
# dct = {86853: ("Eugene", 20), 24365: ("Gene", 17), 73154: ("Kate", 21), 49910: ("Pete", 20), 78411: ("Henry", 23), 88822: ("Helen", 27)}
# information = json.dumps(dct, indent=2)
# file_json.write(information)
# ==============
# # 6
# import json
# import csv
# file_js = "dct_json.json"
# file_cs = "file_csv.csv"
# file_read = open(file_js, "r", encoding="UTF-8")
# file_write = open(file_cs, "w", encoding="UTF-8")
# text = json.load(file_read)
# for key, value in text.items():
#     file_write.write(f"Person;{key};{value[0]};{value[1]}\n")
#
# file_write.close()
# file_read.close()
# ========
# # 7
# file = "7.txt"
# file_r = open(file, "r", encoding="UTF-8")
# lst_second = []
# dct = dict()
# count = 0
# for line in file_r:
#     lst = line.split()
#
#     for i in range(len(lst)):
#         if dct.get(lst[i].lower()) is None:
#             count += 1
#             key = lst[i].lower()
#             value = count
#             dct.update({key: value})
#         else:
#             dct[lst[i].lower()] += 1
#         count = 0
# maxx = 0
# ans_key = ""
# for key, value in dct.items():
#     if maxx < value:
#         maxx = value
#         ans_key = key
# print(ans_key, dct[ans_key])
# file_r.close()
# ===============
# # 8
#
# file = "8.txt"
# file_r = open(file, "r", encoding="UTF-8")
# str1 = ""
# str2 = ""
# for line in file_r:
#     k = 0
#     while line[k] != line[-1]:
#         if line[k + 1].isdigit():
#             if line[k + 2].isdigit():
#                 j = int(line[k + 1] + line[k + 2])
#                 while j != 0:
#                     str1 += line[k]
#                     j -= 1
#                 k += 3
#
#             else:
#                 j = int(line[k + 1])
#                 while j != 0:
#                     str1 += line[k]
#                     j -= 1
#                 k += 2
#
# print(str1)
# file_r.close()
#
# count = 1
# ans = ""
# for i in range(len(str1) - 1):
#     if str1[i] == str1[i + 1]:
#         count += 1
#     else:
#         ans = str1[i]
#         str2 += ans + str(count)
#         count = 1
# if str1[-2] == str1[-1]:
#     count += 1
# else:
#     ans = str1[-1]
#     str2 += ans + str(count)
#     count = 1
#
# print(str2)



