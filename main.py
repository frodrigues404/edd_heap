import heapq
import random

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
            return None

    def listar_ultimos_pacientes_chamados(self):
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

print('''Selecione a opção:
      [1] Cadastrar paciente
      [2] Atender paciente de maior prioridade
      [3] Visualizar a fila
      [4] Visualizar do próximo paciente
      [5] Listar os cinco últimos pacientes chamados
      [0] Sair''')

opcao = int(input("Digite a opção: "))

while opcao != 0:
    if opcao == 1:
        pass
    elif opcao == 2:
        for _ in range(5):
            paciente_atendido = pronto_socorro.atender_proximo_paciente()
            if paciente_atendido:
                print(f"Atendendo {paciente_atendido.nome}, Idade: {paciente_atendido.idade}, Prioridade: {paciente_atendido.prioridade}")
            else:
                print("Não há mais pacientes na fila.")
    elif opcao == 3:
        if not pronto_socorro.visualizar_fila():
            print("Não há pacientes na fila")
        else:
            print(f'Fila: {pronto_socorro.visualizar_fila()}')
        break
    elif opcao == 4:
        pronto_socorro.mostrar_proximo_paciente()
    elif opcao == 5:
        pronto_socorro.listar_ultimos_pacientes_chamados()
    else:
        print("Opção inválida")

# Testes da implementação

# gerar_simulacao(pronto_socorro, 20)

# print("Fila de Pacientes:")
# print(pronto_socorro.visualizar_fila())

# print("\nPróximo Paciente:")
# print(pronto_socorro.mostrar_proximo_paciente())

# print("\nAtendendo Pacientes:")
# for _ in range(5):
#     paciente_atendido = pronto_socorro.atender_proximo_paciente()
#     if paciente_atendido:
#         print(f"Atendendo {paciente_atendido.nome}, Idade: {paciente_atendido.idade}, Prioridade: {paciente_atendido.prioridade}")
#     else:
#         print("Não há mais pacientes na fila.")

# print("\nÚltimos Pacientes Atendidos:")
# print(pronto_socorro.listar_ultimos_pacientes_chamados())
