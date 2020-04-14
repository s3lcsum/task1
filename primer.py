
baseComplementary = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C",
    "N": "N"
}


def makeComplementary(sequnce):
    complementary = ""
    for char in sequnce:
        complementary += baseComplementary[char]

    return complementary


def getPrimerForward(sequnce, length):
    return sequnce[:length]


def getPrimerReverse(sequnce, length):
    # Reverse length and minus 1, because arrays are counted from 0
    return makeComplementary(sequnce[:(length * -1) - 1:-1])