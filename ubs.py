import folium
from folium.plugins import MarkerCluster

unidades = {}

uf = {'AL': ('27', '-9', '-36'), 
      'BA': ('29', '-13', '-41'),
      'CE': ('23', '-5', '-39'),
      'DF': ('53', '-15', '-47'),
      'ES': ('32', '-19', '-40'), 
      'GO': ('52', '-15', '-50'),
      'MA': ('21', '-5', '-45'), 
      'MG': ('31', '-18', '-44'), 
      'MS': ('50', '-20', '-54'), 
      'MT': ('51', '-12', '-55'),
      'PA': ('15', '-3', '-52'),
      'PB': ('25', '-7', '-36'),  
      'PE': ('26', '-8', '-37'),  
      'PI': ('22', '-7', '-43'), 
      'PR': ('41', '-24', '-51'), 
      'RJ': ('33', '-22', '-43'),    
      'RN': ('24', '-6', '-36'), 
      'RO': ('11', '-10', '-62'),  
      'RR': ('14', '2', '-61'), 
      'RS': ('43', '-30', '-55'), 
      'SC': ('42', '-27', '-51'), 
      'SE': ('28', '-10', '-37'),
      'SP': ('35', '-22', '-48'), 
      'TO': ('17' ,'-10', '-48') } 

uf_valor = ""

while True:
    ufinput = input("Digite a UF: ").upper()
    if ufinput in uf.keys():
        uf_valor = uf[ufinput]
        with open("UBS.csv") as csv:
            for linha in csv:
                aux = linha[:-1].split(";")
                lat = aux[6]
                lon = aux[7]
                uf = aux[1]
                if lat != "" and lon != "" and uf == uf_valor[0]:
                    nome = aux[3][1:-1]
                    logr = aux[4][1:-1]
                    bairro = aux[5][1:-1]
                    lat = lat.replace(',','.')
                    lon = lon.replace(',','.')
                    lat = float(lat)
                    lon = float(lon)
                    unidades[nome] = (logr, bairro, lat, lon)
        break
    else:
        print("UF não encontrada")

latt = uf_valor[1]
lonn = uf_valor[2]

mapa = folium.Map(location=[latt, lonn], zoom_start=8)
mapa_ubs = folium.Map(location=[latt, lonn], zoom_start=8)
marker_cluster = MarkerCluster().add_to(mapa)
marker_cluster_ubs = MarkerCluster().add_to(mapa_ubs)


for nome, (logr, bairro, lat, lon) in unidades.items():
    folium.Marker(location=[lat, lon], popup=nome).add_to(marker_cluster) 

mapa.save('mapa_de_todas_as_ubs_da_uf.html')

ubs = input("Digite o nome da UBS: ").upper()
resultados = []

for nome in unidades.keys():
    if ubs in nome:
        resultados.append(unidades[nome])

        tuplaDasUbs = unidades[nome]
        latitudeDaUbs = tuplaDasUbs[2]
        longitudeDaUbs = tuplaDasUbs[3]

        folium.Marker(location=[latitudeDaUbs, longitudeDaUbs], popup=nome).add_to(marker_cluster_ubs) 
        
        print("UBS encontrada: ", nome, unidades[nome])
        
if len(resultados) == 0:
    print("UBS não encontrada")
else:
    mapa_ubs.save('mapa_das_ubs_pesquisadas.html')


        


