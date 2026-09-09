qataques = int(input(''))
print('Quando percebi que contara oito mortes, senti o peso da minha própria lenda')

if qataques == 0:
    print('Até logo, velho amigo... É bom saber que finalmente posso respirar fundo e apenas viver o dia de hoje.')

else:
    desfecho = False
    continuar = True

    while qataques > 0 and continuar == True:
        qataques -= 1
        print('Preciso encontrar esse mapa a qualquer custo, nem que seja a última coisa que eu faça com esta vida!')
        companheiro = str(input(''))
        if companheiro == 'cao perrito':
            print('Olha só... de todas as criaturas do mundo, justo você tinha que decidir me seguir com esse rabo abanando?')
            N = int(input(''))
            tddivisiveis = True
            for i in range(N):
                numero = int(input(''))
                if numero % 3 != 0:
                    tddivisiveis = False
            if tddivisiveis == True:
                print('Bom trabalho, meu garoto! Quem diria que um cãozinho tão pequeno seria o grande herói do dia?')
                desfecho = True
                continuar = False
        elif companheiro == 'kitty patamansa':
            print('Kitty... Olhar para você de novo só me faz lembrar que, entre todas as minhas nove vidas, o meu maior erro foi ter deixado você esperando.')
            item = str(input(''))
            if item == 'chapeu do gato' or item == 'bota do gato':
                print('Impressionante, Kitty... Sempre soube que você era rápida, mas admito que nada fica melhor nas mãos da melhor ladra de Tão Tão Distante do que um presente para mim.')
                desfecho = True
                continuar = False
        else:
            lerfrases = True
            while lerfrases == True:
                frases = str(input(''))
                if 'Desfecho' in frases:
                    continuar = False
                    desfecho = True
                    lerfrases = False
                elif 'Morte' in frases:
                    lerfrases = False

    if desfecho == True:
        print('Parece que essa família de ursos e sua cachinhos acabam de provar do verdadeiro felino de botas!')
        frasefinal = str(input(''))
        if 'coragem' in frasefinal.lower():
            print('A verdadeira vitória não está em vencer a morte, mas em encará-la de frente e escolher lutar por cada segundo desta vida!')
        else:
            print('Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.')
    else:
        print('Pode levar minha espada e meu chapéu... Eu lutei até o fim, mas hoje a lenda finalmente descansa.')