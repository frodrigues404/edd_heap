import os
import random
from faker import Faker
import Paciente
import ProntoSocorro

pronto_socorro = ProntoSocorro.ProntoSocorro()

# Gerar uma simulação com pacientes aleatórios
def gerar_simulacao(pronto_socorro, num_pacientes):
    fake = Faker('en_US')
    for _ in range(num_pacientes):
        nome = f'Paciente {fake.name()}'
        idade = random.randint(1, 100)
        prioridade = random.randint(1, 10)
        paciente = Paciente.Paciente(nome, idade, prioridade)
        pronto_socorro.adicionar_paciente(paciente)



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
        os.system("cls")
        nome = input("Digite o nome do paciente: ")
        idade = int(input("Digite a idade do paciente: "))
        prioridade = int(input("Digite a prioridade do paciente: "))
        paciente = Paciente.Paciente(nome, idade, prioridade)
        pronto_socorro.adicionar_paciente(paciente)
        os.system("cls")

    elif opcao == 2:
        os.system("cls")
        paciente_atendido = pronto_socorro.atender_proximo_paciente()
        if paciente_atendido:
            print(f"Atendendo {paciente_atendido.nome}, Idade: {paciente_atendido.idade}, Prioridade: {paciente_atendido.prioridade}")
        else:
            print("Não há mais pacientes na fila.")  
                              
    elif opcao == 3:
        os.system("cls")
        if not pronto_socorro.visualizar_fila():
            print("Não há pacientes na fila")
        else:
            print(f'Fila: {pronto_socorro.visualizar_fila()}')

    elif opcao == 4:
        os.system("cls")
        if not pronto_socorro.mostrar_proximo_paciente():
            print("Não há pacientes na fila")
        else:
            print(pronto_socorro.mostrar_proximo_paciente())

    elif opcao == 5:
        os.system("cls")
        if not pronto_socorro.listar_ultimos_pacientes_chamados():
            print("Não há pacientes na fila")
        else:
            print(pronto_socorro.listar_ultimos_pacientes_chamados())

    elif opcao == 6:
        os.system("cls")
        num_pacientes = int(input("Digite o número de pacientes: "))
        gerar_simulacao(pronto_socorro, num_pacientes)
        os.system("cls")

    elif opcao == 0:
        os.system("cls")
        print("Saindo...")
        break

    else:
        print("Opção inválida")
