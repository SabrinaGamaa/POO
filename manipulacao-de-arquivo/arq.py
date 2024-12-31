def movimentar_arquivos():
    import os
    arquivos = os.listdir('arquivos')
    try:
        for lista in arquivos:
            if 'txt' in lista:
                if '22' in lista:
                    os.rename(f'arquivos/{lista}', f'arquivos/22/{lista}')
                elif '23'in lista:
                    os.rename(f'arquivos/{lista}', f'arquivos/23/{lista}')
    except:
        print('Erro ao tentar movimentar arquivos.')
    else:
        print('Arquivos Organizados com sucesso!')

movimentar_arquivos()

