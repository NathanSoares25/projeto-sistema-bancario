# Nthbank - Sistema Bancário Simulado

Bem-vindo ao Nthbank! Este é um sistema bancário simulado desenvolvido para fins educacionais e de aprendizado. Com o Nthbank, você pode simular operações bancárias básicas, como sacar, depositar, exibir extrato, criar usuário, criar conta, listar contas e sair do aplicativo.

## Sobre o Projeto

Este é um projeto de desafio de código da plataforma DIO referente ao bootcamp **Python AI Backend Developer** em parceria com a Vivo.

Para mais informações, estarei deixando o link na seção *Links*

Link com projeto corrigido para comparações de código na seção *Links*

## Versions

### V1.0

- Criado uma mensagem de boas vindas e um input para coletar o nome do usuário.
- Criado menu com opções Depositar, Sacar, Exibir extrato e sair.
- Adicionado a função **Sleep** da biblioteca **Time** para dar um pause depois de cada comando.


### V2.0

- Código completamente refeito para melhorias.
- Removido o input parar coletar o nome de usuário no inicio do programa (será criado um sistema melhor).
- Removido blocos de códigos **depositar**, **sacar** e **exibir extrato** .
- Criado as funções **menu** **depositar**, **sacar** e **exibir extrato** e a função principal **main** para melhorar a leitura e compreensão do código.
- Alterado o menu com adições de novas funções: **Nova conta**, **Novo usuário** e **Listar contas**(OBS: ainda será implementada essas funções).

**OBS:** Posso ter feito mais alterações, porém, talvez eu tenha esquecido de colocar rs. O código ainda contém alguns bugs por ter sido totalmente refeito e que pretendo resolver logo para deixar o código ok para ser executado.

**OBS 2:** Como já mencionei, estou aprendendo e usando este projeto para treinamento e aprendizado então pode ser que certos trechos eu possa ter 'colado' do repositório oficial de onde estou estudando. Mas sempre buscando alterar uma coisinha aqui ou ali.

### V2.1

- Corrigido o bug onde o limite de saque diário não estava sendo contabilizado.

### V2.1.1

- Adicionado as novas funções **Criar usuário**, **Criar conta** e **Listar contas**
- **Criar usuário:** O usuário primeiramente precisar criar um usário para depois ter permissão para criar uma conta.
- **Criar conta:** Após ter criado o usuário, será solicitado o CPF para a criação da conta, se o CPF constar na lista de usuário a conta será criada, se não, a operação irá indicar para criar um usuário primeiro.
- **Listar contas:** Mostra uma lista de contas criadas.

### V3.0
- Código **TOTALMENTE** refeito para aplicar os aprendizados em Programação Orientada a Objetos.
- Implementação inicial das classes Cliente, PessoaFisica, Conta, ContaCorrente, Historico, Transacao, Saque, e Deposito.
- Definição de métodos e propriedades para manipulação de contas bancárias, transações e clientes.
- Implementação de lógica para realizar saques e depósitos em contas, verificando saldo disponível e limites.
- Adição de histórico de transações em cada conta.
- Implementação de classes abstratas para transações bancárias e métodos abstratos para registrar transações.

### V3.1
- Correção de bugs na lógica de saque em contas correntes.
- Adição de contagem de saques diários e verificação de limite de saques em contas correntes.
- Melhoria na documentação e organização do código.
- Adição de representação textual (__str__) para objetos da classe ContaCorrente.

**Não Desista!:** POO pra mim ta sendo super complicado, não estou conseguindo entender tudo de primeira, já pensei em desistir pois não tava me sentindo confortável porque não estava entendendo o assunto(ainda to sem entender kkk). Então eu tive que ver a resolução do código do desafio, mas isso não vai me desanimar em tentar compreender o assunto e essa linguagem maravilhosa que eu amo. Não posso e não quero desistir de seguir a carreira dos meus sonhos! Então se você ler isso, não desista! A caminhada é dificil mas lá no futuro renderá bons resultados.

### V4.0

#### Mudanças na Classe ContaCorrente:
- Antes: O método __init__ da classe ContaCorrente recebia parâmetros limite e limite_saques, mas o atributo limite estava sendo atribuído como self._limite e o atributo limite_saques estava sendo atribuído como self.limite_saques.
- Depois: Foi corrigido para que os atributos limite e limite_saques sejam atribuídos corretamente como self._limite e self._limite_saques, respectivamente.

#### Mudanças na Classe Historico:
- Antes: A classe Historico estava definindo o atributo transacoes como uma lista vazia chamada _transacoes.
- Depois: O nome do atributo foi corrigido para _transacoes para evitar colisão com o nome do método transacoes, que também retorna o histórico de transações.
#### Outras Mudanças:
- As importações foram organizadas para melhor legibilidade.
- As mensagens de erro e sucesso foram padronizadas para melhor consistência no código.

### V5.0
### Adição do Iterador de Contas:
- **Classe Adicionada:** ContasIterador
- **Finalidade:** Permite iterar sobre uma lista de contas e exibir informações formatadas de cada conta.

### Controle de Limite de Transações Diárias para Clientes:
- **Método Adicionado:** realizar_transacao na classe Cliente
- **Finalidade:** Limita o número de transações diárias que um cliente pode realizar, exibindo uma mensagem de erro caso exceda o limite.

### Relatório de Transações por Tipo no Histórico:
- **Método Adicionado:** gerar_relatorio na classe Historico
- **Finalidade:** Permite gerar um relatório das transações filtrando por tipo (saque ou depósito).

### Filtragem de Transações do Dia no Histórico:
- **Método Adicionado:** transacoes_do_dia na classe Historico
- **Finalidade:** Retorna as transações realizadas no dia atual, baseando-se na data registrada nas transações.

### Decorator para Logging de Transações:
- **Decorator Adicionado:** log_transacao
- **Finalidade:** Registra em log o momento e o tipo de transação realizada.

### Atualizações e Correções Menores:
- Ajustes nos métodos sacar e depositar das classes Conta e ContaCorrente para refletir as novas regras de transação e histórico

## V5.1
### Indentação do Texto Formatado em ContasIterador
- Alteração no método __next__ da classe ContasIterador, a string formatada estava com indentação extra.Foi essa indentação para que a saída seja formatada corretamente.

### Lógica de Transações Diárias em Cliente
- Na função realizar_transacao, a lógica limita a quantidade de transações diárias. Foi adicionado um parâmetro opcional para configurar esse limite (limite_diario).

### Melhorias na Função recuperar_conta_cliente
- Feito ajuste na função recuperar_conta_cliente para retornar **None** se o cliente não tiver conta, em vez de imprimir uma mensagem de erro diretamente.

### Melhorias na Saída de Mensagens
- Feita a Padronização e melhoria das mensagens de sucesso e erro para uma experiência de usuário mais consistente e clara.
### Encapsulamento e Validação Adicional
- Implementação de validações adicionais, para garantir que valores negativos não sejam aceitos em transações.

## Funcionalidades

- **Depositar:** Permite que você deposite dinheiro na sua conta.
- **Sacar:** Permite que você retire dinheiro da sua conta. Obs: Existe um limite diário de 3 saques, e o usuário pode sacar até 500, caso passe esse valor a operação é negada.
- **Exibir Extrato:** Mostra o extrato da sua conta, incluindo transações passadas.
- **Sair:** Encerra o aplicativo.
- **Criar usuário:** Cria um novo usuário.
- **Criar conta:** Cria uma nova conta.
- **Listar contas:** Lista todas as contas criadas.

## Contribuindo

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

- [@NathanSoares25](https://www.github.com/NathanSoares25)

## 🔗 Links
[![Bootcamp DIO](https://img.shields.io/badge/-Bootcamp%20DIO-0077B5?style=for-the-badge&logo=gitbook&logoColor=white)](https://web.dio.me/track/coding-future-vivo-python-ai-backend-developer?tab=about)
[![Desafio corrigido](https://img.shields.io/badge/-Desafio%20DIO%20Corrigido-0077B5?style=for-the-badge&logo=gitbook&logoColor=white)](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nathan-soares-b9092b1b4/)
