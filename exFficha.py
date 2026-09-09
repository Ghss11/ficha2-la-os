anorigem = int(input(''))
anoproibido = int(input(''))
nivelenergia = int(input(''))

anoatual = anorigem
rasgotemporal = 0
pecas = 0
primeirosalto = False
continuar = True
motivo = ''

print('''=== WABAC: SISTEMA DE EMERGÊNCIA ===
Alvo: Ano 2026 | Peças Necessárias: 3
Sherman, mantenha as mãos longe dos botões! Iniciando saltos...''')

while continuar == True:
    acao = str(input(''))

    if acao == 'SALTAR':
        anosalto = int(input(''))
        custoenergia = int(input(''))
        anoatual += anosalto
        nivelenergia -= custoenergia
        rasgotemporal += 10
        primeirosalto = True
    elif acao == 'CONSERTAR':
        dificuldade = int(input(''))
        esforco = int(input(''))
        if esforco >= dificuldade:
            pecas += 1
            nivelenergia -= 10
        else:
            nivelenergia -= 15
            rasgotemporal += 20
    elif acao == 'AULA DE HISTÓRIA':
        nivelenergia += 25
        rasgotemporal += 15

    if nivelenergia < 0:
        nivelenergia = 0
    if rasgotemporal > 100:
        rasgotemporal = 100

    if anoatual == anoproibido or (primeirosalto == True and anoatual == anorigem):
        continuar = False
        motivo = 'paradoxo'
    elif nivelenergia <= 0:
        continuar = False
        motivo = 'apagao'
    elif rasgotemporal >= 100:
        continuar = False
        motivo = 'colapso'
    elif acao == 'ABORTAR':
        continuar = False
        motivo = 'abortar'
    elif pecas >= 3 and anoatual >= 2026:
        continuar = False
        motivo = 'sucesso'
    else:
        if acao == 'SALTAR':
            print(f'WABAC saltou para o ano {anoatual}!')
            print(f'Energia restante: {nivelenergia} | Rasgo Temporal: {rasgotemporal}%')
        elif acao == 'CONSERTAR':
            if esforco >= dificuldade:
                print('Sherman: "Consegui, Mr. Peabody! Encontrei uma peça de calibragem!"')
                print(f'Peças coletadas: {pecas}/3 | Energia: {nivelenergia}')
            else:
                print('Mr. Peabody: "Tenha mais cuidado, Sherman! Essa falha desestabilizou o tempo!"')
                print(f'Energia: {nivelenergia} | Rasgo Temporal: {rasgotemporal}%')
        elif acao == 'AULA DE HISTÓRIA':
            print('Mr. Peabody: "Como disse Galileu Galilei, a matemática é a linguagem com a qual Deus escreveu o universo."')
            print(f'Energia recarregada para {nivelenergia}!')

if motivo == 'paradoxo':
    print(f'ALERTA CRÍTICO: Peabody encontrou sua própria versão no ano {anoatual}!')
    print('O continuum espaço-tempo ruiu em uma espiral paradoxal.')
elif motivo == 'apagao':
    print('A WABAC desligou completamente por falta de energia.')
    print('Peabody e Sherman estão vagando sem rumo pela linha do tempo...')
elif motivo == 'colapso':
    print('O rasgo temporal atingiu massa crítica!')
    print('O universo foi engolido por um buraco negro sobre a cidade de Nova York.')
elif motivo == 'abortar':
    print('Mr. Peabody acionou o protocolo de parada manual.')
    print('A viagem foi cancelada antes de sua conclusão.')
elif motivo == 'sucesso':
    print(f'A WABAC emergiu com sucesso no ano de {anoatual}! Com as 3 peças coletadas, Mr. Peabody selou o rasgo temporal e salvou o presente!')