mRNABaseDict = { 1: "C",
2: "A",
3: "U",
4: "G",
}

for i in range(4):
	for j in range(4):
		for k in range(4):
			print("\"" + mRNABaseDict[i+1] + mRNABaseDict[j+1] + mRNABaseDict[k+1] + "\"" + ": ")
