***
# <h1 align="center"> Operadores e Ordem de precedência </h1>
***

Imagine que você está montando um sanduíche. Você tem pão, queijo, presunto e tomate. A ordem em que você coloca os ingredientes vai influenciar o sabor final do sanduíche. Em programação, os operadores funcionam de forma similar.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **O que são operadores?**

Operadores são símbolos especiais que realizam operações em valores. Por exemplo, o operador + serve para somar, o operador - para subtrair, o operador * para multiplicar, e assim por diante.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Tipos de Operadores:**

:white_check_mark: Aritméticos: Usados para realizar cálculos matemáticos :

| + | soma |
| --- | --- |
| - | subtração |
| * | multiplicação |
| / | divisão |
| % | módulo (resto da divisão) |

:white_check_mark: Comparação: Usados para comparar valores:

| == | para verificar se dois valores são iguais |
| --- | --- |
| != | para verificar se são diferentes |
| > | maior |
| < | menor |
| >= | maior e igual |
| <= | menor e igual |

:white_check_mark: Lógicos: Usados para combinar condições lógicas

| and | retorna verdadeiro somente quando as condições são verdadeiras |
| --- | --- |
| or | retorna verdadeiro quando uma das condições é verdadeira |
| not | nega a condição ou seja, se a condição for verdadeira, ela será falsa |

:white_check_mark: Atribuição: Usados para atribuir um valor a uma variável
| = | inseri um valor em uma variável, exemplo: nome = 'Maria' |
| --- | --- |

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Ordem de Precedência::
***
Assim como na matemática, os operadores em programação têm uma ordem de execução. Essa ordem é chamada de precedência. Por exemplo, a multiplicação é realizada antes da adição.
Imagine a expressão:

~~~~
2 + 3 * 4
~~~~

Para confirmamos os ajustes que iremos executar logo em seguida, iremos precisar da função type, cujo o objetivo é retornar o tipo de dado de uma variavel.


### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Armazenando os números em uma variável:
***

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Inteiro:**

~~~~python
#atribuindo os valores 1 e 25 nas variáveis n e num:
n = 1
num = 25

print(n)
print(num)

1
25
~~~~

Utilizando a função type para imprimir na tela o tipo de dado das variaveis *n* e *num*:

~~~~python
print(type(n))
print(type(num))

<class 'int'>
<class 'int'>
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Flutuantes (float):**

~~~~python
n = 5.5
num = 350.19

print(type(n))
print(type(num))

<class 'float'>
<class 'float'>
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Complex:**

~~~~python
num = 1+2j
num_comp = complex(1, 2) + 2

print(num)
print(num_comp)

print(type(num))
print(type(num_comp_1))


(1+2j)
(3+2j)

<class 'complex'>
<class 'complex'>
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Conversão:**

* Para converter qualquer tipo de dado para o tipo que desejamos basta executar os passos abaixo:

Declarar a variável e, inserir o tipo de dado que desejo converter, entre parêntese, inserir o dado que estou recebendo;
~~~~python
numero_int_1 = int('50') #declarando 50 como string e, convertendo para inteiro
numero_int_2 = int(10.5) #recebendo um valor float e convertendo para inteiro

numero_flo_1 = float('55.10')
numero_flo_2 = float(10)

print(type(numero_int_1))
print(type(numero_int_2))

print(type(numero_flo_1))
print(type(numero_flo_2))

<class 'int'>
<class 'int'>
<class 'float'>
<class 'float'>

~~~~

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Operadores aritméticos:
***

Segue abaixo o conjunto base de operadores aritméticos em python:

~~~~python
+  :    adição :                     a + b
-  :    subtração:                   a - b
*  :    multiplicação:               a * b
/  :    divisão em ponto flutuante:  a / b
// :    divisão sem ponto flutuante: a // b
%  :    resto:                       a % b
** :    potência                     a ** b
~~~~

Exemplo:

~~~~python
soma = 5 + 2
subtracao = 10 - 3
multiplicacao = 3 * 3
divisao = 12 / 2
divisao_facionada = 10 // 3
resto = 10 % 3
potencia = 2 ** 8


print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisao_fracionada)
print(resto)
print(potencia)


7
7
9
6.0
3
1
256

~~~~

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Aqui, aprendemos:
***

- [x] Quais são os tipos de dados númericos em python;
- [x] Como reprensatá-los;
- [x] Função type( );
- [x] Operadores aritméticos; 
