hpnoel = 100
danobreu = 15
totalpresentes = 0
totalcarvao = 0
custoglobal = 0.0
continuar = True
vivo = True
seqpresente = 0
seqcarvao = 0

while continuar == True:
    localidade = str(input(''))
    if localidade == 'FIM':
        continuar = False
    else:
        continente = str(input(''))
        pais = str(input(''))

        if continente == 'Europa':
            fatorcontinente = 1.0
        elif continente == 'Oceania':
            fatorcontinente = 2.0
        elif continente == 'América':
            fatorcontinente = 3.0
        elif continente == 'África':
            fatorcontinente = 4.0
        elif continente == 'Ásia':
            fatorcontinente = 5.0
        else:
            fatorcontinente = 1.0

        if pais == 'Brasil':
            modificadorpais = 1.10
        elif pais == 'EUA':
            modificadorpais = 1.15
        elif pais == 'China':
            modificadorpais = 1.20
        elif pais == 'Canadá':
            modificadorpais = 1.25
        elif pais == 'Rússia':
            modificadorpais = 1.30
        else:
            modificadorpais = 1.00

        custobase = 10.0
        custolocal = 0.0
        sobrecargaavisada = False
        continuarlocal = True

        while continuarlocal == True:
            nome = str(input(''))

            if nome == 'FIM_LOCAL':
                continuarlocal = False
                print(f'Localidade {localidade} finalizada. Custo logístico: {custolocal:.2f}')

            elif nome == 'Breu':
                print('Alerta! Breu atacou a entrega!')
                hpbreu = 50
                iniciativa = str(input(''))
                turno = iniciativa
                combatendo = True

                while combatendo == True:
                    acao = str(input(''))
                    if turno == 'Noel':
                        hpbreu -= 20
                        turno = 'Breu'
                    else:
                        hpnoel -= danobreu
                        turno = 'Noel'

                    if hpbreu <= 0:
                        combatendo = False
                        print('Noel repeliu a emboscada e as entregas continuam!')
                    elif hpnoel <= 0:
                        combatendo = False
                        vivo = False
                        continuarlocal = False
                        continuar = False

            else:
                notavalida = False
                while notavalida == False:
                    pontuacao = int(input(''))
                    if pontuacao < 0 or pontuacao > 100:
                        print('Pontuação inválida, insira novamente.')
                    else:
                        notavalida = True

                custo = custobase * fatorcontinente * modificadorpais
                custolocal += custo
                custoglobal += custo

                if pontuacao >= 70:
                    totalpresentes += 1
                    print(f'{nome} foi uma boa criança este ano e receberá um presente!')
                    seqpresente += 1
                    seqcarvao = 0
                    if seqpresente == 3:
                        hpnoel += 10
                        if hpnoel > 100:
                            hpnoel = 100
                        print('A fé das crianças fortalece a magia! Noel recuperou 10 de HP.')
                        seqpresente = 0
                else:
                    totalcarvao += 1
                    print(f'{nome} não se comportou bem e receberá carvão.')
                    seqcarvao += 1
                    seqpresente = 0
                    if seqcarvao == 3:
                        danobreu += 5
                        print(f'O medo e a descrença alimentam as sombras... O dano de Breu aumentou para {danobreu}!')
                        seqcarvao = 0

                if custolocal > 100.0 and sobrecargaavisada == False:
                    custobase = 15.0
                    sobrecargaavisada = True
                    print('O trenó está sobrecarregado pela magia! Custos base aumentados.')

if vivo == True:
    print(f'Noite concluída com sucesso! Presentes: {totalpresentes} | Carvão: {totalcarvao}')
    print(f'Custo logístico total: {custoglobal:.2f}')
    print(f'HP final do Noel: {hpnoel}')
else:
    print('O HP de Noel chegou a zero! O Breu venceu a batalha... O Natal das crianças foi arruinado.')