class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade

    def __lt__(self, other):
        return self.prioridade < other.prioridade