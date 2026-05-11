# Compactador de Huffman

## Alunos
| Matrícula  | Aluno                                 |
| ---------- | ------------------------------------- |
| 23/1027121 | José Victor Gabriel Menezes da Costa  |
| 23/1011284 | Eduardo Silva Waski                   |

**Link Apresentação**: [https://www.youtube.com/watch?v=LINK_AQUI]

## Sobre 
Este projeto implementa um **Compactador e Descompactador de Arquivos** utilizando o **Algoritmo de Huffman**. O objetivo é demonstrar a aplicação prática de algoritmos ambiciosos em compactação de dados sem perdas.

## Funcionamento do Algoritmo

1.  **Cálculo de Frequências**: Varredura do arquivo para contar a ocorrência de cada byte.
2.  **Construção da Min-Heap**: Cada caractere torna-se um nó em uma fila de prioridade.
3.  **União**: Os dois nós de menor peso são removidos e unidos em um novo nó cuja frequência é a soma das duas anteriores.
4.  **Codificação**: Geração de um dicionário de bits (0 para esquerda, 1 para direita).
5.  **Bit-Packing**: Agrupamento da string de bits em bytes reais para armazenamento físico.

---

## Estrutura do Arquivo Comprimido (.huff)

Para que a descompressão seja possível, o arquivo gerado possui uma estrutura de cabeçalho que permite a reconstrução da árvore original:

| Seção           | Tamanho  | Conteúdo                                                     |
| :---            | :---     | :---                                                         |
| **Header Size** | 4 Bytes  | Inteiro indicando o tamanho do JSON.                         |
| **JSON Header** | Variável | Dicionário com as frequências e o valor do *padding*.        |
| **Data**        | Variável | Os dados originais convertidos em bits e agrupados em bytes. |

---

## Screenshots

Ainda não tem.

## Configuração e Execução

### Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Execução
1. **Clone o repositório**:
```bash
git clone https://github.com/projeto-de-algoritmos-2026/G26_Greddy_PA-26.1.git
cd "G26_Greedy_PA-26.1"
```

2. **Execute o arquivo principal**

```bash
python3 main.py
```