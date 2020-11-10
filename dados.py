from random import randrange
bolso = 100
resultado = 0
resposta = "s"
while(resposta=="s"):
  numero_apostado = int(input("Escolha um número entre 1 e 6 para você apostar: "))
  valor_aposta = float(input("Qual o valor da aposta? "))
  bolso -= valor_aposta
  dado1 = randrange(1,6)
  dado2 = randrange(1,6)
  print("Sorteados os dados {} e {}.".format(dado1, dado2))
  if(dado1==numero_apostado)and(dado2==numero_apostado):
    resultado = valor_aposta * 10
    bolso += resultado
    print("Você ganhou {} e agora está com {}.".format(resultado,bolso))
  elif (dado1==numero_apostado)or(dado2==numero_apostado):
    resultado = valor_aposta * 2
    bolso += resultado
    print("Você ganhou {} e agora está com {}.".format(resultado,bolso))
  else:
    print("Você errou. Agora tem {} no bolso.".format(bolso))
  resposta = input("Deseja jogar outra vez? ".lower())
print("Fim de jogo.")
