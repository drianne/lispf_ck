<h1>brainfuckCompiler</h4> <br>
<p align="center">    
    <img src="http://i66.tinypic.com/72zho7.jpg" width=130 height=130>
</p>

## Contribuidores
| Nome	| Matrícula	|
|--|--|
| Adrianne Alves da Silva | 16/0047595 |
| Letícia de Souza | 15/0015160 |


## Apresentação

Este repositório apresenta um lexer e parser de Lispf_ck, escritos em linguagem python. Eles fazem parte de uma atividade apresentada como avaliação parcial da disciplina de Compiladores do curso de Engenharia de software da Universidade de Brasília (UnB), Campus de Engenharias - Faculdade do Gama (FGA).

## Sobre a Linguagem

Lisp é uma linguagem de programação que foi projetada a fim de realizar processamento de dados simbólicos, sendo considerada uma linguagem formal matemática. Ela e uma linguagem funcional que representa o código como lista, de maneira que os elementos são separados por espaços atraves de uma notaç~ao prefixa, em que o primeiro elemento representa uma funç~ao e os demais s~ao argumentos da mesma. Essa linguagem foi utilizada por um tempo pela comunidade de inteligência artificial. Entretanto, nesse repositório será desenvolvido um parser para a linguagem Lispf_ck, uma variante da linguagem brainf_ck que combina a semântica do brainf_ck com outros recursos.

De maneira simplista, a Lispf_ck e uma brainf_ck em termos de limitaç~oes, mas em uma notaç~ao diferente. Ex:

BrainFuck : ,+[.-]
Lispf_ck: (do read inc (loop print dec))


### Caracteres

Como ´e uma linguagem diretamente relacionada com brainf_ck, podemos utilizar o alfabeto de brainfuck para demonstrar o de Lispf_ck. Tal que, temos em brainf_ck:

| Caractere | Significado  |
|---|---|
| > | Incremento do ponteiro  |
| < | Decremento do pronteiro  |
| + | Incremento do byte |
| - | Decremento do byte |
| . | Imprimir o dado |
| , | Entrada de um byte |
| [ | Início de um Laço |
| ] | Fim de um laço de repetição |

E em Lispf_ck teriamos: 

| Caractere | Significado  |
|---|---|
| [...] | (loop ...)  |
| > | right |
| < | left |
| + |  inc |
| - | dec |
| . | print |
| , | read |

## Como Contribuir

Para contribuir com o desenvolvimento, é preciso que o colaborador crie o seu próprio Fork e envie um pull request com a contribuição para a branch master do projeto. As alterações serão analisadas e incorporadas ao compilador em caso de aprovação.
