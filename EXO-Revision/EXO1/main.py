if __name__ == "__main__":

    hauteur = int(input("Taille du sapin:\nhauteur:"))
    branche = ['^']
    space = ' '

    for y in range(0, hauteur - 1):
        branche.append('^' + branche[y] + '^')
        print(int(hauteur-y)*space + branche[y])
