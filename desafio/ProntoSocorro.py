import heapq
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
        if not self.ultimos_pacientes_chamados:
            return None
        else:
            return [(paciente.nome, paciente.idade, paciente.prioridade) for paciente in self.ultimos_pacientes_chamados[-5:]]