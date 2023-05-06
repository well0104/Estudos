funcionario = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

#funcionarios que tem carros e trabalham de noite
set1 = set(turno_noite)
set2 = set(tem_carro)

nome_em_comum1 = set1 & set2

print('funcionarios que tem carros e trabalham de noite', nome_em_comum1)

#funcionarios que tem carros e trabalham de dia
set3 = set(turno_dia)
set2 = set(tem_carro)

nome_em_comum2 = set3 & set2

print('funcionarios que tem carros e trabalham de dia ',nome_em_comum2)

#funcionarios que não tem carro

set5 = set(funcionario)
nome_em_comum3 = set5 - set2
print('funcionarios que não tem carro' ,nome_em_comum3)
