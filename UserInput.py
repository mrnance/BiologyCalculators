def checkPolymerType(inputString):
    polymerType = "unknown";
    notprotein = ("b", "j", "o", "u", "x", "z")
    notdna = (
    "b", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z")
    notrna = (
    "b", "d", "e", "f", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    dnacount = 0
    rnacount = 0
    proteincount = 0

    for i in inputString.lower():
        if i not in notdna:
            dnacount += 1
        if i not in notrna:
            rnacount += 1
        if i not in notprotein:
            proteincount += 1

    if len(inputString) == dnacount:
        return "DNA"
    if len(inputString) == rnacount:
        return "RNA"
    if len(inputString) == proteincount:
        return "Protein"
    else:
        return "Not a recognized biological polymer"



