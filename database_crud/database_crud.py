# Importando conector MySQL, previamente instalado
import mysql.connector as connectorMSQL
from datetime import datetime

con = connectorMSQL.connect(user="root", database="cotacao_db")

cursor = con.cursor(buffered=True)

option = input("Informe a operação que voce quer realizar:\nS - Exibir resultados da tabela\nI - para inserir dados\nD- para remover dados\nU - para atualizar dados")
option = option.upper()

# SELECT TABLE
if option == 'S':
    query = "SELECT * FROM cotacao_db.produto"

    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        date_cotation = str(res[4])[:10]
        print(res[1] + ", " + str(res[3]) + ", " + date_cotation)

# INSERT DATA
if option == 'I':
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    date_cotation = dt_string
    print(date_cotation)

    name = input("Informe um nome.......:")
    link = input("Informe o link........:")
    price = input("Informe um preco.......:")
    messageAsk = input("Quer inserir uma mensagem(sim / nao)").lower()

    if messageAsk == 'sim':
        message = input("Informe uma mensagem..:")
    else:
        message = "N/A"

    query = "INSERT INTO cotacao_db.produto (nome_produto, link_produto, preco_produto, mensagem_produto, data_cotacao_produto) VALUES(%s,%s,%s,%s,%s)"
    value = (name, link, float(price), message, date_cotation)

    cursor.execute(query, value)

    con.commit()
    
# DELETE DATA
if option == "D":
    query = "SELECT * FROM cotacao_db.produto"

    cursor.execute(query)
    result = cursor.fetchall()
    for res in result:
        date_cotation = str(res[4])[:10]
        print(res[1] + ", " + str(res[3]) + ", " + date_cotation)

    id_produto = input("\n\nInforme o id do produto a ser removido")
    query = "DELETE FROM cotacao_db.produto WHERE id_produto = "+ id_produto
    
    cursor.execute(query)
    con.commit()

# UPDATE DATA
if option == "U":

    # LIST ALL PRODUCTS
    query = "SELECT * FROM cotacao_db.produto"

    cursor.execute(query)
    select_complete = cursor.fetchall()
    for res in select_complete:
        date_cotation = str(res[4])[:10]
        print(str(res[0]) + ", "+ res[1] + ", " + str(res[3]) + ", " + date_cotation)

    id_produto = input("Informe o ID do produto a ser modificado")

    # SELECT PRODUCT USER INFORM
    query = "SELECT * FROM cotacao_db.produto WHERE id_produto=" + id_produto
    cursor.execute(query)    
    product_alter_show = cursor.fetchall()

    print("\nSera perguntado se voce quer alterar cada um dos campos do produto selecionado, \nDigite\ns - sim\nn-nao\n")

    answer=input("Alterar nome [" + str(product_alter_show[0][1]) + "]? ")
    if answer == "s":
        name = input("nome atual [" + str(product_alter_show[0][1]) + "], informe o novo nome: ")
    else:
        name = product_alter_show[0][1]

    answer=input("Alterar link [" + str(product_alter_show[0][2]) + "]? ")
    if answer == "s":
        link = input("nome atual [" + str(product_alter_show[0][2]) + "], informe o novo link: ")
    else:
        link = product_alter_show[0][2]
        
    answer=input("Alterar preco [" + str(product_alter_show[0][3]) + "]? ")
    if answer == "s":
        price = input("nome atual [" + str(product_alter_show[0][3]) + "], informe o novo link: ")
    else:
        price = product_alter_show[0][3]
        
    answer=input("Alterar mensagem [" + str(product_alter_show[0][5]) + "]? ")
    if answer == "s":
        message = input("nome atual [" + str(product_alter_show[0][5]) + "], informe o nova mensagem: ")
    else:
        message = product_alter_show[0][5]
        

    # REFRESHING THE DATE OF COTATION
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    date_cotation = dt_string

    query = "UPDATE cotacao_db.produto SET nome_produto=%s, link_produto=%s, preco_produto=%s, mensagem_produto=%s, data_cotacao_produto=%s WHERE id_produto = %s"
    value = (name, link, price, message, date_cotation, id_produto)    
    cursor.execute(query, value)
    con.commit()


cursor.close()
con.close()