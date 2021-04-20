#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def compare_files(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        lignes1 = f1.readlines()
        lignes2 = f2.readlines()
        if len(lignes1) != len(lignes2):
            print("Les fichiers ne sont pas de la même longueur")
        else:
            for i in range(len(lignes1)):
                if lignes1[i] != lignes2[i]:
                    print(f"{lignes1[i]} N'est pas pareil à : \n{lignes2[i]}")
                    break
            else:
                print("Ces fichiers sont identiques")


def triple_spaces(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "w", encoding="utf-8") as f2:
        for ligne in f1:
            f2.write(ligne.replace(" ", "   "))


def note_to_lettre(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "w", encoding="utf-8") as f2:
        for note in f1:
            for lettre, intervalle in PERCENTAGE_TO_LETTER.items():
                if intervalle[1] > int(note.strip()) >= intervalle[0]:
                    f2.write(note.strip() + " " + lettre + "\n")


def nombres(file):
    with open("exemple.txt", "r", encoding="utf-8") as f1:
        words = f1.read().replace("\n", " ").split()
        nombres = []
        for word in words:
            if word.isdigit():
                nombres.append(int(word))
        print(sorted(nombres))


def recopie_1_sur_2(file1, file2):
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "w", encoding="utf-8") as f2:
        lignes1 = f1.readlines()
        for i in range(0, len(lignes1), 2):
            f2.write(lignes1[i])




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_files("exemple.txt", "exemple2.txt")
    triple_spaces('exemple.txt', 'exemple_triple_espaces.txt')
    note_to_lettre('notes.txt', 'notes_et_lettres.txt')
    nombres("exemple.txt")
    recopie_1_sur_2("exemple.txt", "exemple_1_sur_2.txt")

