import mysql.connector

# o computador em que o banco de dados está rodando
# se estiver no mesmo computador que o sistema está rodando,
# pode ser # localhost ou 127.0.0.1
# A Porta padrão é 3306, mas verifique para ter certeza 
# se o seu sistema não está rodando em outra porta.
hostname = "127.0.0.1"
porta = "3306"

# as credenciais de acesso do
# SGBD que o sistema vai utilizar
# você pode criar um usuário e senha
# só pra isso ou, no caso, usar o
# usuário raiz do SGBD
usuario = "root"
senha =""

# o nome do esquema de banco de dados
# que o sistema estará utilizando
# aqui você deve preencher o nome
# que você deu ao seu banco de dados.
banco = "fittrack"

def conectar():
    conexao = mysql.connector.connect(host=hostname,
    port=porta,
    user=usuario,
    password=senha,
    database=banco)
    return conexao

# use essa função quando for executar um comando
# no banco de dados que precise alterar os dados
# lá dentro.
def executarComando(comando:str):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

# use essa função quando for executar uma consulta,
# ou seja, um comando que retorna dados do banco.
def executarConsulta(consulta:str) -> list:
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado