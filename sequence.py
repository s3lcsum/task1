def verboseSequence(sequence, gc, at, proprtionGcAt, proprtionAtGc):
    if len(sequence) > 70:
        print(''.join(["Sequence: ", sequence[:65], "(...)"]))
    else:
        print(''.join(["Sequence: ", sequence]))

    print(
        "{:^12}|{:^12}|{:^12}|{:^12}"
        .format("Sum GC", "Sum AT", "% GC", "% AT")
    )
    print(
        "{:^12}|{:^12}|{:^12.2f}|{:^12.2f}"
        .format(gc, at, proprtionGcAt, proprtionAtGc)
    )
    print()
