nrodadas = int(input(''))
np = 100
recruta = ''
ajuda = ''
print('Os pinguins começaram sua fuga. Operação: sair de Mônaco vivos!')
while np > 0 and nrodadas > 0:
    acao = str(input(''))
    if acao == 'CHANTEL DUBOUIS':
        print('Parece que a Capitã Dubouis ganhou uma ajudinha extra na caçada... Como se ela precisasse.')
        ajuda = str(input(''))  
        if ajuda == 'helicóptero':
            np += 15
            print('Pendurada em um helicóptero, Dubouis se aproxima cada vez mais dos fugitivos!')
        elif ajuda == 'rastrear':
            np += 20
            print('Dubouis encontrou os rastros dos animais. Infelizmente, despistar essa mulher não estava no plano.')
        elif ajuda == 'SCOOTER':
            np += 35
            print('ELA PEGOU A LENDÁRIA SCOOTER! OS PINGUINS REALMENTE TÊM ALGUMA CHANCE?!')
        elif ajuda == 'Non, je ne regrette rien':
            np += 100
            print('INACREDITÁVEL! A VOZ ANGELICAL DE DUBOIS REANIMOU TODA A EQUIPE! ISSO É PERMITIDO?!')
        else:
            np += 5
            print('Um dos capangas encontrou uma pista dos animais. Pequena pista, enorme problema.')
    elif acao == 'kowalski':
        print('Kowalski teve uma ideia! Por algum milagre, ela realmente funcionou e atrasou a caçadora.')
        np -= 30
    elif acao == 'capitão':
        print('Após uma troca de golpes com Dubouis, o Capitão conseguiu atrasá-la. Liderança também envolve pancadaria.')
        np -= 40
    elif acao == 'RICO':
        np -= 50
        print('Rico sacou uma bomba de procedência extremamente duvidosa e acertou em cheio! Clássico Rico.')
    else:
        print('Parece que o Recruta vai tentar ajudar na fuga... Que os céus protejam essa operação.')
        recruta = str(input(''))
        if recruta == 'sucesso':
            np -= 15
            print('ELE CONSEGUIU! A fofura do Recruta distraiu os guardas de Dubouis. Uma arma verdadeiramente devastadora.')
        else:
            np += 10
            print('Ele tentou... mas deixou um rastro enorme para os guardas. Pelo menos a intenção foi boa.')
    nrodadas -= 1
if np > 0:
    print('Os pinguins não tiveram chance... A maior caçadora de animais de Mônaco é simplesmente IMPLACÁVEL!')
else:
    print('ELES CONSEGUIRAM! Deixaram a grandiosa CHANTEL DUBOUIS para trás e seguiram rumo a Madagascar!')