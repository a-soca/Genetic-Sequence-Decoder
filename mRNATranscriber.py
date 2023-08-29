cDNA = input("Please enter your complimentary DNA sequence : ")
mRNASeq = ""
for i in range(len(cDNA)):
    if cDNA[i] == "T":
        mRNASeq.append("U")
    else:
        mRNASeq.append(cDNA[i])

print(mRNASeq)
    