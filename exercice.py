#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
import os
import sys

# TODO: Définissez vos fonction ici
def compare_files(file1, file2):
    with open(file1, 'r', encoding="utf-8") as f1, open(file2, 'r', encoding="utf-8") as f2:
        for line1 in f1:
            line2 = f2.readline()
            if line1 != line2:
                print("The files are not identical")
                print(line1)
                print("Is not the same as:")
                print(line2)
                break
        else:
            print("The files are identical")

def triple_spaces(file, file2):
    with open(file, 'r', encoding='utf-8') as f1, open(file2, 'w', encoding='utf-8') as f2:
        for line1 in f1:
            f2.write(line1.replace(' ', '   '))

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_files("exemple.txt", "exemple2.txt")
    triple_spaces('exemple.txt', 'exemple_triple_espaces.txt')
    pass
