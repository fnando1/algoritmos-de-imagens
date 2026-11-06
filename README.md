# algoritmos-de-imagens

## Desenho de retas e círculo discreto

O script `algoritmos_desenho.py` implementa os três métodos de desenho de reta no primeiro octante e o círculo discreto por simetria de oito octantes. As coordenadas dos pontos são fornecidas como `(y, x)`, pois a matriz é indexada por linha e coluna: `f[y, x]`.

Instale as dependências e execute:

```bash
python -m pip install numpy matplotlib
python algoritmos_desenho.py
```

O programa imprime os estados `(x, y, d)` de Bresenham antes da atualização do erro em cada pixel e abre uma figura com a reta e o círculo.

### Rastreio da reta

Para `p=(2, 2)` e `q=(6, 8)`, os estados impressos são:

| x | y | d antes da atualização |
|---:|---:|---:|
| 2 | 2 | 0 |
| 3 | 3 | -4 |
| 4 | 3 | 4 |
| 5 | 4 | 0 |
| 6 | 5 | -4 |
| 7 | 5 | 4 |
| 8 | 6 | 0 |

Assim, no pixel `(x=5, y=4)`, o erro é zero.

### Questões de análise

1. No Caso 2, cada passo soma `dy/dx` a `d`. No Caso 3, o erro é escalado por `2*dx`: `D = 2*dx*d`. Portanto, somar `dy/dx` equivale a somar `2*dy` em `D`; o teste `d >= 0.5` equivale a `D >= dx`; e subtrair `1` equivale a subtrair `2*dx`. O estado inicial também corresponde (`D=0`). A trajetória de atualizações e os pixels é a mesma, sem floats ou divisões no Caso 3. Essa equivalência é entre os Casos 2 e 3; o Caso 1 usa o `round` do Python, que desempata meios exatos para o inteiro par, enquanto o Caso 2 usa limiar `>= 0.5`, então eles podem divergir em casos de empate exato.
2. Para uma espessura uniforme, representa-se a reta como o eixo central de uma faixa: calcula-se a direção perpendicular (normal) à reta e deslocam-se os extremos em metade da espessura para cada lado, formando um retângulo (ou quadrilátero) que então é rasterizado. O trecho/página do livro não foi fornecido, então esta resposta descreve a técnica geométrica usual para obter uma linha espessa.
3. Calcula-se um único octante e refletem-se os pontos nos outros sete. Isso reduz aproximadamente por um fator de 8 os cálculos de posição/distância em comparação a calcular cada octante separadamente, uma redução de 7/8 (87,5%). Pontos sobre eixos e diagonais podem coincidir, mas não alteram a simetria.