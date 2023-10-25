# BS Programming Language

## *POR QUE*?

Sabe aquela pessoa que programa sem pensar em que vai ler o código depois? Escreve aquele spaghetti delicioso que nem ela entende depois? Não gosta de identação nem quebras de linha? Não conhece ninguém assim? Cuidado, você pode ser essa pessoa.

Essa linguagem é inspirada nelas.

## Simplicidade
`BS` é uma linguagem simples, nada de *frescuras desnecessárias* como funções e classes ou else if e else, só o necessário.

`BS` possui apenas um loop, o equivalente ao while, e um condicional, o equivalente ao if, *sem else ou else if*.

`BS` também é uma linguagem para os *programadores preguiçosos*. Pode arrancar o ENTER e o TAB do seu teclado, pois você não vai usar!

## Sintaxe
A sintaxe é simples, coloque um `.` no fim das declarações.

Quando utilizando um while ou if, abra seu corpo com `..` e feche com `...`

### EX.: Programa que recebe `x` e `n`, calcula `x` elevado a `n` e exibe o resultado no console:
```
x ingual pega . n ingual pega . res ingual 1 . enquando n maioque 0 . .. res ingual res mutiprica x . n ingual n menus 1 . ... gozpe res .
```
### EX.: Programa que recebe `a` e compara seu valor com a constate `abc`, exibindo `errado` até que o valor de `a` seja `ingual` a `abc` e, por fim, exibindo `certo` no console:
```
a ingual pega . enquando a naoengual falah abc falah . .. gozpe falah errado falah . a ingual pega . ... gozpe falah certo falah .
```

## Ordem das Operações

As operações, tanto matemáticas quando lógicas, não ocorrem na mesma ordem que nas outras linguagens.

Em `BS`, a ordem é sempre da direita para a esquerda.

| BS | Python |
|:-:|:-:|
| `a * (b - c)` | (a * b) - c |
| `a + (b / (c * d))` | a + ((b / c) * d) |

Por exemplo, a operação *3 + 2 * 4 - 1 / 10*, que seria executada na ordem *3 + ((2 * 4) - (1 / 10))* nas outras linguagens, em `BS`, é executada na ordem *3 + (2 * (4 - (1 / 10)))*.

### Calculo acima em código:

#### BS

```
mult ingual 2 mutiprica 4 . calculo ingual 3 mas mult menus 1 cortaem 10 .

// explicação
// calcula primeiro a multiplicação e guarda em "mult"
// faz o restante do calculo e guarda em "calculo"
```

#### Python

```
calculo = 3 + 2 * 4 - 1 / 10
```

## Operadores Lógicos

| BS | Python |
|:-:|:-:|
| `ingual` | = |
| `engual` | == |
| `naoengual` | != |
| `maioque` | > |
| `menoque` | < |
| `i` | and |
| `o` | or |

## Operadores Aritméticos

| BS | Python |
|:-:|:-:|
| `mas` | + |
| `menus` | - |
| `mutiprica` | * |
| `cortaem` | / |
| `sobrah` | % |

## While

| BS | Python |
|:-:|:-:|
| `enquando a maioque b . .. a ingual a menus 1 ...` | while a > b: a = a - 1 |

## if

| BS | Python |
|:-:|:-:|
| `se a maioque b . .. gozpe falah a é maior que b falah .` | if a > b: print("a é maior que b") |

## strings

Para declarar uma constante do tipo texto, coloque o texto entre `falah`, da mesma forma que você faria com aspas.

`falah` esse é meu texto `falah`

## I/O
### Input
`pega` é o equivalente do *input()* no Python

O `pega` tenta transformar qualquer input em um float, se falhar nisso, usa o valor inserido como texto.

### Output
`gozpe` é o equivalente do *print()* no Python
