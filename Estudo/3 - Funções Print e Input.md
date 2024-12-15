***
# <h1 align="center"> Funções : Print e Input </h1>
***
<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Funções Integradas (built-In):

Para iniciarmos, primeiramente, devemos entender que dentro do python existe funções built-In (funções integradas).
Elas são um conjunto de comandos pré-definidos que executam tarefas específicas, podendo ser chamadas para executar uma ação ao longo do código.

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> A função print() em Python: :
***
**Imagine que você está conversando com um amigo e quer mostrar algo para ele.** Você pode apontar para um objeto, fazer um gesto ou simplesmente dizer o que você quer mostrar.

**Em programação, a função `print()` faz um papel parecido.** Ela serve para mostrar algo na tela do computador, como se você estivesse "apontando" para um resultado e dizendo: "Olha só o que eu encontrei!".
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

