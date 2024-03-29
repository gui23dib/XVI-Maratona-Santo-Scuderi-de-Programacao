# Problema G

## Mágica

**Nome do arquivo fonte: magica. [c | cpp | java | py ]**

Um aprendiz de mágico está querendo realizar um novo número de magia. Ele está pensando em um número de magia que envolve matemática, daqueles em que é possível adivinhar um número escolhido.
Pensando em um número n, depois um outro número A que divide n, depois um outro número B que não é divisor de n, e agora outro número C que é múltiplo de n, e outro D que não é múltiplo de n. Será que conhecendo A, B, C e D é possível descobrir qual era o número original n?
Perceba que pode existir mais de uma solução, ou nenhuma solução!

### Entrada

A entrada é formada por uma única linha contendo 4 valores inteiros A, B, C, e D ( 1 ≤ A, B, C, D ≤ 10°).
possível.

### Saída

Consiste em uma única linha, retornando o menor n possível, ou -1, caso não exista n possivel.

### Exemplos

| Entrada    | Saída |
|------------|-------|
| 2 12 8 2   | 4     |
| 3 4 60 105 | 6     |
