import testePandas as tp

class main:
    print('Inicio do prograda de analise de dados.')
    print('Use base de dados em formato txt!')

    while true:
        tp.leDados()
        print('1 - Resumo; \n 2 - Tabela; \n 3 - Grafico de Barras \n 4 - Medidas Descritivas \n 5 - Medidas de dispersão \n 6 - Medidas Relativas')
        opcao = input('Digite o valor da opcao do que deseja fazer: ')
        match opcao:    
            case 1:
                tp.resumoDados()
            case 2:
                tp.tabela()
            case 3:
                tp.grafBarra()
            case 4:
                tp.medidaDesc()
            case 5:
                tp.medidaDisp()
            case 6:
                tp.medidaRelativa()
            case 0:
                break