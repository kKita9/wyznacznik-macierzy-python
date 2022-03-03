# PROGRAM LICZACY WYZNACZNIK Z MACIERZY

from tkinter import *


# ---------- FUNKCJE ------------------ #

# tworzenie macierzy do wpisania elementow
def elementy_do_wpisania():
    # pobranie rozmiaru
    rozmiar = rozmiar_entry.get()
    rozmiar = int(rozmiar)

    # tworzenie kolumn
    for x in range(rozmiar):
        # tworzenie wierszy
        for y in range(rozmiar):
            element = Entry(okno, width=10)  # tworzenie pola element do wczytania wartosci
            element.grid(row=x + 3, column=y, pady=5, padx=5)
            wczytane_elementy.append(element)  # pobranie wartosci z pole element do listy


# funkcja liczaca wyznacznik
def liczenie_wyznacznika():
    # pobranie rozmiaru
    rozmiar = rozmiar_entry.get()
    rozmiar = int(rozmiar)

    # tworzenie listy pomocniczej
    macierz_pomocnicza = []

    # dodanie oraz kowersja z str na float z listy wczytane_elementy do listy macierz_pomocnicza
    for elem in wczytane_elementy:
        macierz_pomocnicza.append(float(elem.get()))

    # tworzenie macierzy o rozmiarze (rozmiar x rozmiar) wypelnionej zerami
    macierz = [[0] * rozmiar for i in range(rozmiar)]

    # zamiana wartosci w macierzy
    for x in range(rozmiar):
        for y in range(rozmiar):
            macierz[x][y] = macierz_pomocnicza[0]
            del macierz_pomocnicza[0]

    # instrukcja warunkowa sprawdzajaca rozmiar macierzy i wywolujaca funkcje zalezna od rozmiaru
    if rozmiar == 1:
        wyznacznik.set(str(macierz[0]))
    elif rozmiar == 2:
        wyznacznik.set(str(wyznacznik_2(macierz)))
    elif rozmiar == 3:
        wyznacznik.set(str(wyznacznik_3(macierz)))
    else:
        wyznacznik.set(str(metoda_laplace(rozmiar, macierz)))


# funkcja liczaca wyznacznik stopnia 2
def wyznacznik_2(m):
    w = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return w


# funkcja liczaca wyznacznik stopnia 3 metoda Sarrusa
def wyznacznik_3(m):
    # dopisanie' dwoch pierwszych wierszy na koniec macierzy
    m.append(m[0])
    m.append(m[1])
    w1 = w2 = 0

    # petla liczaca wyznacznik na podstawie metody Sarrusa
    for i in range(3):
        w1 += m[i][0] * m[i + 1][1] * m[i + 2][2]
        w2 -= m[i][2] * m[i + 1][1] * m[i + 2][0]

    # usuniecie wierszy dodanych na poczatku funkcji
    del m[4]
    del m[3]

    return w1 + w2


# funkcja liczaca wyznacznik metoda Laplace
def metoda_laplace(r, m):
    w = 0

    if r == 3:
        return wyznacznik_3(m)
    else:
        for i in range(r):
            elem = m[i][r - 1]
            wiersz = m[i]
            del m[i]
            w += ((-1) ** (r + i + 1)) * elem * metoda_laplace(r - 1, m)
            m.insert(i, wiersz)

    return w


# ------------PROGRAM--GLOWNY------------------- #

# tworzenie pustej listy, ktora bedzie przechowywac wczytane elementy
wczytane_elementy = []

# tworzenie okna
okno = Tk()
okno.title('Wyznacznik macierzy')

# tworzenie etykiety ROZMIAR
rozmiar_label = Label(okno, text='Rozmiar:', font=("Arial", 9), width=8)
rozmiar_label.grid(row=0, column=0, pady=5, padx=5)

# tworzenie pola do wczytania rozmiaru
rozmiar_entry = Entry(okno, width=10)
rozmiar_entry.grid(row=0, column=1, pady=5, padx=5)

# tworzenie przycisku DALEJ ktory bedzie tworzyc pola do wczytania elementow
dalej_button = Button(okno, text='Dalej', width=7, font=("Arial", 9), background='#34404d', foreground="#ffffff",
                      command=elementy_do_wpisania)
dalej_button.grid(row=0, column=2)

# tworzenie przycisku LICZ, ktory wywoluje funkcje do liczenia wyznacznika
licz_button = Button(okno, text='Licz', width=7, font=("Arial", 9), background='#34404d', foreground="#ffffff",
                     command=liczenie_wyznacznika)
licz_button.grid(row=0, column=3, padx=5, pady=5)

wyznacznik = StringVar()

# tworzenie etykiety WYZNACZNIK
wyznacznik_label = Label(okno, text='det=', font=("Arial", 9))
wyznacznik_label.grid(row=0, column=4, pady=5, padx=5)

# tworzenie pola do wypisania wartosci wyznacznika
wyznacznik_entry = Entry(okno, width=10, textvariable=wyznacznik)
wyznacznik_entry.grid(row=0, column=5, pady=5, padx=5)

okno.mainloop()
