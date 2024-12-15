***
# <h1 align="center"> Funções : Print e Input </h1>
***
<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⚠</font></font> Funções Integradas (built-In):

Para iniciarmos, primeiramente, devemos entender que dentro do python existe funções built-In (funções integradas).
Elas são um conjunto de comandos pré-definidos que executam tarefas específicas, podendo ser chamadas para executar uma ação ao longo do código.

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> A função `print()` em Python: :
***
**Imagine que você está conversando com um amigo e quer mostrar algo para ele.** Você pode apontar para um objeto, fazer um gesto ou simplesmente dizer o que você quer mostrar.

**Em programação, a função `print()` faz um papel parecido.** Ela serve para mostrar algo na tela do computador, como se você estivesse "apontando" para um resultado e dizendo: "Olha só o que eu encontrei!".

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> Para que serve a função print ( )?

- **Exibir mensagens:** Você pode usar o `print()` para mostrar mensagens na tela, como "Olá, mundo!", "O resultado da conta é:" ou qualquer outra frase que você queira.
- **Mostrar o valor de variáveis:** Se você tiver um número guardado em uma variável, pode usar `print()` para ver qual é esse número.
- **Verificar o funcionamento do seu código:** Às vezes, você quer saber se uma parte do seu programa está funcionando corretamente. O `print()` te ajuda a "espiar" o valor das variáveis em diferentes pontos do código.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> Como usar a função `print()`?

É muito simples! Você escreve `print()` seguido de parênteses e, dentro dos parênteses, coloca o que você quer mostrar. Por exemplo:

`print("Olá, mundo!")`

Isso vai mostrar a mensagem "Olá, mundo!" na tela.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> Você também pode mostrar o valor de uma variável:
~~~~
nome = "Ana"
print(nome)
~~~~

Esse código vai mostrar o nome "Ana" na tela.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> **E se você quiser mostrar o resultado de uma conta?**

~~~~
numero1 = 10
numero2 = 5
resultado = numero1 + numero2
print(resultado)
~~~~

Isso vai mostrar o número 15 na tela, que é o resultado da soma.

A função `print()` é uma ferramenta essencial em Python, pois ela te permite ver o que o seu programa está fazendo a cada passo. É como ter uma janela para dentro do seu código!

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> A função `input()` em Python: Uma porta de entrada para seus dados:
***
Imagine que você está criando um programa que precisa de informações do usuário. Por exemplo, um programa que calcula a área de um círculo precisa saber o raio. É aí que a função `input()` entra em cena!

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> E o que a função `input()` faz ??

- **Pausa o programa:** Quando o programa encontra a função `input()`, ele para e espera que você digite algo.
- **Captura a entrada do usuário:** Tudo o que você digitar será armazenado em uma variável.
- **Converte a entrada em texto:** Por padrão, a função `input()` considera tudo que você digita como um texto, mesmo que você digite um número.

  
<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> Como usar a função `input()`?

É bem simples! Você escreve `input()` seguido de parênteses e, dentro dos parênteses, você coloca uma mensagem para o usuário. Essa mensagem vai aparecer na tela e explicar o que você espera que o usuário digite.

~~~~
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
~~~~

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **O que acontece no código acima?**

1. O programa pergunta: "Digite seu nome: ".
2. Você digita seu nome e pressiona Enter.
3. O nome que você digitou é armazenado na variável `nome`.
4. O programa imprime na tela: "Olá, [seu nome]!"


<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">✏</font></font> Por que a função `input()` é útil??

- **Interação com o usuário:** Permite que seus programas sejam mais dinâmicos e personalizáveis.
- **Coleta de dados:** Você pode coletar informações importantes para os seus cálculos ou decisões dentro do programa.

<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⏺</font></font> **Mas atenção:**

- **A entrada é sempre texto:** Mesmo que você digite um número, a função `input()` vai considerá-lo como texto. Para fazer cálculos com números, você precisa converter o texto para um número, usando funções como `int()` ou `float()`.
- **Segurança:** Se você estiver criando um programa que recebe informações sensíveis, como senhas, é importante tomar cuidados para proteger esses dados.

A função `input()` é uma ferramenta poderosa em Python que permite que seus programas interajam com o usuário. Com ela, você pode criar programas mais personalizados e interessantes.

### <font style="vertical-align: inherit;"><font style="vertical-align: inherit;">⭕</font></font> Aqui, aprendemos:
***

- [x] Funções integradas (built-In);
- [x] Função `print()` : definição e utilização;
- [x] Função `input()` : definição e utilização;


