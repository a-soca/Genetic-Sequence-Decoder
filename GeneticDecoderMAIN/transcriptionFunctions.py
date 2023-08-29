complimentaryPairDict = {"C": "G",
"A" : "T",
"T" : "A",
"G" : "C"
}

codonDict = { "CCC": "Pro",
"CCA": "Pro",
"CCU": "Pro",
"CCG": "Pro",
"CAC": "His",
"CAA": "Glm",
"CAU": "His",
"CAG": "Glm",
"CUC": "Leu",
"CUA": "Leu",
"CUU": "Leu",
"CUG": "Leu",
"CGC": "Arg",
"CGA": "Arg",
"CGU": "Arg",
"CGG": "Arg",
"ACC": "Thr",
"ACA": "Thr",
"ACU": "Thr",
"ACG": "Thr",
"AAC": "Asn",
"AAA": "Lys",
"AAU": "Asn",
"AAG": "Lys",
"AUC": "Ile",
"AUA": "Ile",
"AUU": "Ile",
"AUG": "Met",
"AGC": "Ser",
"AGA": "Arg",
"AGU": "Ser",
"AGG": "Arg",
"UCC": "Ser",
"UCA": "Ser",
"UCU": "Ser",
"UCG": "Ser",
"UAC": "Tyr",
"UAA": "STOP",
"UAU": "Tyr",
"UAG": "STOP",
"UUC": "Phe",
"UUA": "Leu",
"UUU": "Phe",
"UUG": "Leu",
"UGC": "Cys",
"UGA": "STOP",
"UGU": "Cys",
"UGG": "Trp",
"GCC": "Ala",
"GCA": "Ala",
"GCU": "Ala",
"GCG": "Ala",
"GAC": "Asp",
"GAA": "Glu",
"GAU": "Asp",
"GAG": "Glu",
"GUC": "Val",
"GUA": "Val",
"GUU": "Val",
"GUG": "Val",
"GGC": "Gly",
"GGA": "Gly",
"GGU": "Gly",
"GGG": "Gly"
}

def DNA2cDNA(DNA):
	cDNASeq= ""
	for i in range(len(DNA)):
		cDNASeq = cDNASeq + complimentaryPairDict[DNA[i]]
	return cDNASeq
	
def cDNA2mRNA(cDNA):
	mRNASeq = ""
	for i in range(len(cDNA)):
		if cDNA[i] == "T":
			mRNASeq = mRNASeq + "U"
		else:
			mRNASeq = mRNASeq + cDNA[i]
	return mRNASeq
	
def mRNA2AminoAcid(mRNA):
	aminoAcidSeq = []
	for i in range(int(len(mRNA)/3)):
		aminoAcidSeq.append(codonDict[str(mRNA[i*3:i*3+3])])
	return aminoAcidSeq
