# coding: utf-8

from amara.bindery import html
from amara.lib import U


doc = html.parse('http://educacaoaberta.org/wiki/index.php?title=Tabla_Din%C3%A1mica_Software_Educativo_Libre')
datos  = doc.xml_select(u'//table[@id="tab"]/tbody/tr[td]')

# datos = tabla.tbody.tr

def area(f):
    return U(f.td[0]).strip()

def nivel(f):
    niveles = {1: 'EPE', 2:  'EP1', 3: 'EP2' , 4: 'EM', 5: 'ES'}

    return [niveles[x] for x in range(1,6) if u'Sí' in U(f.td[x])]

def link(f):
    try:
        return f.td[6].a.href
    except:
        return None

def label(f):
    return U(f.td[6])

resultado = []

def extraer(datos):
    for fila in datos:

            keys = 'area nivel link label'.split()
            res = zip(keys, [area(fila), nivel(fila), link(fila), label(fila)])
            resultado.append(res)

extraer(datos)
