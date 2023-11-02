class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()

        return root

    def _heapify_down(self):
        index = 0
        while True:
            left_children_index = 2 * index + 1
            right_children_index = 2 * index + 2
            largest = index

            if (left_children_index < len(self.heap) and self.heap[left_children_index] > self.heap[largest]):
                largest = left_children_index
            
            if (right_children_index < len(self.heap) and self.heap[right_children_index] > self.heap[largest]):
                largest = right_children_index

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
        

    def _heapify_up(self, index):
        parent_index = (index -1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def show_level(self):
        print(self.heap)
        print()

        for i in range(len(self.heap)):
            parent = self.heap[i]
            left_child = self.heap[2 * i + 1] if 2 * i + 1 < len(self.heap) else ''
            right_child = self.heap[2 * i + 2] if 2 * i + 2 < len(self.heap) else ''
            print(" PARENT : " + str(parent) + " LEFT CHILD : " + str(left_child) + " RIGHT CHILD : " + str(right_child))
            print()
        print()

# Exemplo de uso:
heap = MaxHeap()
heap.push(17)
heap.push(36)
heap.push(25)
#heap.push(7)
#heap.push(3)
#heap.push(90)
#heap.push(1)
#heap.push(2)
#heap.push(19)

heap.show_level()

print(heap.pop())
heap.show_level()
