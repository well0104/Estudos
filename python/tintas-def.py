redimento = int(input('qual é o rentimento por 1 lata ?'))
largura_parede = int(input('qual é a largura da parede ?'))
altura_parede = int(input('qual é a altura da parede ?'))


def calulo_titas():
    area = largura_parede * altura_parede
    total = area / redimento
    print('Voce precisa de', total, 'de latas de tintas para pintar essa parede')