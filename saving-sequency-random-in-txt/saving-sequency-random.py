# program by sequency of numbers random
from random import randint

# Create array
seqN = []
count = 0

limitSeqN = int(input("Informe um limite para a sequencia: \n"))

# Algorithim generate random sequency numbers
while len(seqN) != limitSeqN:
    numRand = randint(0, limitSeqN - 1)
    if numRand not in seqN:
        seqN.append(numRand)


#Escrita de arquivo TXT
with open('guardando-dados-python.txt','a') as fileW:
	fileW.write('\n\nSequencia de numeros aleatorios:\n')

	for i in seqN:
		fileW.write(str(i) + " ")

	fileW.close()

with open('guardando-dados-python.txt') as fileR:
	print(fileR.read())
	fileR.close()