import random as rd

def validator(str="atg"):
    nbr_str = 0

    for n in str:
        for verf in "atgc":
            if n == verf:
                nbr_str = nbr_str + 1
    if len(str) == nbr_str:
        return True
    else:
        return False

def randomSaisie():
    list_atcg = "atgc"
    output = ""
    for e in range(rd.randrange(8,450)):
        for i in range(rd.randrange(0, 5)):
            output = output + list_atcg[i]
    return  output





if __name__ == "__main__":
    str = randomSaisie()
    print(str)
    valid = validator(str)

    if valid:
        print("chaine valide")
    else:
        print("chaine invalide")

    print("{0:.2f}".format(1.35555533), "test")