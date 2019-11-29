from pyDatalog.pyDatalog import create_terms, ask, load, assert_fact

if __name__ == "__main__":
    create_terms('X, frog, canary, green, yellow, chirps, sings, croakes, eatFlies')

    load("""
        frog(X) <= croakes(X) & eatFlies(X)
        canary(X) <= chirps(X) & sings(X)
        green(X) <= frog(X)
        yellow(X) <= canary(X)
    """)

    assert_fact('croakes', 'fritz')
    assert_fact('eatFlies', 'fritz')

    print(ask('frog(X)').answers)

