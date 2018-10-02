import urllib.request
import sys
import report

months = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def parse_metar(metar):
    if 'Mensagem METAR' in metar:
        metar = metar.split(' ')
        return {
            "data": metar[0],
            "aerodromo": '',
            "temperatura": '0/0',
            "pressao": 'Q0000'
        }
    else: 
        metar = metar.split(' ')
        return {
            "data": metar[0],
            "aerodromo": metar[3],
            "temperatura": metar[-2],
            "pressao": metar[-1].replace('=', '').replace('\n', '')
        }


def get_metar(aerodromo, dt_inicial, dt_final):
    req = urllib.request.Request("http://www.redemet.aer.mil.br/api/consulta_automatica/index.php?local={}&msg=metar&data_ini={}&data_fim={}".format(aerodromo, dt_inicial, dt_final))
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')
    data = []
    with urllib.request.urlopen(req) as f:
        for l in f.readlines():
            data.append(parse_metar(l.decode('utf-8')))
    return data


def get_data():
    y, m = sys.argv[2][:4], sys.argv[2][4:6]
    results = []
    for i in range(0, months[int(m)]):
        date = y + m + str('%02d' % (i + 1))
        results.append(get_metar(
            sys.argv[1],
            date + '00',
            date + '23'
        ))
    stats = {
        "temperatura": [],
        "ponto_orvalho": [],
        "pressao": []
    }
    for d in results:
        tmp = []
        po = []
        pressao = []
        for h in d:
            tmp.append(int(h['temperatura'].split('/')[0]))
            po.append(int(h['temperatura'].split('/')[1]))
            pressao.append(int(h['pressao'].replace('Q', '')))
        stats['temperatura'].append(tmp)
        stats['ponto_orvalho'].append(po)
        stats['pressao'].append(pressao)
    return stats


if __name__ == "__main__":
    if len(sys.argv) == 3:
        data = get_data()
        report.gerar(sys.argv[1], sys.argv[2], data)


