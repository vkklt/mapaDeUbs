# Mapa De UBS

Buscador de todas as UBS do país. Busca e retorna o nome e o endereço pesquisados, além de gerar um mapa interativo com todas as UBS do estado, e um mapa interativo com a localização da(s) UBS(s) pesquisada(s).

![Captura de tela 2023-04-02 213707](https://user-images.githubusercontent.com/109630661/229388333-07eb3d66-4b44-49a5-b1d1-68d88fac496c.png)

Primeiro, ao digitar a UF ele filtra no .csv todas as UBS da UF pesquisada tratando todos os dados e comparando ao código de cada estado colocado originalmente no arquivo .csv. Junto do código do estado coloquei um indicador de latitude e longitude para a biblioteca "folium" gerar um mapa focado na UF escolhida. 

![Captura de tela 2023-04-02 213720](https://user-images.githubusercontent.com/109630661/229388360-d374df86-b094-4416-ab5e-b7483e35f922.png)

Após isso o folium gera o mapa do estado com todas as UBS em um arquivo .html interativo, e abre a pesquisa por uma UBS específica.

![Captura de tela 2023-04-02 213728](https://user-images.githubusercontent.com/109630661/229388388-56c487a5-d23b-421a-aa53-2038fe7dada6.png)

Ao digitar o nome (ou uma parte do nome) ele retorna a busca com todos os resultados que encontrou, com os endereços, nomes e também um segundo mapa, esse somente com as UBS pesquisadas, também feito pelo folium e interativo em um segundo arquivo .html.

![Captura de tela 2023-04-02 213744](https://user-images.githubusercontent.com/109630661/229388405-b1935315-406b-4c83-a042-5646eef03dc0.png)
![Captura de tela 2023-04-02 213753](https://user-images.githubusercontent.com/109630661/229388407-0d872a1b-9dad-478a-b96a-4018267a4ff0.png)

Obs: ele busca por nome, não por bairro, no caso eu pesquisei qual tinha "Copacabana" no nome, existem outras UBS em Copacabana, porém não possuem a palavra "Copacabana" no nome, para saber quais ficam em Copacabana, use o primeiro mapa gerado pelo folium, que exibe todas as UBS da UF escolhida

Coloquei 2 arquivos de .html de teste, usando dados do RJ. Porém ele funciona para todas as UF do país.
