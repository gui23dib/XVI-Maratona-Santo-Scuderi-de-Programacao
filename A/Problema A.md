# Problema A

## Avião

**Nome do arquivo fonte: aviao. [c | cpp | java | py ]**

Você está competindo em um concurso de aviões de papel ao ar livre e deseja prever até onde seu avião de papel voará. O seu design tem um fator fixo K, de tal forma que, se a velocidade do avião for pelo menos K, ele subirá. Se a sua velocidade for inferior a K, ele descerá.
Aqui está como seu avião de papel voará:
  • Você começa jogando seu avião de papel com uma velocidade horizontal de V a uma altura de H. Há um vento externo soprando com uma força de S.
  • Enquanto H > 0, repita a seguinte sequência:
  • Aumente V por S. Em seguida, diminua V por max(1, LV/10J). Observe que LV/10] é o valor de V/10, arredondado para baixo para o inteiro mais próximo, caso não seja um número inteiro.
  ° Se V ≥ K, aumente H em 1.
  • Se 0 < V< K, diminua H em 1. Se H for zero após a diminuição, defina V como zero.
  • Se V≤ 0, defina H e V como zero.
  • Seu avião agora viaja horizontalmente por V unidades.
  • Se S> 0, diminua S em 1.
Calcule até onde o avião de papel viajará horizontalmente.

### Entrada

A única linha de entrada contém quatro inteiros H, K, V e S (1 ≤ H, K, V, S ≤ 10°), onde H é a altura inicial, K é o fator fixo, V é a velocidade inicial e S é a força do vento.

### Saída

Imprima um único inteiro, que é a distância percorrida pelo avião de papel horizontalmente.
Pode ser mostrado que essa distância é sempre um número inteiro.

### Exemplos

| Entrada         | Saída  |
|-----------------|--------|
| 1 1 1 1         | 1      |
| 2 2 2 2         | 9      |
| 1 2 3 4         | 68     |
| 314 159 265 358 | 581062 |
