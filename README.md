# Devfit - Documentation

#### Este projeto tem como principal objetivo possibilitar a facilidade na administração de uma empresa fictícia cujo nome é DevFit. Neste projeto, foram usadas as linguagens Python e SQL, em conjunto com a extensão mysql-connector-python, para possibilitar a comunicação entre o aplicativo e o banco de dados através da linguagem de programação supracitada.

### Funções do programa:
##### O aplicativo é um CRUD(Create, Read, Update & Delete). Logo, suas funções estão explícitas, a saber: Cadastrar(criar), Ler(Consultar), Atualizar e Excluir.

----

##### - Silent patch | 23/02/2025 
#####  Senhas agora são cadastradas em forma de hash(criptografadas) Ao iniciar o programa pela primeira vez, o cadastro é requerido e o primeiro acesso, realizado. 
##### SQL query adicionada aos arquivos
##### - Silent patch | 24/02/2025
##### Nova função utilizando hashlib em `./login.py`, que também foi importada para o arquivo `./funcoes_de_cadastro.py` para realização da criação de hash no ato de cadastro de novo usuário.
---
### Demo do app
###### Segue algumas imagens do aplicativo em funcionamento

#### Tela inicial:
![home](./img/home.png)

#### Exemplo de consulta
###### obs: O mesmo padrão serve para todos as outras funcionalidades, seja de listagem, edição ou exclusão. O programa executa uma consulta precipuamente e, em seguida, o usuário segue as instruções para executar a ação desejada.

![constulta de alunos](./img/exemplo_consulta.png)

#### Login
###### Uma tela de cadastro semelhante irá aparecer ao executar o programa pela primeira vez, visto que não há usuário algum no banco de dados. Tais credenciais serão usadas para o login no sistema, posteriormente.

![login](./img/login.png)

---
### Equipe responsável pelo projeto
###### Abaixo segue a tabela contendo os membros da equipe, bem como suas atribuições.

|Membros da equipe|Função|
|---|---|
|Abraão F. Santos|Desenvolvedor I|
|Diego Silva|Desenvolvedor II|
|Fernanda Nascimento| Desenvolvedor III|
|Robson Francisco|Desenvolvedor IV|
|Ana Clara|Desenvolvedor Jr.|
---

### DEVFIT | SOBRE
###### <strong>Visão:</strong> Ser a academia líder no mercado fitness para  oferecendo um ambiente inovador e especializado onde os membros podem melhorar sua saúde física e mental enquanto seguem a rotina intensa de trabalho.

###### <strong>Missão:</strong> Ajudar os nossos alunos a alcançarem seu melhor potencial físico e mental, proporcionando treinos personalizados e experiências de bem-estar que se encaixam nas suas necessidades de rotina, criando um equilíbrio entre corpo e mente.​
---

###### "*O sucesso nasce do querer, da determinação e persistência em se chegar a um objetivo. Mesmo não atingindo o alvo, quem busca e vence obstáculos, no mínimo fará coisas admiráveis*." 
###### - José de Alencar