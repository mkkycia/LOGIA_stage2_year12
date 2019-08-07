def ilecyfr(liczba, podstawa):
    i = 0
    wynik = 1
    while liczba > wynik:
        i += 1
        wynik = wynik * podstawa
    if i == 0:
        return 1
    return i

print(ilecyfr(255, 16))
