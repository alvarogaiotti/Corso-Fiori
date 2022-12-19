"""Crea coppie per il Torneo Finale con allievi."""
import random


giocatori = [
    "Bruno",
    "Alvaro",
    "Mauro",
    "Walter",
    "Aurora",
    "Cesarino",
    "Ermanno",
    "Gianni",
    "Nicola",
    "Francesco",
]

allievi = [
    "Raffaella",
    "Livietta",
    "Marika",
    "Alessandro",
    "Aldo",
    "Nadia",
    "Laura",
    "Francesco",
]


def crea_coppie(allievi, giocatori) -> None:
    for num_coppia in range(8):
        giocatore = random.choice(giocatori)
        allievo = random.choice(allievi)
        print(f"{allievo} giocherà in coppia con {giocatore}")
        giocatori.remove(giocatore)
        allievi.remove(allievo)
        if num_coppia == 7:
            print(f"{giocatori[0]} giocherà in coppia con {giocatori[1]}")


crea_coppie(allievi, giocatori)
input()