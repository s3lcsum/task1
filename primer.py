from counter import findGcParis, percent

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


# Difine when proportion is acceptable
def isGood(gn_pf, gn_pr):
    return gn_pf - gn_pr < 8


def findGoodPrimer(pf, pr):
    gc_pf = findGcParis(pf)  # Find GC in forward primer for later calulations
    gn_pf = percent(gc_pf, len(pf))  # NOTICE: This raise exception when length of pf is zero

    gc_pr = findGcParis(pr)

    for _ in range(len(pr)):
        gn_pr = percent(gc_pr, len(pr))  # Calulate good number for current pr sequence

        if not isGood(gn_pf, gn_pr):
            tmp_pr = pr[:-1]  # Get rid last nucleotide and put into temporary sequencce variable
            gc_pr = findGcParis(tmp_pr)  # Find GC pairs in the temporary sequence

            if gc_pr <= 0:  # When there is no more GC in temporary sequence
                print("There is no good number for primers")
                break  # Leaveing for loop with last sequence (not the temporary)

            pr = tmp_pr  # If condition is true this will assing temporary into main variable

    return pf, pr  # Return both primers (forward and reverse)


def calculateTemperature(seq):
    gc = findGcParis(seq)
    at = len(seq) - gc

    return (gc * 4) + (at * 2)