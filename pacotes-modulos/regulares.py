import re

texto = 'Meu email é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com'

resultado = len(re.findall('@', texto))
print(f'O caractere @ apareceu {resultado}, vezes no texto')

#expressao regular para extrair a palavra que aparece após a palavra você
resultado2 = re.findall(r'você (\w+)', texto)
print(f'A palavra após você é: {resultado2[0]}')

# para procurar no chatgpt use REGEX
# ver o arquivo CAP06 - 10 LAB3 se ficar em duvida
