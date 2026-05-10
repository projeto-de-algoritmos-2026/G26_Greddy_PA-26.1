import json

# Grava o arquivo .huff com o cabeçalho necessário para a descompressão
def save_compressed_file(output_path, frequencias, extra_padding, compressed_byte_array):

    # Prepara o dicionário do cabeçalho
    header_dict = {
        "padding": extra_padding,
        "frequencias": frequencias
    }

    # Converte o dicionário para uma string JSON e depois para bytes em UTF-8
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode('utf-8')

    # Calcula o tamanho exato desse cabeçalho
    header_size = len(header_bytes)

    # Abre o arquivo em modo de escrita binária
    with open(output_path, 'wb') as f:
        # 1. Grava o tamanho do cabeçalho usando 4 bytes (big-endian)
        f.write(header_size.to_bytes(4, byteorder='big'))

        # 2. Grava os bytes do cabeçalho (o JSON)
        f.write(header_bytes)

        # 3. Grava os dados comprimidos reais
        f.write(compressed_byte_array)


def load_compressed_file(input_path):
    """Lê o arquivo .huff e separa o cabeçalho dos dados comprimidos."""
    with open(input_path, 'rb') as f:

        header_size_bytes = f.read(4)

        if not header_size_bytes:
            return None, 0, bytearray() # Arquivo vazio

        header_size = int.from_bytes(header_size_bytes, byteorder='big')

        # Lendo o cabeçalho e transformando em JSON
        header_bytes = f.read(header_size)
        header_dict = json.loads(header_bytes.decode('utf-8'))

        extra_padding = header_dict["padding"]
        frequencias = {int(k): v for k, v in header_dict["frequencias"].items()}

        # Lendo o restante do arquivo
        compressed_byte_array = f.read()

    return frequencias, extra_padding, compressed_byte_array