# FUNÇÃO EXTRAIDA DO SITE JOURNALDEV
# https://www.journaldev.com/23666/python-string-find

def find_all_indexes(input_str, search_str):
    l1 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(search_str, index)
        if i == -1:
            return l1
        l1.append(i)
        index = i + 1
    return l1

# Função para abrir arquivo Excel
x = open("txt/organizacao-do-json.txt","r")

# filtros
nome   = "nome="
idade  = "idade="
cpf    = "cpf="
rg     = "rg="
dtnsc  = "dtnsc="
email  = "email="
cep    = "cep="
end    = "end="
numero = "numero="
bairro = "bairro="
cidade = "cidade="
estado = "estado="



for line in x:
	# POSICAO PALAVRA
	nomePos   = line.find(nome)  + len(nome)
	idadePos  = line.find(idade) + len(idade)
	cpfPos    = line.find(cpf)   + len(cpf)
	rgPos     = line.find(rg)    + len(rg)
	dtnscPos  = line.find(dtnsc) + len(dtnsc)
	emailPos  = line.find(email) + len(email)
	cepPos    = line.find(cep)   + len(cep)
	endPos    = line.find(end)   + len(end)
	numeroPos = line.find(numero)   + len(numero)
	bairroPos = line.find(bairro)   + len(bairro)
	cidadePos = line.find(cidade)   + len(cidade)
	estadoPos = line.find(estado)   + len(estado)

	# GERA ARRAY COM INDEXES DAS OCORRENCIAS DE PIP[|] NA STRING LINE ATRAVES DE FUNÇÃO IDENTIFICADORA
	n = []
	n.append(find_all_indexes(line, "|"))

	# EXIBIÇÃO DE COLUNA
	print(n[0][0])

	# TAMANHO PESQUISA CONTEUDO
	lenNomeCont   = n[0][0]
	lenIdadeCont  = n[0][1]
	lenCpfCont    = n[0][2]
	lenRgCont     = n[0][3]
	lenDtnscCont  = n[0][4]
	lenEmailcCont = n[0][5]
	lenCepCont    = n[0][6]
	lenEndCont    = n[0][7]
	lenNumeroCont = n[0][8]
	lenBairroCont = n[0][9]
	lenCidadeCont = n[0][10]
	lenEstadoCont = len(line)

	# IMPRESSÃO DE VISUALIZAÇÃO EM PROMPT PARA TESTE
	print(str( line[nomePos:]    [:lenNomeCont      - nomePos]   ))
	print(str( line[idadePos:]   [:lenIdadeCont     - idadePos]  ))
	print(str( line[cpfPos:]     [:lenCpfCont       - cpfPos]    ))
	print(str( line[rgPos:]      [:lenRgCont        - rgPos]     ))
	print(str( line[dtnscPos:]   [:lenDtnscCont     - dtnscPos]  ))
	print(str( line[emailPos:]   [:lenEmailcCont    - emailPos]  ))
	print(str( line[cepPos:]     [:lenCepCont       - cepPos]    ))
	print(str( line[endPos:]     [:lenEndCont       - endPos]    ))
	print(str( line[numeroPos:]  [:lenNumeroCont    - numeroPos] ))
	print(str( line[bairroPos:]  [:lenBairroCont    - bairroPos] ))
	print(str( line[cidadePos:]  [:lenCidadeCont    - cidadePos] ))
	print(str( line[estadoPos:]  [:lenEstadoCont    - estadoPos] ))
	print()