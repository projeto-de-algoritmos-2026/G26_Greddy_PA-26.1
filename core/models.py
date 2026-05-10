class Node:
    def __init__(self, byte, freq):
        self.byte = byte
        self.freq = freq
        self.left = None
        self.right = None

    # Permite fazer comparações do tipo Node1 < Node2
    def __lt__(self, other):
        return self.freq < other.freq