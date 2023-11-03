import unittest
import ProntoSocorro
import Paciente


class TestProntoSocorro(unittest.TestCase):
    def setUp(self):
        self.pronto_socorro = ProntoSocorro.ProntoSocorro()

    def test_adicionar_paciente(self):
        paciente = Paciente.Paciente("João", 30, 3)
        self.pronto_socorro.adicionar_paciente(paciente)
        self.assertEqual(len(self.pronto_socorro.fila_prioridades), 1)

    def test_atender_proximo_paciente(self):
        paciente = Paciente.Paciente("Maria", 25, 2)
        self.pronto_socorro.adicionar_paciente(paciente)
        atendido = self.pronto_socorro.atender_proximo_paciente()
        self.assertEqual(atendido.nome, "Maria")

    def test_visualizar_fila(self):
        paciente1 = Paciente.Paciente("Carlos", 35, 1)
        paciente2 = Paciente.Paciente("Ana", 40, 2)
        self.pronto_socorro.adicionar_paciente(paciente1)
        self.pronto_socorro.adicionar_paciente(paciente2)
        fila = self.pronto_socorro.visualizar_fila()
        self.assertEqual(fila, [("Carlos", 35, 1), ("Ana", 40, 2)])

    def test_mostrar_proximo_paciente(self):
        paciente = Paciente.Paciente("Pedro", 28, 5)
        self.pronto_socorro.adicionar_paciente(paciente)
        proximo = self.pronto_socorro.mostrar_proximo_paciente()
        self.assertEqual(proximo, ("Pedro", 28, 5))

    def test_listar_ultimos_pacientes_chamados(self):
        pacientes = [Paciente.Paciente("Rita", 50, 4),
                     Paciente.Paciente("José", 45, 3),
                     Paciente.Paciente("Fernanda", 55, 2),
                     Paciente.Paciente("Lucas", 32, 1)]
        for paciente in pacientes:
            self.pronto_socorro.adicionar_paciente(paciente)
            self.pronto_socorro.atender_proximo_paciente()
        ultimos = self.pronto_socorro.listar_ultimos_pacientes_chamados()
        self.assertEqual(ultimos, [("Rita", 50, 4), ("José", 45, 3), ("Fernanda", 55, 2), ("Lucas", 32, 1)])

if __name__ == '__main__':
    unittest.main()