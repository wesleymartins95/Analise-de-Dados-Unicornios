# Analise-de-Dados-Unicornios
Analise de dados de Unicornios Mundiais entre 2018 a 2021

## Explicando as linhas de código do arquivo Analise.py 

*  Começando pela linha 5 onde importo os dados do site.  
*  Linha 6 e 7: Configuro a visualização no terminal do python.  
*  Em seguida altero os nomes das colunas de ingles para portugues.  
*  Com a função info() consigo ver a tipagem do arquivo.  
*  A função isnull().sum() faz a somatoria onde os dados estão nulos nas linhas/colunas.  
*  nunique é a função que seleciona apenas os dados unicos, sem redundancia.  
*  Pulando para linha 14 é usado o Normalize=True, estou pedindo que pegue os valores e transforme em porcentagem.  
*  Na 15 vou começar a criar a plotagem em barra, nos eixos estarão as industrias e valor de cada.  
*  Indo para linha 21, vou criar um grafico de 'pizza' , quero que mostre apenas as 5 primeiras informações usando os parametros:  (Labels: selecionando as info. do array de 0 a 5; StartAngle: onde o angulo do grafico começa;Autopct: o numero de casas decimais que quero mostrar;Labeldistance: (autoexplicativo),Radius: o tamanho do Raio do grafico).  
*  plt.legend(bbox_to_anchor=(1, 1)) , escolher a posição da legenda.  
*  Na linha 24 vou fazer a alteração do tipo do dado, a tipagem é object, mas preciso dele em Int senão as informações serão imprecisas e erradas.  
*  Alterado o tipo agora vou criar 2 colunas novas o mes e ano.  
*  Agora faço uso do GroupBy, assim consigo selecionar varias colunas para fazer Analise comparatoria,deixando organizado por ID.  
*  Por fim, é criado uma variavel e dentro dela é armazenado a agrupagem das colunas País e Valor onde Valor é organizado do maior valor para menor.  


## Conclusões dos Graficos

1.  Gráfico de Barra: Analisando as Industrias podemos observar que os setores que mais geraram Unicornios nos ultimos anos foram Startups,Internet/software e E-commerce.  
2.  Gráfico de 'pizza': São os TOP 5 Países que mais geram Unicornios no mundo, e os Estados Unidos lideram o ranking com uma discrepancia enorme da proxima posição que é a China (quase 3 vezes mais). O Brasil não está no grafico mas ele ocupa a nona posição.  
3.  Gráfico de Linha: Podemos ver os Países com maior valor em bilhões de Unicornios, e se compararmos com o grafico de 'pizza' podemos ver que a India tem uma colocação contrária, antes ela tinha mais Unicornios que o Reino Unido, mas se tratando de Valor em Bilhões o Reino Unido possue maior valor de mercado. E o mesmo acontece com o Brasil, quando analisamos seu valor ele está na 6° colocação.  
4.  Analise Descritiva: (Arquivo jpg e pdf) Nele está todas as empresas que se tornaram Unicornios entre 2018 a 2021, separando tambem pelo mês. Observando podemos ver que a Nubank foi a primeira que atingiu a casa do bilhão em Março/2018. 
