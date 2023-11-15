import sys
import pandas as pd
import numpy as np

#class analise:
 #   def leDados():
dados = input("Forneça o endereço do arquivo de dados a ser analisado, inclusive a terminação de seu formato (somente .txt): ")
dadosTxt = pd.read_table(dados)
#resumo dos dados    
resumo = dadosTxt.info()
#Tabela o "elemento a ser" será uma variável fornecida pelo usuario
frequencia = dadosTxt['elemento a ser analisado'].value_counts().sort_index()
proporcao = round(dadosTxt['elemento a ser analisado'].value_counts(normalize= True), 2).sort_index()
percentagem = round(dadosTxt['elemento a ser analisado'].value_counts(normalize= True)*100, 2).sort_index()
tabela_freq = pd.DataFrame({'Frequência': frequencia, 'Proporção': proporcao, 'Percentual(%)': percentagem})
total = pd.DataFrame(tabela_freq.sum(), columns= ['Total'])
result = pd.concat([tabela_freq, total.transpose()])

print(result)