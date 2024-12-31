from time import sleep


def movimentar_arquivos():
    import os
    os.makedirs(os.path.join('arquivos', '22'), exist_ok=True)
    os.makedirs(os.path.join('arquivos', '23'), exist_ok=True)
    try:
        arquivos = os.listdir('arquivos')

        for lista in arquivos:
            # Obter caminho completo de lista
            caminho_completo = os.path.join('arquivos', lista)
            # Verifica se é um arquivo
            if os.path.isfile(caminho_completo):
                #separa nome do arquivo e extensao
                nome, extensao = os.path.splitext(lista)
                print('-' * 60)
                print(f'Processando arquivo: {lista} | Nome: {nome} | Extensão: {extensao}')
                sleep(1)
                #Verificar a extensão do arquivo
                if extensao == '.txt':
                    if '22' in nome:#arquivo com 22 no nome
                        dst = os.path.join('arquivos', '22', lista)
                        print(f'Movendo arquivo: {lista} para {dst}')
                        print('-' * 60)
                        os.rename(caminho_completo, dst)
                        sleep(1)
                    elif '23' in nome:# arquivo com 23 no nome
                        dst = os.path.join('arquivos', '23', lista)
                        print(f'Movendo arquivo: {lista} para {dst}')
                        print('-' * 60)
                        os.rename(caminho_completo, dst)
            else:
                print(f'{lista} Não é um arquivo. Ignorando...')
    except Exception as e:
        print(f'Erro ao tentar movimentar arquivos.: {e.__class__}')

movimentar_arquivos()

