from .models import Node


def decode_data(encoded_bits, root: Node):
    """
    Função responsável por decodificar a sequência de bits gerada pelo
    algoritmo de codificação do Huffman.

    O retorno é um array contendo a sequência de bytes decodificada.
    """

    if not root:
        return

    decoded_bytes = bytearray()
    current_node = root

    # Navengando na árvore (esquerda = 0; direita = 1)
    for bit in encoded_bits:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        # Se for um nó folha, nós salvamos aquele dado
        if current_node.byte:
            decoded_bytes.append(current_node.byte)
            current_node = root

    return bytes(decoded_bytes)