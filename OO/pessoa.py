class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    matheus = Pessoa(felipe, nome='Matheus')
    print(Pessoa.cumprimentar(matheus))
    print(id(matheus))
    print(matheus.cumprimentar())
    print(matheus.nome)
    print(matheus.idade)

    for filho in matheus.filhos:
        print(filho.nome)

    matheus.sobrenome = 'Morais'
    del matheus.filhos
    print(felipe.__dict__)
    print(matheus.__dict__)
