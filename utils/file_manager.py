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