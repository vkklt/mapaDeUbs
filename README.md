# Mapa De UBS

Buscador de todas as UBS do país. Busca e retorna o nome e o endereço pesquisados, além de gerar um mapa interativo com todas as UBS do estado, e um mapa interativo com a localização da UBS pesquisada.

Primeiro, ao digitar a UF ele filtra no .csv todas as UBS da UF pesquisada tratando todos os dados e comparando ao código de cada estado colocado originalmente no arquivo .csv. Junto do código do estado coloquei um indicador de latitude e longitude para a biblioteca "folium" gerar um mapa focado na UF escolhida. Após isso o folium gera o mapa do estado com todas as UBS em um arquivo .html interativo, e abre a pesquisa por uma UBS específica, ao digitar o nome (ou uma parte do nome) ele retorna a busca com todos os resultados que encontrou, com os endereços, nomes e também um segundo mapa, esse somente com as UBS pesquisadas, também feito pelo folium e interativo em um segundo arquivo .html

Coloquei 2 arquivos de .html de teste, usando dados do RJ. Porém ele funciona para todas as UF do país.
