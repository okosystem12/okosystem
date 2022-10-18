import os


token = ""
with open(os.path.abspath(os.path.join("genering_profils_vk", "files", "token.txt"))) as file:
    for line in file:
        token = line

lst_dict = []
with open(os.path.abspath(os.path.join("genering_profils_vk", "files", "dict.txt"))) as file:
    for line in file:
        lst_dict.append(line.replace("\n", ""))
