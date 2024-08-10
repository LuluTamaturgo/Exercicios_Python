***
# <h1 align="center"> Tipos de Dados String </h1>
***
Em python trabalhamos com tipo de dados String. Nas linguagens de alto nível sua manipulação geralmete é fácil.

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Criando e manipulando texto:
***

Em python, existe várias formas de declarar e formatar strings:

~~~~python
"Texto de Exemplo"
'Texto de Exemplo'
'''Texto de Exemplo'''
"Texto de 'Exemplo'"
'Texto de "Exemplo"'
~~~~

as ' (aspas simples) e " (aspas duplas) são os formatos principais, sendo possível também usa-las internamente, como mostra nos exemplos acima.
O uso das multiline strings (três aspas simples ou três aspas duplas), são utilizadas em comentários dentro do código ou, formatações de saída de console:

~~~~python
'''
Inserindo comentário dentro do código com aspas simples: 
atribuindo valores nas variáveis num1 e num2.
'''

num1 = 10
num2 = 5

soma = num1 + num2

print(f'''
Resultado da soma dos valores inseridos:\n {num1} + {num2} = {soma}''')
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
Resultado da soma dos valores inseridos:
 10 + 5 = 15
~~~~

o **\n** representa uma quebra de linha. Observe que, os números estão na linha abaixo.

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Estrutura de uma string:
***

As Strings são compostas por indices. Cada caracter da String é indentificado por um indice, sendo o primeiro caracter com indice 0, e os seguintes seguirá a sequência.

Exemplo:

~~~~python
palavra = 'Python'
~~~~

Estamos atribuindo na variável palavra a palavra Python.
Sabemos que, o primeiro indice tem o valor 0 (zero) então:

~~~~python
P y t h o n
0 1 2 3 4 5 
~~~~

a palavra python possui 6 caracteres (6 letras).

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Manipulando Strings:
***

Para que possamos manipular uma string, precisamos obter algumas informações:

* Tamanho;
* Posição;
* Trechos por posição;

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Função LEN:

A função len nos retorna o número de elementos de um objeto.
Podendo ser usada para contar número de itens em uma lista, número de caracteres em uma string, chaves em dicionário, entre outros.

Sintaxe:

len(objeto)

~~~~python
palavra = 'Python'
print(f'A palavra Python possui {len(palavra)} letras')
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
A palavra Python possui 6 letras
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Manipulando strings acessando por possição de indice - slice notation:

Conforme vimos anteriormente, o primeiro caracter possui o indice 0 e, como resultado da função len a palavra python tem 6 caracteres (0 até 5).
Outra forma manipularmos as strings é por suas posições:

~~~~python
palavra = 'Python'

print(f'Caracter que ocupa a posição 2: {palavra[2]}')
print(f'Caracter que ocupa a posição 5: {palavra[5]}')
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
Caracter que ocupa a posição 2: t
Caracter que ocupa a posição 5: n
~~~~


<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Acessando trechos da string:

Também podemos manipular string informando o trecho especifico dentro do tamanho do objeto.

~~~~python
palavra = 'Python'

print(f'Selecionando o intervalo do primeiro indice até o terceiro: {palavra[:4]}')
print(f'Selecionando o intervalo iniciando do 2° indice até o ultimo: {palavra[2:]}')
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
Selecionando o intervalo do primeiro indice até o terceiro: Pyth
Selecionando o intervalo iniciando do 3° indice até o ultimo: thon
~~~~

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Outras operações:
***

* X está em Y: x in y
    *  aqui será retornado resuldao booleano: Falso ou Verdadeiro

~~~~pytho
palavra = 'Python'

#aqui ele está buscado se existe a letra 'm' na palavra python:
print('m' in palavra)
~~~~
<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:
~~~~python
False
~~~~

Ou seja o resultado é falso pois, não existe m na palavra Python.

* Não está em Y:  not in y
   * aqui ele nega a existência do item de busca ao objeto referenciado

~~~~python
palavra = 'Python'

#aqui ele nega a existencia da letra m na palavra python:
print('m' not in palavra)
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
True
~~~~

* Concatenação: +
  * Tem como objetivo juntar duas strings

~~~~python
print('Estudando' + 'python')
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
Estudando Python
~~~~

* Repetição: 'caractere' * valor que será repetido
   * quando queremos iserir algum caracter especial várias vezes

~~~~python
print('#' * 15) #sera repetido o simbolo 15 vezes
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>resultado:

~~~~python
###############
~~~~

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Principais métodos:
***

Na documentação é possivel encontrar todos os métodos utilizados na string:
https://docs.python.org/3.3/library/stdtypes.html#

Neste momento vamos abordar os métodos mais comuns:

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Captalize:
Ajusta a primeira letra para Maiscula:

~~~~python
print('python'.capitalize())
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
Python
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Count:
quantifica quantas vezes um elemento se repete na string:

~~~~python
print('Estudando Python'.count('o')) #aqui será retornando quantas vezes é apresentado a letra o:
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
2
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Startwith:
analisa se a primeira letra atendente a condição de inicialização:

exemplo: vamos analisar se a primeira letra da palavra inicia com p minusculo:

~~~~python
print('Python'.startswith('p'))
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
False
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> endswith:
analisa se a ultima letra atende a condição apresentada, analisando a ultima letra da string:

exemplo: vamos solicitar para que analise se a ultima letra da palavra termina com a letra 'n':
~~~~python
print('Python'.endswith('n'))
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
True
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Split:
cria uma lista

~~~~python
print('Estudando Python'.split())
print(type('Estudando Python'.split()))
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
['Estudando', 'Python']
<class 'list'>
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Join:
converte uma lista em string

~~~~python
lista = ['Estudando', 'Python']
print(" ".join(lista))
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
Estudando Python
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Replace:
substitui um elemento de uma string por outro:

~~~~python
frase = 'Python 24'.replace('24', '2024')
print(frase)
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font>
~~~~python
Python 2024
~~~~

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Aqui, aprendemos:
***

- [x] Implementação de strings;
- [x] sua estrutura;
- [x] como manipular as strings;
- [x] metodos mais comuns utilizados em strings; 
