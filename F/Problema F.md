# Problema F

## Cabotagem

**Nome do arquivo fonte: navio. [c | cpp | java | py ]**

A cabotagem é a navegação entre portos marítimos percorrendo a costa de uma determinada região, diferentemente do transporte marítimo de longo curso entre países de continentes diferentes.
Dessa forma os navios que fazem cabotagem fazem viagens mais curtas, levando dias entre um porto e outro, realizando muitas vezes viagens repetidas entre os mesmos portos. O navio de uma determinada empresa de logística faz sempre até três viagens entre portos diferentes com o seu tanque cheio. A empresa quer melhorar o planejamento dessas viagens com o objetivo de otimizar o consumo de combustível das viagens, essas viagens nem sempre levam o mesmo tempo devido as condições climáticas, e ficar navegando sempre de tanque cheio aumenta o peso do navio. A empresa precisa saber se é possível o navio ir e voltar, gastando o mesmo tempo pelo menos em uma das 3 viagens. Por exemplo, se os tempos que o navio leva para realizar as 3 viagens forem 5, 12 e 9 dias, ela pode decidir fazer uma viagem de 5 dias no sentido norte da costa até um determinado porto, depois retornar no sentindo sul para outro porto em uma viagem de 9 dias, dessa forma você teria passado pelo porto original sem atracar, e ainda teria 4 dias para chegar no próximo. Poderia também iniciar pela viagem de 12 dias em um sentido, depois retornar no sentindo contrário em uma viagem de 5 dias, e depois continuar no mesmo sentido por 9 dias, e teria passado pelo porto de origem e ainda teria 2 dias para chegar no próximo porto. A ordem das viagens é de livre escolha.
Dados os valores de tempo de cada viagem do navio, seu programa deve informar se é ou não possível realizar uma viagem entre os portos, gastando o mesmo tempo em pelo menos uma das viagens e, no máximo, realizando as três viagens.

### Entrada

A entrada é formada por uma linha contendo valores inteiros que representam os dias de cada viagem A, B e C (1 ≤ A, B, C ≤ 1000).

### Saída

A saída consiste na impressão de um caracter "S" se é possível realizar pelo menos 1 das
viagens gastando o mesmo tempo, ou "N" caso contrário.

### Exemplos

| Entrada   | Saída |
|-----------|-------|
| 22 5 22   | S     |
| 31 110 79 | S     |
| 45 8 7    | N     |
