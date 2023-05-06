import math


redimento = int(input('qual é o rentimento por 1 lata ?'))
largura_parede = int(input('qual é a largura da parede ?'))
altura_parede = int(input('qual é a altura da parede ?'))

area = largura_parede * altura_parede

quantidade_latas = math.ceil(area / redimento)

print('Voce precisa de ', quantidade_latas, "para pintar essa parede")




 