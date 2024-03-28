# Problema D

## ProsaGPT

**Nome do arquivo fonte: prosa. [c | cpp | java | py ]**

A empresa mineira OpenUAI está desenvolvendo uma aplicação para troca de mensagens de texto com seu modelo de Inteligência chamado ProsaGPT. Cada mensagem trocada precisa ser classificada se ela possui boa, média ou pouca informação. Uma frase com boa informação contém todas as letras do alfabeto presentes na frase. Uma frase com média informação contém ao menos metade das letras do alfabeto, e menos que isso é um frase com pouca informação.

### Entrada

A primeira linha deve conter um inteiro N (1 ≤ N ≤ 20), indicando o número de frases a serem classificadas. Na sequência, as N frases com no máximo 500 caracteres em cada frase, contendo letras minúsculas, espaços em branco, pontuações e qualquer outro caractere.

### Saída

Para cada frase de entrada, imprima uma linha contendo a classificação "boa informacao",
"media informacao" ou "pouca informacao", conforme o caso.

### Exemplos

| Entrada                                                                                                                                                                                                            | Saída                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| 2<br> ola, como vai?<br> vou bem tomando um cafe com pao de queijo.                                                                                                                                                | <br> pouca informacao<br> media informacao                                                              |
| 5<br> o que oce ta fazendo?<br> to proseando com o prosagpt<br> que trem de prosagpt eh esse, soh? eh de comer?<br> eh a inteligencia artificial da openuai<br> meu prefixo de radio amador eh yzg4jkl6bcqtuvnwyzs | <br> pouca informacao<br> pouca informacao<br> media informacao<br> media informacao<br> boa informacao |
