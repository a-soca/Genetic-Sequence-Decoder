import random

randCodonsDict = { 1: "C",
2: "A",
3: "T",
4: "G"
}

def DNASeqGenerator(length):
	DNASeq = ""
	for i in range(length):
		DNASeq = DNASeq + randCodonsDict[random.randint(1,4)]
	return DNASeq
