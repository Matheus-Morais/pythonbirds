class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 18

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':
    felipe = Homem(nome='Felipe')
    matheus = Homem(felipe, nome='Matheus')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(matheus.olhos)
    print(felipe.olhos)
    print(id(Pessoa.olhos), id(matheus.olhos), id(felipe.olhos))
    print(Pessoa.metodo_estatico(), matheus.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), matheus.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(felipe, Pessoa))
    print(isinstance((felipe, Homem)))
