from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://gamingboss000.blogspot.com/2011/03/lista-de-tesouros-do-uncharted.html"

html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

cd = bs.find_all('h3', class_='js-guide-title')
lista = bs.find_all('div', class_='guide-section-content')

cdTemp = []
listaTemp = []

for cd in lista:
	if cd.get_text() != "":
		listaTemp.append(cd)

for cd in cd:
	if cd.get_text() != "":
		cdTemp.append(cd)

# for i in range(len(cdTemp)):
	# print(cdTemp[i].get_text())

# print(listaTemp)
for i in range(len(listaTemp)):
	x = listaTemp[i].find('li')
	print(x.get_text())