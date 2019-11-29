from typing import List

if __name__ == "__main__":
    nbr_entier = int(input("Entrez un entier strictement positif: "))
    nbr_list: List[int] = []
    nbr = 1
    while nbr < nbr_entier:
        nbr = nbr + 1
        if nbr_entier % nbr == 0:
            nbr_list.append(nbr)
    nbr_list.pop(len(nbr_list) - 1)

    if len(nbr_list) > 0:
        print("Diviseur propre sans répétition de", nbr_entier, ": ", nbr_list)
        print("il a ", len(nbr_list), " diviseurs propres")
    else:
        print("Diviseur propre sans répétition de", nbr_entier, ": aucun")
        print("il est deja premier!")
