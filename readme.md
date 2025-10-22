1--
Na classe CarroPasseio, não é explicado pelo enunciado como calcular a depreciação. O texto só diz "Adiciona taxa no cálculo" sem dizer como é o calculo antes da taxa. Sendo assim, fica dificil ser muito preciso a não ser que se use um pouco de imaginação. 
Além disso, não achei que fazia muito sentido o metódo ter como entrada o número de anos de uso, se já temos como atributo da classe o ano de fabricação e podemos usar o modulo datetime para obter o ano atual.
Sendo assim, eu criei o método do jeito que eu achei mais lógico, e deixei o jeito pedido no enunciado em forma de comentário.

2--
O enunciado diz qual é a tipagem das variaveis, mas como sabemos, Python é uma linguagem dinamicamente tipada. Ainda assim, pesquisei e descobri que é um boa prática usar "type hints", ou seja, anotações sobre o tipo das variáveis para facilitar a compreensão de quem for fazer manutenção do código no futuro. Eu pus type hints em todas as váriaveis da super classe, mas apenas nas variaveis novas das subclasses.
Além disso, usei nas variáveis que são passadas ao serem chamados os métodos.

3--
O nome do método registrar_vistorias sugere que há uma intenção de não apenas exibir informações, mas também registrá-las. Sendo assim criei uma lista de vistorias e a cada vez que o método é usado, é adicionada à lista uma tupla contendo motivo e multa. Usei uma tupla, porque uma vez ocorrida, a vistoria não muda mais. Além disso, a multa é definida a principio como zero.

4--
No main, eu instanciei dois carros de passeio, sendo um para testar o exibir detalhes detalhado e um o exibir detalhes simples. Já o caminhão instanciei apenas um, criei 3 vistorias e depois mandei printar a lista de vistorias

5--
Acho que era isso que você queria, professor. Não sei se ficou faltando alguma coisa aqui no readme.
Eu sei que fiz algumas coisas um pouco diferente e outras um pouco além do que foi pedido, mas espero que o conjunto final esteja bom.

Obrigado, 
    Victor Merling.
