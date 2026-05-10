class Node:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    # Ensina o heapq a ordenar os nós com base na frequência
    def __lt__(self, other):
        return self.freq < other.freq