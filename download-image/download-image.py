# CRIAR UM SCRIPT QUE UTILIZE UMA PLANILHA COM LINKS PARA BAIXAR PHOTOS 
# E SALVAR COM O NOME E TIPO INFORMADOS EM UMA COLUNA ESPECIFICA

try:
  import requests
except:
  import os
  os.system("pip install requests")
  print("Biblioteca Instalada - Execute Novamente")

imageURL = "https://external-preview.redd.it/K0CT6pvyCGPOFEyjfli8Y7hJUg5X_0IO86yasq0LCRY.jpg?auto=webp&s=f5b24a2a37993ea22ba3c4e68a870bbb0837265a"

with open('binary.png', 'wb') as imagem:
  resposta = requests.get(imageURL, stream=True)

  if not resposta.ok:
    print("Ocorreu um erro, status:" , resposta.status_code)
  else:
    for dado in resposta.iter_content(1024):
      if not dado:
          break

      imagem.write(dado)

    print("Imagem salva! =)")

