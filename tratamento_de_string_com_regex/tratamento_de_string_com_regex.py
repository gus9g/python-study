import re

path = str(input("Diretorio: "))

pathRE = re.sub(r'/', r'\\', path)

print("Antes do Tratamento ---> " + str(path))
print("Depois do Tratamento ---> " + str(pathRE))

