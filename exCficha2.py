paciencia = int(input(''))
qtd_visitantes = 0
continuar = True
print('Shrek achava que morar em um pântano afastado seria suficiente para manter as pessoas longe. Ele estava muito enganado.')
while  continuar == True:
    visitante = str(input(''))
    if visitante == 'ninguém':
        print('Ufa! Ninguém apareceu. Finalmente, um pouco de paz no pântano!')
        continuar = False
    else:
        gastopaciencia = int(input(''))
        if visitante == 'Burro':
            print('Burro?! Eu acabei de pedir um pouco de paz!')
            assunto = str(input(''))
            if assunto == 'sanduíche':
                print('Ah, isso sim é um bom assunto!')
                gastopaciencia = gastopaciencia / 2
        if paciencia == 0 or gastopaciencia > paciencia:
            print('A paciência do Shrek acabou! Dê meia-volta antes que ele perca o controle!')
            continuar = False
        else:
            if visitante == 'Burro':
                if assunto == 'Fiona':
                    print('É o Burro! E, como sempre, ele só sabe falar da Fiona.')
                if assunto == 'pântano':
                    print('Burro, isso é MEU pântano...')
            elif visitante == 'Gato de Botas':
                print('O Gato de Botas chegou! Shrek já está de olho nas suas botas.')
            elif visitante == 'Pinóquio':
                print('Pinóquio chegou! Shrek espera que ele não esteja mentindo.')
            elif visitante == 'Lobo Mau':
                print('Lobo Mau?! Shrek abriu a porta, mas já está se arrependendo!')
            else:
                print('Visitante desconhecido! Shrek não sabe quem você é, mas pode entrar por sua conta em risco.')
            paciencia -= gastopaciencia
            qtd_visitantes += 1

print(f'Ao todo, {qtd_visitantes} visitantes passaram pelo pântano. Shrek sobreviveu a mais um dia!')