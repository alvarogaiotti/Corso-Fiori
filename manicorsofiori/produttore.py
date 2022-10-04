from redeal import *
import itertools
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

Deal.set_str_style("long")

mani = [
    "ak63 a64 kq a863",
    "75 875 ajt52 952",
    "qjt92 j93 98 jt4",
    "84 kqt2 764 kq7",
    "kq63 k97 k86 t84",
    "j4 qjt63 aq54 93",
    "at5 a84 jt73 ak2",
    "9872 52 92 qj765",
    "akq6 jt7 q92 t63",
    "75 a632 kjt43 aj",
    "JT9432 Q84 A6 K8",
    "8 k95 875 q97542",
    "Jt97 AK 9643 764",
    "542 97653 J75 AK",
    "863 84 AK2 t9853",
    "AKQ QJt2 Qt8 QJ2",
    "Ak2 kq52 akj a64",
    "8764 A qt9542 q5",
    "j953 jt97 86 t82",
    "qt 8643 73 kj973",
    "a54 kqj9 a64 t86",
    "t9832 72 92 9432",
    "j6 8643 k83 akq5",
    "kq7 at5 qjt75 j7",
    "kqj92 987 q9 qj3",
    "a6 ak52 t42 8752",
    "t85 j3 8653 akt9",
    "743 qt64 akj7 64",
    "653 j43 873 jt97",
    "t984 t952 92 k65",
    "j7 a876 jt654 q2",
    "akq2 kq akq a843",
]
mani = [H(x.upper()) for x in mani]

posizioni = (Seat["N"], Seat["S"], Seat["E"], Seat["W"])
predeal = dict()
counter = 0
while mani:
    for seat in posizioni:
        predeal[seat] = mani.pop(0)
    deal = Deal.prepare(predeal)()
    counter += 1
    print(f'[Board "{counter}"]')
    print(deal._pbn_str())
