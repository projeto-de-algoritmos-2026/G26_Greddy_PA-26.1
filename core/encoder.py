import collections
import heapq
from core.models import Node
from utils.file_manager import save_compressed_file

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

# Transforma os dados originais em uma string de bits
def encode_data(data, codes_dict):
    encoded_bits = "".join([codes_dict[byte] for byte in data])
    return encoded_bits

# Adiciona zeros ao final para que o tamanho da string seja múltiplo de 8
def pad_encoded_data(encoded_bits):
    extra_padding = 8 - (len(encoded_bits) % 8)
    
    if extra_padding == 8:
        extra_padding = 0
        
    padded_bits = encoded_bits + ("0" * extra_padding)
    
    return padded_bits, extra_padding

# Converte a string de bits em um array de bytes
def get_byte_array(padded_bits):
    b = bytearray()
    
    for i in range(0, len(padded_bits), 8):
        byte_str = padded_bits[i:i+8]
        # Converte a string de base 2 (ex: "10110010") para um byte real e adiciona
        b.append(int(byte_str, 2))
        
    return b

# Função principal que orquestra todo o processo de compressão
def compress_file(input_path, output_path):
    
    # Lê o arquivo e pega as frequências
    frequencias, data = get_frequencies(input_path)
    
    # Trata o caso extremo de arquivo vazio
    if not data:
        with open(output_path, 'wb') as f:
            pass # Cria um arquivo vazio e encerra
        return
        
    # Constrói a árvore de Huffman
    root = build_huffman_tree(frequencias)
    
    # Gera a tabela de conversão
    codes_dict = build_codes_dict(root)
    
    # Transforma os dados em bits
    encoded_bits = encode_data(data, codes_dict)
    
    # Adiciona o Padding
    padded_bits, extra_padding = pad_encoded_data(encoded_bits)
    
    # Converte para array de bytes reais
    compressed_byte_array = get_byte_array(padded_bits)
    
    # Salva o arquivo final
    save_compressed_file(output_path, frequencias, extra_padding, compressed_byte_array)