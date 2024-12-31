# vamos criar uma classe para Clientes da Netflix
class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        try:
            if plano in self.lista_planos:
                self.plano = plano
            else:
                raise Exception('Plano invalido.')
        except:
            print('ERRO! Por favor tente novamente mais tarde!')


    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido. Por favor escolha plano \'Basic\' ou \'Premium\'. ')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Infelizmente seu plano não cobre esse filme')
        else:
            print('Plano invalido para esse filme')


cliente = Cliente(str(input("Nome: ")), 'sabrinagama@gmail.com', 'basic')
cliente.ver_filme('Harry Potter', 'premium')


cliente.mudar_plano('premium')
print(cliente.ver_filme('Harry Potter', 'premium'))

