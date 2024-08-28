from random import randint

print('\nADIVINHE O NÚMERO')
random = randint(0, 100)
chute = 0
chances = 10
for _ in range(chances):
    chute = input('\n\nChute um número entre 0 a 100: ')
    if chute.isnumeric():
        chute = int(chute)
        if chute >= 0 and chute <= 100:        
            if chute == random:
                print('\nParabéns, você acertou o número! Você ainda tinha {} chances.'.format(chances-1))
                break
            else: 
                chances -= 1
                if chances == 0:
                    print('\nSuas chances acabaram, você perdeu! O número era {}.'.format(random))
                    break
                else:
                    if chute > random:print('\nVocê errou! Dica: É um número menor.')
                    else:
                        print('\nVocê errou! Dica: É um número maior.')
                    print('\nVocê ainda possui {} chances.'.format(chances))
        else:
            print('\nFoi digitado um número menor que 0 ou maior que 100') #Informa quando o número digitado não está entre 0 a 100
            chances -= 1  
    else: 
        print('\nPor favor, digite um número válido!') #Informa quando o caractere digitado não é válido
        chances -= 1

print('\n\n#FIM DE JOGO#\n')