ponto = input('Qual é o ponto da sua carne ? ')

if int(ponto) < 48:
    print('È melhor casar e comer na mata mesmo')

elif int(ponto) in range(48,53):
    print('esta mal passada em')

elif int(ponto) in range(54,60):
    print('está ponto para mal passada, para ficar melhor so mais 1 min e fica perfeita!')   

elif int(ponto) in range(60,64):
    print('Isso ai tu entende de carne, esta carne esta no ponto!')

elif int(ponto) in range(65,69):
    print('cuidado esta carne esta ponto para bem!')

elif int(ponto) in range(70,72):
    print('quer comer carvao ? esta bem passada!')

else:
    print('AAAAAAAA estragou a nossa picanha, ja vende para adega que la eles usam esse carvao')
