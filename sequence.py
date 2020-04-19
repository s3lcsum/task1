from counter import findGcParis, percent


def countSequence(seq):
    result = {
        'seq': seq
    }

    result['gc'] = findGcParis(result['seq'])
    result['at'] = len(seq) - result['gc']

    result['prop_gc_at'] = percent(result['gc'], result['at'])
    result['prop_at_gc'] = 100 - result['prop_gc_at']

    return result


def verboseSequences(seq):
    results = []

    for i in range(len(seq)):
        results += [countSequence(seq[i])]

    print(
        "{:^5}{:^12}|{:^12}|{:^12}|{:^12}| Sequence"
            .format("Len", "Sum GC", "Sum AT", "% GC", "% AT")
    )
    print('---------------------------------------------------')

    for res in results:
        length = res['gc'] + res['at']
        print(
            "{:^5}|{:^12}|{:^12}|{:^12.2f}|{:^12.2f}| {:}"
                .format(length, res['gc'], res['at'], res['prop_gc_at'], res['prop_at_gc'], res['seq'])
        )
    print("\n\n\n", '')  # Add 3 break lines after printing table
