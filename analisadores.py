import funcoes


def assimetria(x):
    a = funcoes.assimetria(x)
    if a > 0:
        text = "A distribuição apresenta caracteristica de assimetria positiva, com valor de assimetria {}."
    elif a < 0:
        text = "A distribuição apresenta caracteristica de assimetria negativa, com valor de assimetria {}."
    else:
        text = "A distribuição apresenta caracteristica simétrica, com valor de assimetria {}."
    return text.format('%.5f' % a)


def curtose(x):
    c = funcoes.curtose(x)
    if c > 0.263:
        text = "Por curtose temos que a distribuição normal é platicúrtica com valor: {}"
    elif c < 0.263:
        text = "Por curtose temos que a distribuição normal é leptocúrtica com valor: {}"
    else:
        text = "Por curtose temos que a distribuição normal é mesocúrtica com valor: {}"
    return text.format('%.5f' % c)
