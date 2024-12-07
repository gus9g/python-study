
read = open("59.html","r",encoding="utf-8") 
save = open("1Extracted.txt","a")

txtSearch = "<h3>"
incrementTxtSearch = len(txtSearch) + 0
# incrementTxtSearch = 0

for readLine in read:
	x = readLine.find(txtSearch)

	if readLine[x:][:len(txtSearch)] == txtSearch:
		# print(readLine[x+incrementTxtSearch:][:])
		save.write(readLine[x+incrementTxtSearch:][:] + "\n")


read.close
save.close