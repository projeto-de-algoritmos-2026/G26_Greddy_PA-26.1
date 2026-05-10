from .models import Node
from .encoder import build_huffman_tree
from utils.file_manager import load_compressed_file


def decode_data(encoded_bits, root: Node):
    """
    Função responsável por decodificar a sequência de bits gerada pelo
    algoritmo de codificação do Huffman.

    O retorno é um array contendo a sequência de bytes decodificada.
    """

    # Se não tiver nenhum Nó, vamos retornar o byte vazio
    if not root:
        return b""

    decoded_bytes = bytearray()
    current_node = root

    # Navengando na árvore (esquerda = 0; direita = 1)
    for bit in encoded_bits:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # Se for um nó folha, nós salvamos aquele dado
        if current_node.byte is not None:
            decoded_bytes.append(current_node.byte)
            current_node = root

    return bytes(decoded_bytes)


def get_bit_string_from_bytes(compressed_bytes):
    """Função responsável por converter o array de bytes para um string com 0s e 1s."""
    return "".join(f"{byte:08b}" for byte in compressed_bytes)

def remove_padding(padded_bits, extra_padding):
    """Remove os zeros adicionais do final da string de bits."""
    if extra_padding > 0:
        return padded_bits[:-extra_padding]
    return padded_bits

def decompress_file(input_path, output_path):
    """
    Orquestra todo o processo de descompressão, abrindo o arquivo,
    reconstruindo a árvore e salvando o arquivo original.
    """

    # Lendo o arquivo comprimido
    frequencias, extra_padding, compressed_bytes = load_compressed_file(input_path)

    # Se o arquivo for vazio, não escrevemos nada
    if frequencias is None:
        with open(output_path, 'wb') as f:
            pass
        return

    # Tratando os dados
    padded_bits = get_bit_string_from_bytes(compressed_bytes)
    encoded_bits = remove_padding(padded_bits, extra_padding)

    # Percorrendo a árvore
    root = build_huffman_tree(frequencias)
    decoded_bytes = decode_data(encoded_bits, root)

    # Salvando o arquivo original
    with open(output_path, 'wb') as f:
        f.write(decoded_bytes)