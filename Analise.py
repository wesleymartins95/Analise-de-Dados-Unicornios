import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Base_dados = pd.read_csv('Startups in 2021 end.csv')
pd.set_option('display.max_columns',8)
pd.set_option('display.width',2000)
Base_dados.rename(columns={'Unnamed: 0':'Id','Company':'Empresa', 'Valuation ($B)':'Valor($)','Date Joined' : 'Data de Adesão','Country':'País','City':'Cidade','Industry':'Industria','Select Investors':'Investidores'},inplace=True)
Base_dados.info()
(Base_dados.isnull().sum())
(Base_dados.nunique())
(Base_dados['Industria'].unique())
(Base_dados['Industria'].value_counts())
(Base_dados['Industria'].value_counts(normalize=True))
plt.bar(Base_dados['Industria'].value_counts().index,Base_dados['Industria'].value_counts())
plt.title('Analise de Industrias que mais geram Unicornios')
print(plt.xticks(rotation=45,ha='right'));
print(plt.show())
plt.title('Países com maior numero de Unicornios (%)')
porc_Unicornio_País=(round(Base_dados['País'].value_counts(normalize=True)*100,2))
plt.pie(porc_Unicornio_País.head(5),labels=porc_Unicornio_País.index[0:5],startangle=90,autopct='%1.1f%%',labeldistance=1.2,pctdistance=0.8,radius=1.5)
plt.legend(bbox_to_anchor=(1, 1))
print(plt.show())
Base_dados['Data de Adesão']= pd.to_datetime( Base_dados['Data de Adesão'])
Base_dados['Mes'] = pd.DatetimeIndex(Base_dados['Data de Adesão']).month
Base_dados['Ano'] = pd.DatetimeIndex(Base_dados['Data de Adesão']).year

Analise_Agrupada=Base_dados.groupby(by=['País','Ano','Mes','Empresa']).count()['Id'].reset_index()

print(Analise_Agrupada.loc[Analise_Agrupada['País']=='Brazil'])

Base_dados['Valor($)'] = pd.to_numeric(Base_dados['Valor($)'].apply(lambda linha: linha.replace('$','')))

Analise_valor=Base_dados.groupby(by= ['País']).sum()['Valor($)'].reset_index().sort_values('Valor($)',ascending=False)
plt.title('Países com maior valor em Bilhões de Unicornios')
plt.plot(Analise_valor['País'],Analise_valor['Valor($)'])

plt.xticks(rotation=45,ha='right');
print(plt.show())