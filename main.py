class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2
        return self.heap


    def pop(self):
        if len(self.heap) == 1: # since our array starts at [0], we basically have no node in our heap
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        pop_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and
            self.heap[2 * i + 1] < self.heap[2 * i] and
            self.heap[2 * i + 1] < self.heap[i]):
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[2 * i] < self.heap[i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break
        return pop_val


    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        self.heap[0] = 0
        index = (len(self.heap) - 1) // 2
        while index > 0:
            i = index
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[i] > self.heap[2 * i + 1]):
                    self.heap[i] , self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                    i = 2 * i
                else:
                    break
            index -= 1
        return self.heap





heap = Heap()
heap.heapify([60,50,80,40,30,10,70,20,90])
print(heap.heap)
heap.pop()
print(heap.heap)