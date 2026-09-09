rodadas = int(input(''))
recorde = int(input(''))
nrodadas = 0
tbolinhos = 0
extrapolar = 0
bolinhos2 = 0
parar = False
print('Tigresa: Duvido você bater o recorde, Po!\nPo: Prepare-se para ver o Dragão Guerreiro em ação!')
print()
for i in range(rodadas):
    if parar == False:
        nrodadas += 1
        bandejas = int(input(''))
        bolinhosrodada = 0
        for j in range(bandejas):
            if parar == False:
                bolinhos = int(input(''))
                tbolinhos += bolinhos
                bolinhosrodada += bolinhos
                if bolinhosrodada > recorde:
                    extrapolar += 1
                    bolinhos2 = bolinhosrodada
                    parar = True
        if extrapolar > 0 and bolinhos2 == bolinhosrodada:
                    print('Tigresa: Mas como?!\nPo: UHUL! CONHEÇA A FORÇA DO DRAGÂO GUERREIRO!!')
        elif bolinhosrodada >= 10:
            print('Po: Delícia! Mais uma rodada finalizada!')
        else:
            print('Po: Ainda tenho espaço para mais!')
        print(f'Rodada {nrodadas}: Po comeu {bolinhosrodada} bolinhos.')
        print()
if extrapolar > 0:
    print(f'Po: Ei! Eu ainda não terminei!\nTigresa: Acho que não vou mais subestimar sua fome.\nQue loucura! Po venceu a aposta comendo um total de {bolinhos2} bolinhos em uma só rodada!')
elif tbolinhos > recorde:
    print(f'Po: Eu sabia que conseguiria! O recorde e meu!\nTigresa: Inacreditável... Você realmente venceu a aposta.\nPo venceu a aposta! Ele comeu um total de {tbolinhos} bolinhos e superou o recorde de {recorde}!')
elif tbolinhos == recorde:
    print(f'Po: Empatamos! Cheguei exatamente no recorde!\nTigresa: Impressionante, mas empatar não basta para vencer a aposta. Venha lavar a louça!\nHouve um empate! Po comeu exatamente {tbolinhos} bolinhos e igualou o recorde de {recorde}.')
else:
    print(f'Tigresa: Eu avisei, Po! A louça do palácio te espera.\nPo: Ah não... Minhas mãos vão ficar enrugadas...\nTigresa venceu a aposta! Po comeu apenas {tbolinhos} bolinhos e não alcançou o recorde de {recorde}.')
