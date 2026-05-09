import collections
import heapq
from core.models import Node

# pega o arquivo binário e calcula frequências
def get_frequencies(file_path):
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # O Counter gera um dicionário {byte: frequencia}
    frequencias = collections.Counter(data)
    
    return frequencias, data

# constrói árvore de huffman usando min-heap
def build_huffman_tree(frequencias):

    heap = [Node(byte, freq) for byte, freq in frequencias.items()]
    
    # Transforma a lista numa min-heap
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # une os nós
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        # nó unificado para a heap
        heapq.heappush(heap, merged)
        
    # raiz
    return heap[0] if heap else None

# Percorre a árvore e gera o dicionário de bits
def build_codes_dict(node, current_code="", codes_dict=None):
    if codes_dict is None:
        codes_dict = {}

    if node is None:
        return codes_dict

    # Se o nó tem um byte, então é folha
    if node.byte is not None:
        codes_dict[node.byte] = current_code
        return codes_dict

    # Vai para a esquerda -> 0
    build_codes_dict(node.left, current_code + "0", codes_dict)
    
    # Vai para a direita - 1
    build_codes_dict(node.right, current_code + "1", codes_dict)

    return codes_dict