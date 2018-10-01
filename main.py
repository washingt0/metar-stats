import urllib.request
import sys
import funcoes

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
    req = urllib.request.Request("http://www.redemet.aer.mil.br/api/consulta_automatica/index.php?local={}&msg=metar&data_ini={}&data_fim={}".format(
        aerodromo,
        dt_inicial,
        dt_final
    ))
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')

    data = []

    with urllib.request.urlopen(req) as f:
        for l in f.readlines():
            if 'Mensagem METAR' in l.decode('utf-8'):
                pass
            else:
                data.append(parse_metar(l.decode('utf-8')))

    return data

if __name__ == "__main__":
    if len(sys.argv) == 3:
        y, m = sys.argv[2][:4], sys.argv[2][4:6]

        results = []

        for i in range(0, months[int(m)]):
            date = y+m+str('%02d' % (i+1))
            results.append(get_metar(
                sys.argv[1],
                date + '00',
                date + '23'
            ))
        media = []
        mediana = []
        moda = []
        for d in results:
            tmp = []
            for h in d:
                tmp.append(int(h['temperatura'].split('/')[0]))
            media.append(funcoes.media(tmp))
            mediana.append(funcoes.mediana(tmp))
            moda.append(funcoes.moda(tmp))

        print(media)
        print(mediana)
        print(moda)

        print(funcoes.media(media))
        print(funcoes.mediana(mediana))
        print(funcoes.moda(moda))


