import os

from reader import *
from primer import *
from sequence import *

# 1. Read .fasta file
# Get path to .fasta file
fastaPath = os.getenv('FASTA')

# Use function from "reader" package
seq = readSequence(fastaPath)

# 2. Count sequence
print('# Sequence:')
verboseSequences([seq])

# 3. Get primers
# First is primer forward
pf = getPrimerForward(seq, 18)
print('# Primer forward:')
verboseSequences([pf])

# Second is primer reverse
pr = getPrimerReverse(seq, 25)
print('# Primer reverse')
verboseSequences([pr])

# 4. Find
pf, pr = findGoodPrimer(pf, pr)
print('# Primer')
verboseSequences([pf, pr])

t_pf = calculateTemperature(pf)
print("Melting temperature for primer forward is {}°C".format(t_pf))

t_pr = calculateTemperature(pr)
print("Melting temperature for primer reverse is {}°C".format(t_pr))

avg_t = (t_pf + t_pr) / 2
if abs(avg_t - t_pf) > 4:  # When difference between average and forward temperature are higher than 4
    print("Better would be PCR with temperatures between {}°C and {}°C".format(avg_t - 4, avg_t + 4))
else:
    print("Proposed temperature:", avg_t)


# 5. Connect to database
