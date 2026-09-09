n = int(input(''))
nomevaga = ''
repetidas = 0
unica = 0
for c in range(1, n+1):
    vaga = str(input(''))
    saidavaga = nomevaga
    if vaga  in saidavaga:
        repetidas += 1
    else:
        if nomevaga == '':
            nomevaga = vaga
        else:
            nomevaga += ' - ' + vaga
        unica += 1

print('Parabéns formandos! E agora iniciaremos sua carreira nas indústrias Honex.')
print(nomevaga)
print(f'Quantidade de cargos repetidos: {repetidas}')
if unica > repetidas:
    print('Pelo menos Barry tem opções!')
else:
    print('Mais do mesmo. Barry será apenas uma engrenagem na máquina de mel.')