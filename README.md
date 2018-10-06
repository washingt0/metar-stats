## METAR stats

Aplicação que busca gera um relatório mensal de temperatura, ponto de orvalho e pressão de um aerodromo a partir dos dados disponibilizados pela [Rede de Meteorologia do Comando da Aeronáutica](https://www.redemet.aer.mil.br/). 


### Requisitos
- Python 3.5+
- Pandoc
- matplotlib

### Como utilizar
Após a instalação de todos os requisitos, utilize o comando:
```bash
$ python main.py <ICAO> <YYYYMM>
```

Onde `<ICAO>` deve ser substituido pelo código ICAO do aeródromo que se deseja os dados, por exemplo, `SBJU` é o código ICAO do aeródromo de Juazeiro do Norte/CE e `<YYYYMM>` deve ser substituido pelo periodo desajado, por exemplo, `201809` que representa o periodo de 01 a 30 de setembro de 2018.

Exemplo para consultar o aerodromo de Guarulhos em entre 01 e 31 de agosto de 2018:
```bash
$ python main.py SBGR 201808
```
