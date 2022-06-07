import sys


class MinHeap:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0] * (self.max_size + 1)
        # setting the top of the heap to be the smallest possible int
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    @staticmethod
    def parent(pos):
        return pos // 2

    @staticmethod
    def leftChild(pos):
        return pos * 2

    @staticmethod
    def rightChild(pos):
        return (pos * 2) + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, f_pos, l_pos):
        self.Heap[f_pos], self.Heap[l_pos] = self.Heap[f_pos], self.Heap[f_pos]

    def minHeapify(self, pos):

        if not self.isLeaf(pos):

            if (self.Heap[pos] > self.Heap[self.leftChild(pos)]) or (self.Heap[pos] > self.Heap[self.rightChild(pos)]):

                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, element):
        if self.size >= self.max_size:
            return

        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) +
                  " LEFT CHILD : " + str(self.Heap[2 * i]) +
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))

    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


def main():
    import random

    heap = MinHeap(25)
    for i in range(25):
        heap.insert(random.randint(0, 100))

    heap.Print()


if __name__ == '__main__':
    main()
