from pyDatalog import pyDatalog



if __name__ == "__main__":
    pyDatalog.create_terms('X, frog, canary, green, yellow, chirps, sings')

    pyDatalog.load("""
        + frog('fritz', 'croakes')
        + frog('fritz', 'eatFlies')
        frog(X) <= croakes(X) & eatFlies(X)
        canary(X) <= chirps(X) & sings(X)
        frog(X) <= green(X)
        canary(X) <= yellow(X)
    """)

    print(pyDatalog.ask('frog(fritz, X)'))

