import transcriptionFunctions as t
import generationFunctions as g

print("---------------------\n\tGenetic Decoder\n---------------------")
match int(input("Generate or enter a genetic sequence? [1/2] : ")):
	case 1:
		length = int(input("Please enter the number of bases : "))
		DNASeq = g.DNASeqGenerator(length)
	case 2:
		DNASeq = input("Please enter a genetic sequence : ")
		
cDNASeq = t.DNA2cDNA(DNASeq)

mRNASeq = t.cDNA2mRNA(cDNASeq)

aminoAcidSeq = t.mRNA2AminoAcid(mRNASeq)

print("\nDecoded genetic sequence :\n")
for i in range(int((len(DNASeq))/3)):
	print(DNASeq[i*3] + "═══" + cDNASeq[i*3] + " ┐")
	print(DNASeq[i*3+1] + "═══" + cDNASeq[i*3+1] + " |-> " + aminoAcidSeq[i])
	print(DNASeq[i*3+2] + "═══" + cDNASeq[i*3+2] + " ┘")
	if aminoAcidSeq[i] == "STOP":
		print("\n~~~~~~~~~~~~~~~\n")
		
print("\nEnd of Sequence.")
