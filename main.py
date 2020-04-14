from reader import *
from counter import *
from primer import *
from sequence import *


# 1. Read .fasta file
# Get path to .fasta file
fastaPath = input("Path to .fasta file: ")

# Use function fromo "reader" package
sequence = readSequence(fastaPath)


# 2. Count sequence
gc = findGcParis(sequence)
at = findAtParis(sequence)
proprtionGcAt = percent(gc, at)
proprtionAtGc = percent(at, gc)

print('# Sequence:')
verboseSequence(sequence, gc, at, proprtionGcAt, proprtionAtGc)


# 3. Get primers
# First is primer forward
pf = getPrimerForward(sequence, 20)

pfGc = findGcParis(pf)
pfAt = findAtParis(pf)

ppfGc = percent(pfGc, pfAt)
ppfAt = percent(pfAt, pfGc)

print('# Primer forward:')
verboseSequence(pf, pfGc, pfAt, ppfGc, ppfAt)

# Second is primer reverse
pr = getPrimerReverse(sequence, 20)

prGc = findGcParis(pr)
prAt = findAtParis(pr)

pprGc = percent(prGc, prAt)
pprAt = percent(prAt, prGc)

print('# Primer reverse')
verboseSequence(pr, prGc, prAt, pprGc, pprAt)


# 4.
