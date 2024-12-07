import json

save = open("new.json","a",encoding="utf-8") 

usuarios = [
			"Martin Vinicius", 22, "Belo Horizonte", "MG",
			"Isabel Amanda", 45, "Sao Paulo", "SP",
			"Tereza Renata", 33, "Barueri", "SP",
			"Helena Mendes", 15, "Osasco", "SP",
			"Benedito Oliver", 80, "Salvador", "BA",
			"Sueli Luzia", 24, "Carapicuiba", "SP"
			]


save.write("{ \"people\":")
save.write("[")

count = 0
while count <= len(usuarios)-4:
	if count >= 4:
		save.write(",")

	save.write("{")
	save.write("\"nome\":")
	save.write("\"" + str(usuarios[count]) + "\",")
	save.write("\"idade\":")
	save.write("\"" + str(usuarios[count+1]) + "\",")
	save.write("\"cidade\":")
	save.write("\"" + str(usuarios[count+2]) + "\",")
	save.write("\"estado\":")
	save.write("\"" + str(usuarios[count+3]) + "\"")
	save.write("}")
	count += 4

save.write("]")
save.write("}")

save.close