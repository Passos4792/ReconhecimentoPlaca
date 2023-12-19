DicionarioPlacas = {
    'ELD-2023': ['Gustavo', 'Fusca', 2025],
    'ABC-1234': ['Hariel', 'Ferrari-488-Pista', 2023],
    'UTS-0000': ['Marcelo', 'Ferrari-Italia', 2020],
    'BCD-3456': ['Thiago', 'Porsche 911', 2023],
    'OTM 2022': ['Felipe', 'Amarok', 2020]
}

#Exibir todas informacoes
print(DicionarioPlacas.items())
print ('-' * 100)

#Exibir todas informacoes organizadas
for n in DicionarioPlacas.items():
    print (n)
print ('-' * 100)

#Exibir todos os proprietarios
for n in DicionarioPlacas.values():
    print (n[0])
print ('-' * 100)

#Exibir o nome do carro do Marcelo
for n, indices in DicionarioPlacas.items():
    if 'Marcelo' in indices:
        print (indices[1])

#Exibir dono do carro fusca
print(DicionarioPlacas['ELD-2023'][0])


    