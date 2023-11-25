import sys
import pandas as pd
import numpy as np

class testePandas:
    def leDados():
        dados = input("Forneça o endereço do arquivo de dados a ser analisado, inclusive a terminação de seu formato (somente .txt): ")
        dadosTxt = pd.read_table(dados)
    
    def resumoDados():
        resumo = dadosTxt.info()
        print(resumo)

    def tabela():
        elemento = input("Digite o nome do parametro a ser analizado: ")

        frequencia = dadosTxt[elemento].value_counts().sort_index()
        proporcao = round(dadosTxt[elemento].value_counts(normalize= True), 2).sort_index()
        percentagem = round(dadosTxt[elemento].value_counts(normalize= True)*100, 2).sort_index()
        
        tabela_freq = pd.DataFrame({'Frequência': frequencia, 'Proporção': proporcao, 'Percentual(%)': percentagem})
        total = pd.DataFrame(tabela_freq.sum(), columns= ['Total'])
        
        result = pd.concat([tabela_freq, total.transpose()])
        print(result)
    
    def grafBarra():
        elemento = input("Digite o nome do parametro a ser analizado: ")

        fig = dadosTxt[elemento].value_counts().plot(kind='barh', title='Grafico da variável ' + elemento)
        print(fig)

    def medidaDesc():
        elemento = input("Digite o nome do parametro a ser analizado: ")
        
        media = dadosTxt[elemento].mean()
        mediana = dadosTxt[elemento].median()
        moda = dadosTxt[elemento].mode()

        print('A media, mediana e moda de ' + elemento + 'são respectivamente: ' + media + '; ' + mediana + '; ' + moda)
    
    def medidasDisp():
        elemento = input("Digite o nome do parametro a ser analizado: ")

        amplitude = dadosTxt[elemento].max() - dadosTxt[elemento].min()
        variancia = dadosTxt[elemento].var()
        desvioPadrao = dadosTxt[elemento].std()

        print('A amplitude, variancia e desvio padrão de ' + elemento + ' são respectivamente: ' + amplitude + '; ' + variancia + '; ' + desvioPadrao)

    def medidaRelativa():
        elemento = input("Digite o nome do parametro a ser analizado: ")

        variacao = round(dadosTxt[elemento].std() / dadosTxt[elemento].mean() * 100, 2)
        
        print('A variação do elemento ' + elemento + 'é de ' + variacao + '%')

