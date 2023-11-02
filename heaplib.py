# https://docs.python.org/3/library/heapq.html?highlight=heapq
import heapq

fila = [1,2,3]

heapq.heapify(fila)
print(list(fila))

heapq.heappush(fila, 4)
print(list(fila))

heapq.heappop(fila)
print(list(fila))

heapq.heappushpop(fila, 0)
print(list(fila))


# O Python ao comparar tuplas, caso haja empate entre o primeiro parâmetro, o segundo é usado para desempate
fila_prioridade = [(1, 1, 'Ana'), (22, 2,'Maria'), (33, 3,'Pedro'), (1, 4, 'Ana'), (5, 5, 'Lucas'), (6, 6, 'Clara')]

heapq.heapify(fila_prioridade)
print(list(fila_prioridade))

