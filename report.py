import analisadores
import funcoes
import plots


def gerar(aerodromo, mes, data):
    with open("report-{}-{}.md".format(aerodromo, mes), 'w') as f:
        f.write('''---
geometry: margin=2cm
output: pdf_document
---
''')
        f.write("# Relatório\n")
        f.write("## Aerodromo: {}\n".format(aerodromo))
        f.write("## Periodo: {}/{}\n\n".format(mes[4:6], mes[:4]))
        f.write("## 1 - Temperatura\n")
        f.write("Durante esta seção teremos como alvo de estudo a variavél de temperatura (dada em graus Celsius) em "
                + " um determinado aerodromo pelo periodo de 1 mês. Os dados são coletados hora a hora, assim temos a "
                + "seguinte tabela que apresenta a média, mediana, moda, variância, desvio padrão e o coeficiente de "
                + " variação de cada dia.\n\n\n")
        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        dia = 0
        for d in data['temperatura']:
            dia += 1
            f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
                str('%02d' % dia) + "/" + mes[4:6] + "/" + mes[:4],
                '%.3f' % funcoes.media(d),
                '%.3f' % funcoes.mediana(d),
                '%.3f' % funcoes.moda(d),
                '%.3f' % funcoes.variancia(d),
                '%.3f' % funcoes.desvio_padrao(d),
                '%.3f' % funcoes.coeficiente_variacao(d),
            ))
        f.write('\n\n')

        f.write("Em seguida são apresentadas a média, mediana, moda, variância, desvio padrão e coeficiente de "
                + "variação do mês todo.\n\n\n")

        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
            mes[4:6] + '/' + mes[:4],
            '%.3f' % funcoes.media([funcoes.media(i) for i in data['temperatura']]),
            '%.3f' % funcoes.mediana([funcoes.mediana(i) for i in data['temperatura']]),
            '%.3f' % funcoes.moda([funcoes.moda(i) for i in data['temperatura']]),
            '%.3f' % funcoes.variancia([funcoes.variancia(i) for i in data['temperatura']]),
            '%.3f' % funcoes.desvio_padrao([funcoes.desvio_padrao(i) for i in data['temperatura']]),
            '%.3f' % funcoes.coeficiente_variacao([funcoes.coeficiente_variacao(i) for i in data['temperatura']])
        ))
        f.write('\n\n')
        plt = plots.plot_save_regression([funcoes.media(i) for i in data['temperatura']], 1)
        f.write(analisadores.assimetria([funcoes.media(i) for i in data['temperatura']]) + '\n\n')
        f.write(analisadores.curtose([funcoes.media(i) for i in data['temperatura']]) + '\n\n')
        f.write("Função de regressão linear correspondente: $f(x) = %.5fx + %.5f$\n\n" % (plt['coef_a'], plt['coef_b']))
        f.write('![Histograma de Temperaturas]({})\n\n'.format(
            plots.plot_save_histogram([funcoes.media(i) for i in data['temperatura']])
        ))
        f.write('![Regressão Linear de Temperaturas]({})\n\n'.format(plt['nome']))

        f.write('\\newpage\n\n')

        f.write("## 2 - Ponto de Orvalho\n")
        f.write("Durante esta seção teremos como alvo de estudo a variavél de ponto de orvalho, que é a temperatura "
                + " (dada em graus Celsius) a qual o vapor de água presente no ar passa ao estado líquido em "
                + " um determinado aerodromo pelo periodo de 1 mês. Os dados são coletados hora a hora, assim temos a "
                + " seguinte tabela que apresenta a média, mediana, moda, variância, desvio padrão e o coeficiente de "
                + " variação de cada dia.\n\n\n")
        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        dia = 0
        for d in data['ponto_orvalho']:
            dia += 1
            f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
                str('%02d' % dia) + "/" + mes[4:6] + "/" + mes[:4],
                '%.3f' % funcoes.media(d),
                '%.3f' % funcoes.mediana(d),
                '%.3f' % funcoes.moda(d),
                '%.3f' % funcoes.variancia(d),
                '%.3f' % funcoes.desvio_padrao(d),
                '%.3f' % funcoes.coeficiente_variacao(d),
            ))
        f.write('\n\n')

        f.write("Em seguida são apresentadas a média, mediana, moda, variância, desvio padrão e coeficiente de "
                + "variação do mês todo.\n\n\n")

        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
            mes[4:6] + '/' + mes[:4],
            '%.3f' % funcoes.media([funcoes.media(i) for i in data['ponto_orvalho']]),
            '%.3f' % funcoes.mediana([funcoes.mediana(i) for i in data['ponto_orvalho']]),
            '%.3f' % funcoes.moda([funcoes.moda(i) for i in data['ponto_orvalho']]),
            '%.3f' % funcoes.variancia([funcoes.variancia(i) for i in data['ponto_orvalho']]),
            '%.3f' % funcoes.desvio_padrao([funcoes.desvio_padrao(i) for i in data['ponto_orvalho']]),
            '%.3f' % funcoes.coeficiente_variacao([funcoes.coeficiente_variacao(i) for i in data['ponto_orvalho']])
        ))
        f.write('\n\n')
        plt = plots.plot_save_regression([funcoes.media(i) for i in data['ponto_orvalho']], 2)
        f.write(analisadores.assimetria([funcoes.media(i) for i in data['ponto_orvalho']]) + '\n\n')
        f.write(analisadores.curtose([funcoes.media(i) for i in data['ponto_orvalho']]) + '\n\n')
        f.write("Função de regressão linear correspondente: $f(x) = %.5fx + %.5f$\n\n" % (plt['coef_a'], plt['coef_b']))
        f.write('![Histograma de Temperatura de Ponto de Orvalho]({})\n\n'.format(
            plots.plot_save_histogram([funcoes.media(i) for i in data['ponto_orvalho']])
        ))
        f.write('![Regressão Linear de Temperatura de Ponto de Orvalho]({})\n\n'.format(plt['nome']))

        f.write('\\newpage\n\n')

        f.write("## 3 - Pressão\n")
        f.write("Durante esta seção teremos como alvo de estudo a variavél de pressão atmosférica ao nível do mar"
                + " (dada em hectopascal) em um determinado aerodromo pelo periodo de 1 mês. Os dados são coletados "
                + "hora a hora, assim temos a seguinte tabela que apresenta a média, mediana, moda, variância, desvio "
                + " padrão e o coeficiente de variação de cada dia.\n\n\n")
        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        dia = 0
        for d in data['pressao']:
            dia += 1
            f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
                str('%02d' % dia) + "/" + mes[4:6] + "/" + mes[:4],
                '%.3f' % funcoes.media(d),
                '%.3f' % funcoes.mediana(d),
                '%.3f' % funcoes.moda(d),
                '%.3f' % funcoes.variancia(d),
                '%.3f' % funcoes.desvio_padrao(d),
                '%.3f' % funcoes.coeficiente_variacao(d),
            ))
        f.write('\n\n')

        f.write("Em seguida são apresentadas a média, mediana, moda, variância, desvio padrão e coeficiente de "
                + "variação do mês todo.\n\n\n")

        f.write("|  Data  |  Média  |  Mediana  |  Moda  |  Variância  |  Desvio Padrão  | Coef. Variação |\n")
        f.write("|--------|---------|-----------|--------|-------------|-----------------|----------------|\n")
        f.write("|{}|{}|{}|{}|{}|{}|{}|\n".format(
            mes[4:6] + '/' + mes[:4],
            '%.3f' % funcoes.media([funcoes.media(i) for i in data['pressao']]),
            '%.3f' % funcoes.mediana([funcoes.mediana(i) for i in data['pressao']]),
            '%.3f' % funcoes.moda([funcoes.moda(i) for i in data['pressao']]),
            '%.3f' % funcoes.variancia([funcoes.variancia(i) for i in data['pressao']]),
            '%.3f' % funcoes.desvio_padrao([funcoes.desvio_padrao(i) for i in data['pressao']]),
            '%.3f' % funcoes.coeficiente_variacao([funcoes.coeficiente_variacao(i) for i in data['pressao']])
        ))
        f.write('\n\n')
        plt = plots.plot_save_regression([funcoes.media(i) for i in data['pressao']], 3)
        f.write(analisadores.assimetria([funcoes.media(i) for i in data['pressao']]) + '\n\n')
        f.write(analisadores.curtose([funcoes.media(i) for i in data['pressao']]) + '\n\n')
        f.write("Função de regressão linear correspondente: $f(x) = %.5fx + %.5f$\n\n" % (plt['coef_a'], plt['coef_b']))
        f.write('![Histograma de Pressão Atmosférica]({})\n\n'.format(
            plots.plot_save_histogram([funcoes.media(i) for i in data['pressao']])
        ))
        f.write('![Regressão Linear de Pressão Atmosférica]({})\n\n'.format(plt['nome']))
