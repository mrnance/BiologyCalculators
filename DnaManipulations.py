def reverseComplement(sequence):
    revseq = ''

    for i in reversed(sequence.lower()):
        if i == "a":
            revseq += "t"
        if i == "c":
            revseq += "g"
        if i == "t":
            revseq += "a"
        if i == "g":
            revseq += "c"
        if i == "u":
            revseq += "a"

    return revseq.upper()
