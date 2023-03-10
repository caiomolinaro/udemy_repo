nome = 'Caio'
# print(nome[1])
# print(nome[-2])

# print('a' in nome)
# print('b' in nome)
# print(10 * '-')
# print ('a' not in nome)
# print('b' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
