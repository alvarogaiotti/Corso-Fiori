from redeal import *
import itertools
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

Deal.set_str_style("long")

mani = [
    "642 KQ5 8653 T75",
    "K85 JT964 942 J8",
    "AQJ A82 AKQJ AK6",
    "T973 73 T7 Q9432",
    "J3 QT832 J9 KJT4",
    "7654 64 AK A8532",
    "QT982 J9 T863 Q9",
    "AK AK75 Q7542 76",
    "AK63 K7 7653 AT4",
    "J842 842 KQ9 QJ2",
    "T7 AQ6 AT842 K85",
    "Q95 JT953 J 9763",
    "T82 Q 7643 QJT43",
    "K64 J653 AK2 K62",
    "AQJ9 T842 JT9 87",
    "753 AK97 Q85 A95",
    "AK7 A952 AK6 A74",
    "T9832 KJ4 J82 K9",
    "QJ T76 97543 J86",
    "654 Q83 QT QT532",
    "KJT8 T842 953 32",
    "752 A73 AJ4 KQJ6",
    "964 KJ9 T2 T9854",
    "AQ3 Q65 KQ876 A7",
    "AKT9 Q6 874 7653",
    "632 K42 K952 KJT",
    "QJ8 A73 AQJT Q84",
    "754 JT985 63 A92",
    "AT43 QJT74 J6 T7",
    "KQ2 K6532 AK AKJ",
    "J9 9 QT984 98542",
    "8765 A8 7532 Q63",
]

mani = [H(x.upper()) for x in mani]

posizioni = (Seat["N"], Seat["E"], Seat["S"], Seat["W"])
predeal = dict()
counter = 0
while mani:
    for seat in posizioni:
        predeal[seat] = mani.pop(0)
    deal = Deal.prepare(predeal)()
    counter += 1
    print(f'[Board "{counter}"]')
    print(deal._pbn_str())
