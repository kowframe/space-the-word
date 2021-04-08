# -*- coding: utf-8 -*-
# Develop by: kowframe
def is_stop(usr_cmd):
    if usr_cmd == "exit" or usr_cmd == "EXIT":
        return True

while(True):
    word = input("Tell something (type \"exit\" to exit): ")
    if is_stop(word) is True:
        break

    text = ""
    vowel = ["ิ", "ุ", "ี", "ุ", "ู", "ึ", "ื", "ั", "่", "้", "๊", "๋", "์"]

    for a in word:
        if(a in vowel):
            text = text[:-1]
        text += a + " "

    print("\n*************")
    print(text)
    print("\n*************")

# test git
# test git 2
# test git 3

