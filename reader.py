def readSequence(fastaPath):
    # Read into memory
    lines = open(fastaPath).read().strip().split('\n')

    # When first line start with ">" character
    if lines[0][0] is '>':
        # just remove that line from memory
        del lines[0]

    # Join lines into one long sequnce and force uppercase
    sequence = ''.join(lines).upper()

    # Validate sequence
    for char in sequence:
        allowedChars = ['A', 'C', 'G', 'T']
        if char not in allowedChars:
            raise Exception("Invalid character in sequence: ".join([char]))

    return sequence
