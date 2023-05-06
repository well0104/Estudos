from datetime import datetime
class Funcionario:
    def __init__(self,nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    def nome_completo(self):
        return self.nome + " " + self.sobrenome
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionario('wellinton', 'freitas', 2001)
usuario2 = Funcionario('aghata', 'correia', 2000)
usuario3 = Funcionario('daniele', 'daiana', 1999)


#usuario1.nome = 'wellinton'
#usuario1.sobrenome = 'freitas'
#usuario1.data_nacimento = '01/02/2001'

#usuario2.nome = 'aghata'
#usuario2.sobrenome = 'correia'
#usuario2.data_nacimento = '01/04/2000'

print(usuario3.nome_completo())
print(Funcionario.nome_completo(usuario1))
print(Funcionario.idade_funcionario(usuario3))


