import UserInput
import DnaManipulations

sequence = input().upper()
polymerType = UserInput.checkPolymerType(sequence)


if polymerType == "Protein":
    print("Your polymer type is: ", polymerType)
    print("Your sequence is: Nterm-", sequence, "-Cterm")

if polymerType == "DNA" or "RNA":
    print("Your polymer type is: ", polymerType)
    print("Your sequence is: 5'- ", sequence, " -3'")
    reverseComplement = DnaManipulations.reverseComplement(sequence)
    print("Your reverse complement sequence is: 5'- ", reverseComplement, " -3'")

