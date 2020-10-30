import sqlite3
from sqlite3 import Error

def cria_conexao(diretorio):
	conexao = None
	try:
		conexao = sqlite3.connect(diretorio)
		print("Conexão realizada com o Banco de Dados")
	except Error as e:
		print(f"O erro {e} ocorreu")
	return conexao

def execucao_query(conexao, query):
	cursor = conexao.cursor()
	try:
		cursor.execute(query)
		conexao.commit()
		print("Query realizada com o Banco de Dados")
	except Error as e:
		print(f"O erro {e} ocorreu")

def execucao_leitura_querry(conexao, query):
	cursor = conexao.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"O erro {e} ocorreu")

if __name__ == "__main__":
	#Cria conexão
	conexao = cria_conexao("rede_social.sqlite")
	#Cria tabela de usuários
	criar_tabela_usuarios = """
	CREATE TABLE IF NOT EXISTS usuarios (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	sexo TEXT,
	cidade TEXT
	);
	"""
	execucao_query(conexao, criar_tabela_usuarios)
	#Cria tabela de posts
	criar_tabela_posts = """
	CREATE TABLE IF NOT EXISTS posts (
	id INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	texto TEXT NOT NULL,
	usuario_id INTEGER NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
	)
	"""
	execucao_query(conexao, criar_tabela_posts)

	#Crias tabela de comentarios
	criar_tabela_comentarios = """
	CREATE TABLE IF NOT EXISTS comentarios (
	comentario TEXT NOT NULL,
	usuario TEXT NOT NULL,
	id INTEGER NOT NULL,
	FOREIGN KEY (id) REFERENCES posts (id)
	)
	"""
	execucao_query(conexao, criar_tabela_comentarios)

	#Cria usuarios

	cria_usuarios = """
	INSERT INTO
		usuarios (nome, idade, sexo, cidade)
	VALUES
		('Maycom', 27, 'M', 'Florianópolis' ),
		('Jaqueline', 12, 'F', 'Florianópolis' ),
		('Marcos', 17, 'M', 'São José' ),
		('Daniel', 4, 'M', 'Palhoça' ),
		('Alexandre', 7, 'M', 'Palhoça' ),
		('Felipe', 10, 'M', 'Florianópolis' ),
		('Gabriel', 19, 'M', 'Biguaçu' )
	"""
	#execucao_query(conexao, cria_usuarios)

	#Criar posts
	criar_post = """
	INSERT INTO
		posts(id, titulo, texto, usuario_id)
	VALUES
		(1, 'Como fazer uma append numa lista?', 'Use o método .append', 1),
		(2, 'Problema no Sublime', 'Sublime não executa', 3)
	"""
	#execucao_query(conexao, criar_post)
	
	#Criar comentario

	criar_comentarios = """
	INSERT INTO
		comentarios(comentario, usuario, id)
	VALUES
		('Muito interesantes essa matéria', 'Manuel', 1)
	"""
	execucao_query(conexao, criar_comentarios)

	selecionar_usuarios = "SELECT * from usuarios"
	usuarios = execucao_leitura_querry(conexao, selecionar_usuarios)


	'''for usuario in usuarios:
		print (usuario[1])'''
