from reader import *
from counter import *
from primer import *

# 1. Read .fasta file
# Get path to .fasta file
fastaPath = input("Path to .fasta file: ")

# Use function fromo "reader" package
sequence = readSequence(fastaPath)

# Print results
print("Found sequence:")
print(sequence)

# Add empty break lines before next step
print("\n\n")


# 2. Count sequence
gc = findPairs(['G', 'C'], sequence)
at = findPairs(['A', 'T'], sequence)

proprtionGcAt = percent(gc, at)
proprtionAtGc = percent(at, gc)

print(''.join(["Zawartość GC w zadanej sekwencji wynosi: ", str(gc)]))
print(''.join(["Zawartość AT w zadanej sekwencji wynosi: ", str(at)]))
print(''.join(["GC stanowią ", str(proprtionGcAt), "% sekwencji"]))
print(''.join(["AT stanowią ", str(proprtionAtGc), "% sekwencji"]))

print("\n\n")

# 3. Get
primerForward = getPrimerForward(sequence, 20)
print('Found primer forward:')
print(primerForward)
print()

primerReverse = getPrimerReverse(sequence, 20)
print('Found complementary primer reverse')
print(primerReverse)
print()