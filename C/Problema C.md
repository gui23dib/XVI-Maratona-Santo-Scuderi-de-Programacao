# Problema C

## Fake News

**Nome do arquivo fonte: fake. [c | cpp | java | py ]**

Todos sabem do impacto que pode causar uma notícia falsa, chamada "fake news". Com o intuito de coibir as pessoas que propagam notícias falsas, as autoridades estudam penalizar os propagadores destas notícias de acordo com o alcance da determinada notícia falsa, descobrindo o decidiram colaborar
tempo mínimo em que uma fake atinge uma quantidade grande de visualizações. As redes sociais
autoridades, e cederam os registros de acesso das postagens
identificadas como fake, garantido o direito a privacidade de quem realizou o acesso, contendo o momento inicial em que a pessoa visualizou a fake pela primeira vez, e o intervalo de tempo em que ela visita novamente a mesma fake. Assim é preciso saber o tempo minimo em que essa notícia falsa levou para atingir uma quantidade V de visitas, como uma métrica de velocidade de propagação.

### Entrada

A primeira linha consiste em dois inteiros N e V (1 ≤ N ≤ 103, 1 ≤ V ≤ 103), que representa respectivamente a quantidade de pessoas que acessam a fake, e o alcance da fake dado uma quantidade mínima de visitas a fake. Na sequência, haverá N linhas contendo dois inteiros a, e bi (1 ≤ ai ≤ 10°, 1 ≤ bi ≤ 10°), representando respectivamente o primeiro momento em que a i-ésima pessoa visitou a fake, e quanto tempo em média essa fake era visitada novamente por essa mesma pessoa.

### Saída

Deve conter um inteiro representando o primeiro momento em que a fake atingiu a marca de
V visitas, determinando assim a velocidade em que ela foi propagada.

### Exemplos

| Entrada               | Saída |
|-----------------------|-------|
| 1 5<br> 5 3           | 17    |
| 2 10<br> 5 3<br> 10 4 | 22    |
