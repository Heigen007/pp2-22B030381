import os

# #1
# pth = r"C:\Users\Admin\Desktop\pp2-22B030386"
# print(os.listdir(pth))
##2
# path = r"C:\Users\Admin\Desktop\pp2-22B030386\tsis6\v.txt"
# if not os.path.exists(path):
#     print(f"{path} does not exist.")
# else:
#     print(f"{path} exists.")
#
#     # Test readability
#     if not os.access(path, os.R_OK):
#         print(f"{path} is not readable.")
#     else:
#         print(f"{path} is readable.")
#
#     # Test writability
#     if not os.access(path, os.W_OK):
#         print(f"{path} is not writable.")
#     else:
#         print(f"{path} is writable.")
#
#     # Test executability
#     if not os.access(path, os.X_OK):
#         print(f"{path} is not executable.")
#     else:
#         print(f"{path} is executable.")
# # 3
# pth = r"C:\Users\Admin\Desktop\pp2-22B030386"
# if os.path.isdir(pth):
#     print("exist", os.path.basename(pth))
#     print(pth.split("\\"))
#
# else:
#     print("not exist")

# #4
# file = open("v.txt")
# cnt = 0
# for i in file:
#     cnt+=1
# print(cnt)

# 5
# l = [1, 2, 3, 4, 5]
# file = open("v.txt", "a+")
# file.write(str(l) + '\n')
# file.seek(0)
# print(file.read())

# # 6
# cod = 65
# while cod < 91:
#     open(f"{chr(cod)}.txt", 'w')
#     cod += 1
# cod2 = 90
# while cod2 > 64:
#     d = fr"C:\Users\Admin\Desktop\pp2-22B030386\tsis6\{chr(cod2)}.txt"
#     os.remove(d)
#     cod2 -= 1

# # 7
# a = open("v.txt")
# b = a.read()
# c = open("v_copy.txt", "w")
# c.write(b)

# # 8
# p = r"C:\Users\Admin\Desktop\pp2-22B030386\tsis6\deleteme.txt"
# if os.path.exists(p):
#     os.remove(p)
# else:
#     print("not exist")
