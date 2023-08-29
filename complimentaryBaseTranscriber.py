complimentaryPairs = {"C": "G",
"A": "T",
"T": "A",
"G": "C",
}

DNASeq= input("please enter DNA sequence : ")
cDNA= ""
for i in range(len(DNASeq)):
	cDNA.append(complimentaryPairs[DNASeq[i]])

print(cDNA)
