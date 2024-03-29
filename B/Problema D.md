# Problema B

## Bob não teria vencido

**Nome do arquivo fonte: bob. [c | cpp | java | py ]**

"Nós fecharemos em cerca de 5 minutos. Obrigado por visitar a academia Santo Scuderi hoje"
Com este anúncio, Alice e Bob pararam de jogar sua maratona de pedra-papel-tesoura no meio do décimo jogo. Cada jogador marca um ponto se sua jogada vence a jogada do outro jogador.
Cada jogo foi jogado seguindo a regra do primeiro-a-11, o que significa que quem marcar 11 pontos primeiro vence o jogo. Hoje, Bob venceu Alice por uma única partida; ele marcou 11 pontos primeiro em cinco jogos, enquanto Alice marcou 11 pontos primeiro em apenas quatro jogos.
Depois de examinar cuidadosamente como cada jogo foi jogado, Alice percebeu que poderia ter vencido mais jogos do que Bob se tivessem jogado sob regras ligeiramente diferentes, como primeiro-a-5 ou primeiro-a-8, em vez da regra regular de primeiro-a-11.
Dada a sequência de pontos marcados por Alice e Bob, determine todos os valores de K para
os quais Alice teria vencido mais jogos do que Bob sob a regra de primeiro-a-K.
Tanto Alice quanto Bob começam com zero pontos no início de um jogo. Assim que um jogador atinge K pontos, esse jogador vence o jogo e um novo jogo começa. Alice vence um jogo se ela marcar K pontos antes de Bob. Nenhum jogador vence o jogo se ele for interrompido pelo fechamento da academia antes que qualquer um dos jogadores atinja K pontos.

### Entrada

A única linha de entrada consiste em uma string de letras maiúsculas "A" ou "B", denotando quem marcou cada ponto desde o início da maratona de pedra-papel-tesoura. O comprimento da string está entre 1 e 2.000 letras, inclusive. "A" significa que Alice marcou o ponto, "B" significa que Bob marcou o ponto.

### Saída

Na primeira linha da saída, imprima o número de inteiros positivos K para os quais a regra do primeiro-a-K faria com que Alice vencesse mais jogos do que Bob. Se esse número não for zero, na próxima linha, imprima todos esses valores de K em ordem crescente, separados por espaços.

### Exemplos

| Entrada        | Saída       |
|----------------|-------------|
| BBAAABABBAAABB | 3<br> 3 6 7 |
| AABBBAAB       | 2<br> 2 4   |
