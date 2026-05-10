import tkinter as tk

class HuffmanApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Simulador Huffman")
        self.window.geometry("450x250")
        self.window.eval('tk::PlaceWindow . center')

        # INTERFACE
        self.title_label = tk.Label(
            window,
            text="Compressão com código de Huffman",
            font=("Helvetica", 12, "bold")
        )
        self.title_label.pack(pady=15)

        # BOTÕES
        self.btn_process = tk.Button(
            window,
            text="1. Escolher Arquivo para Processar",
            width=30
        )
        self.btn_process.pack(pady=10)

        self.btn_save = tk.Button(
            window,
            text="2. Salvar Arquivo Decodificado",
            state=tk.DISABLED,
            width=30
        )
        self.btn_save.pack(pady=10)

        # STATUS
        self.status_label = tk.Label(window, text="Aguardando arquivo...", fg="gray")
        self.status_label.pack(pady=10)


if __name__ == "__main__":
    window = tk.Tk()
    app = HuffmanApp(window)
    window.mainloop()