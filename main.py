import heapq
import os
import random
import unittest

class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade

    def __lt__(self, other):
        return self.prioridade < other.prioridade

class ProntoSocorro:
    def __init__(self):
        self.fila_prioridades = []
        self.ultimos_pacientes_chamados = []

    def adicionar_paciente(self, paciente):
        heapq.heappush(self.fila_prioridades, paciente)

    def atender_proximo_paciente(self):
        if self.fila_prioridades:
            paciente = heapq.heappop(self.fila_prioridades)
            self.ultimos_pacientes_chamados.append(paciente)
            return paciente
        else:
            return None

    def visualizar_fila(self):
        return [(paciente.nome, paciente.idade, paciente.prioridade) for paciente in self.fila_prioridades]

    def mostrar_proximo_paciente(self):
        if self.fila_prioridades:
            paciente = self.fila_prioridades[0]
            return paciente.nome, paciente.idade, paciente.prioridade
        else:
            return "Não há pacientes na fila"

    def listar_ultimos_pacientes_chamados(self):
        if not self.ultimos_pacientes_chamados:
            return "Não há pacientes chamados"
        else:
            return [(paciente.nome, paciente.idade, paciente.prioridade) for paciente in self.ultimos_pacientes_chamados[-5:]]
        

# Gerar uma simulação com pacientes aleatórios
def gerar_simulacao(pronto_socorro, num_pacientes):
    for _ in range(num_pacientes):
        nome = f'Paciente {random.randint(1, 100)}'
        idade = random.randint(1, 100)
        prioridade = random.randint(1, 10)
        paciente = Paciente(nome, idade, prioridade)
        pronto_socorro.adicionar_paciente(paciente)

pronto_socorro = ProntoSocorro()

while True:

    print('''Selecione a opção:
[1] Cadastrar paciente
[2] Atender paciente de maior prioridade
[3] Visualizar a fila
[4] Visualizar do próximo paciente
[5] Listar os cinco últimos pacientes chamados
[6] Gerar pacientes aleatórios
[0] Sair''')

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        # os.system("cls")
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        prioridade = int(input("Digite a prioridade do paciente: "))
        paciente = Paciente(nome, idade, prioridade)
        pronto_socorro.adicionar_paciente(paciente)
        # os.system("cls")

    elif opcao == 2:
        # os.system("cls")
        paciente_atendido = pronto_socorro.atender_proximo_paciente()
        if paciente_atendido:
            print(f"Atendendo {paciente_atendido.nome}, Idade: {paciente_atendido.idade}, Prioridade: {paciente_atendido.prioridade}")
        else:
            print("Não há mais pacientes na fila.")  
                              
    elif opcao == 3:
        # os.system("cls")
        if not pronto_socorro.visualizar_fila():
            print("Não há pacientes na fila")
        else:
            print(f'Fila: {pronto_socorro.visualizar_fila()}')

    elif opcao == 4:
        # os.system("cls")
        pronto_socorro.mostrar_proximo_paciente()

    elif opcao == 5:
        # os.system("cls")
        pronto_socorro.listar_ultimos_pacientes_chamados()

    elif opcao == 6:
        # os.system("cls")
        num_pacientes = int(input("Digite o número de pacientes: "))
        gerar_simulacao(pronto_socorro, num_pacientes)
        # os.system("cls")

    elif opcao == 0:
        # os.system("cls")
        print("Saindo...")
        break

    else:
        print("Opção inválida")
