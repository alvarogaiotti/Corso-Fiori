from redeal import *
from redeal import dds
from redeal.global_defs import Seat, Suit, Card, Rank, Strain

predeal = {
    Seat["S"]: H("742 KQJ6 K2 8653"),
    Seat["N"]: H("AQ8 743 A743 AK4"),
    Seat["E"]: H("95 A985 956 QJT9"),
    Seat["W"]: H("KJT63 T2 QJT8 72"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "1"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["S"]: H("K952 853 AQ5 K65"),
    Seat["N"]: H("QJT63 A62 K6 QJ3"),
    Seat["E"]: H("A4 KQJ4 J984 984"),
    Seat["W"]: H("87 T97 T732 AT72"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "2"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("KJT974 AT3 Q43 9"),
    Seat["W"]: H("53 Q865 JT9 AT52"),
    Seat["E"]: H("AQ6 K4 A865 KQJ7"),
    Seat["S"]: H("82 J972 K72 8643"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "3"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("432 JT97 AK98 52"),
    Seat["S"]: H("85 Q8 T7432 QT97"),
    Seat["W"]: H("KQJT6 5432 Q5 K8"),
    Seat["E"]: H("A97 AK6 J6 AJ643"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "4"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("T3 KT82 KQJ2 AJT"),
    Seat["W"]: H("874 J93 4 Q76532"),
    Seat["E"]: H("AKJ62 76 A953 98"),
    Seat["S"]: H("Q95 AQ54 T876 K4"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "5"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["S"]: H("K8 J96 T6432 832"),
    Seat["E"]: H("Q76 T3 J7 KQT964"),
    Seat["W"]: H("J543 AK54 KQ85 J"),
    Seat["N"]: H("AT92 Q872 A9 A75"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "6"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("8643 93 QJ6 T942"),
    Seat["W"]: H("AJT9 KQJ5 32 A87"),
    Seat["E"]: H("Q52 AT864 K98 J5"),
    Seat["S"]: H("K7 72 AT754 KQ63"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "7"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["W"]: H("QT94 93 QJ5 J653"),
    Seat["S"]: H("AJ76 QJT5 87 KQ8"),
    Seat["N"]: H("8532 876 63 AT72"),
    Seat["E"]: H("K AK42 AKT942 94"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "8"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("AQ6 KJ52 763 AKQ"),
    Seat["W"]: H("KJT92 Q3 QJT JT3"),
    Seat["E"]: H("754 AT64 98 9764"),
    Seat["S"]: H("83 987 AK542 852"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "9"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["S"]: H("KQT A62 9875 A98"),
    Seat["E"]: H("97432 J93 Q643 3"),
    Seat["W"]: H("J865 T AJ KJT542"),
    Seat["N"]: H("A KQ8754 KT2 Q76"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "10"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["S"]: H("K542 QJT9 J3 AJ5"),
    Seat["N"]: H("87 86 T8642 Q864"),
    Seat["W"]: H("AQJT A743 Q95 32"),
    Seat["E"]: H("963 K52 AK7 KT97"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "11"]\n{dealer()._pbn_str()}')

predeal = {
    Seat["N"]: H("KQ64 A65 AKJ73 4"),
    Seat["W"]: H("982 T32 952 KT92"),
    Seat["E"]: H("A7 KQJ74 T4 Q863"),
    Seat["S"]: H("JT53 98 Q86 AJ75"),
}
dealer = Deal.prepare(predeal)
print(f'[Board "12"]\n{dealer()._pbn_str()}')
