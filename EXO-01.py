import numpy as np

if __name__ == "__main__":
    rayon = float(input("Rayon: "))
    hauteur = float(input("hauteur: "))

    volume = 1/3 * np.pi * rayon**2 * hauteur

    print("le volume est: ", volume)
