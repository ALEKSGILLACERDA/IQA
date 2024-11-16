
def partida(jogador_1, jogador_2):
  while True:
    jogador_1 = input(" Escolha pedra papel ou tesoura: ")
    jogador_2 = input("Escolha pedra papel ou tesoura: ")
   
    resultado = jogador_1 + jogador_2
    numero_jogadas = 0
   
    pedra = 'a'
    papel = 'b'
    tesoura = 'c'
    
    if jogador_1 not in (pedra, papel, tesoura) or jogador_2  not in (pedra, papel, tesoura):
         print("Opção inválida")
         continue
    
    if jogador_1 == jogador_2:
        print('empate')
        continue
    
    elif resultado == 'ab' or resultado == 'ba':
            print('tesoura ganha papel')
    elif resultado == 'ac' or resultado == 'ca':
        print('pedraganha tesoura')
    elif resultado == 'bc' or resultado == 'cb':
            print('papelganha pedra')

    numero_jogadas += 1
    print(f'Jogadas: {numero_jogadas}')
    if numero_jogadas > 5:
        return 'fim de jogo'
    





#def vitória(resultado)