import numpy as np
import matplotlib.pyplot as plt


def desenhaRetaCaso1(f, p, q, g):
    (yp, xp) = p
    (yq, xq) = q
    s = float(yq - yp) / (xq - xp)

    for x in range(xp, xq + 1):
        y = int(round(yp + s * (x - xp)))
        f[y, x] = g


def desenhaRetaCaso2(f, p, q, g):
    (yp, xp) = p
    (yq, xq) = q
    s = float(yq - yp) / (xq - xp)
    d = 0.0
    y = yp

    for x in range(xp, xq + 1):
        f[y, x] = g
        d += s
        if d >= 0.5:
            y += 1
            d -= 1.0


def desenhaRetaCaso3(f, p, q, g):
    (yp, xp) = p
    (yq, xq) = q
    dx, dy = xq - xp, yq - yp
    s = 2 * dy
    c = 2 * dx
    d = 0
    y = yp
    rastro = []

    for x in range(xp, xq + 1):
        f[y, x] = g
        rastro.append((x, y, d))
        d += s
        if d >= dx:
            y += 1
            d -= c

    return rastro


def plotar8Simetricos(f, xc, yc, x, y, g):
    pontos = (
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x),
    )

    for px, py in pontos:
        f[py, px] = g


def desenhaCirculo(f, centro, r, g):
    (yc, xc) = centro
    x = 0
    y = r
    d = 1 - r

    while x <= y:
        plotar8Simetricos(f, xc, yc, x, y, g)
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1


def main():
    p = (2, 2)
    q = (6, 8)
    imagem_reta = np.zeros((10, 10), dtype=int)
    rastro = desenhaRetaCaso3(imagem_reta, p, q, 1)

    print("Rastreio Bresenham (x, y, d antes da atualização):")
    for estado in rastro:
        print(estado)

    print("\nQuestão 1: equivalência entre os Casos 2 e 3")
    print(
        "Definindo D = 2*dx*d, somar dy/dx a d equivale a somar "
        "2*dy a D. O teste d >= 0.5 equivale a D >= dx, e subtrair "
        "1 de d equivale a subtrair 2*dx de D. Assim, os dois casos "
        "tomam as mesmas decisões e desenham os mesmos pixels, mas o "
        "Caso 3 usa apenas inteiros. No exemplo, (x=5, y=4) tem d=0. "
        "O Caso 1 pode divergir em empates exatos: round() do Python "
        "arredonda para o inteiro par, enquanto o Caso 2 usa d >= 0.5."
    )
    print("\nQuestão 2: linha com espessura uniforme")
    print(
        "Use a reta como eixo central de uma faixa: calcule a normal "
        "perpendicular à direção da reta, desloque os extremos em "
        "e/2 para cada lado e rasterize o retângulo (ou quadrilátero) "
        "formado."
    )
    print("\nQuestão 3: simetria do círculo")
    print(
        "Calcula-se um octante e refletem-se seus pontos nos outros "
        "sete: cerca de 8 vezes menos cálculos de posição, ou 7/8 "
        "(87,5%) a menos, desconsiderando pontos repetidos nos eixos "
        "e na diagonal."
    )

    imagem_circulo = np.zeros((10, 10), dtype=int)
    desenhaCirculo(imagem_circulo, (5, 5), 4, 1)

    fig, eixos = plt.subplots(1, 2, figsize=(8, 4))
    for eixo, imagem, titulo in (
        (eixos[0], imagem_reta, "Bresenham: p=(2,2), q=(6,8)"),
        (eixos[1], imagem_circulo, "Círculo: centro=(5,5), r=4"),
    ):
        eixo.imshow(imagem, cmap="gray_r", vmin=0, vmax=1, origin="upper")
        eixo.set_title(titulo)
        eixo.set_xlabel("x")
        eixo.set_ylabel("y")
        eixo.set_xticks(range(10))
        eixo.set_yticks(range(10))
        eixo.grid(True, color="lightgray", linewidth=0.5)

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()