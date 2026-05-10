import tkinter as tk
from tkinter import filedialog, messagebox
import os

from core.encoder import compress_file
from core.decoder import decompress_file

class HuffmanApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Compactador Huffman")
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
        self.btn_compress = tk.Button(
            window,
            text="Comprimir Arquivo",
            command=self.compress_action,
            width=30
        )
        self.btn_compress.pack(pady=10)

        self.btn_decompress = tk.Button(
            window,
            text="Descomprimir Arquivo (.huff)",
            command=self.decompress_action,
            width=30
        )
        self.btn_decompress.pack(pady=10)

        # STATUS
        self.status_label = tk.Label(window, text="Aguardando ação...", fg="gray")
        self.status_label.pack(pady=10)


    def compress_action(self):
        """Fluxo para selecionar, comprimir e salvar um arquivo."""
        # Escolhe o arquivo de entrada
        input_path = filedialog.askopenfilename(title="Selecione o arquivo para comprimir")
        if not input_path:
            return # Usuário cancelou

        # Escolhe onde salvar
        output_path = filedialog.asksaveasfilename(
            title="Salvar arquivo comprimido como...",
            defaultextension=".huff",
            filetypes=[("Arquivos Huffman", "*.huff"), ("Todos os arquivos", "*.*")]
        )
        if not output_path:
            return

        # Comprimindo
        try:
            self.status_label.config(text="Comprimindo arquivo... Aguarde.", fg="blue")
            self.window.update()

            compress_file(input_path, output_path)

            # Coleta estatísticas para mostrar pro usuário
            tamanho_orig = os.path.getsize(input_path)
            tamanho_comp = os.path.getsize(output_path)

            self.status_label.config(text="Arquivo comprimido com sucesso!", fg="green")
            messagebox.showinfo(
                "Sucesso",
                f"Compressão finalizada!\n\n"
                f"Tamanho original: {tamanho_orig} bytes\n"
                f"Tamanho comprimido: {tamanho_comp} bytes"
            )

        except Exception as e:
            self.status_label.config(text="Erro na compressão.", fg="red")
            messagebox.showerror("Erro", f"Ocorreu um erro ao comprimir:\n{str(e)}")


    def decompress_action(self):
        """Fluxo para selecionar um .huff, descomprimir e salvar o original."""

        # Escolhe um arquivo comprimido (.huff)
        input_path = filedialog.askopenfilename(
            title="Selecione o arquivo .huff para restaurar",
            filetypes=[("Arquivos Huffman", "*.huff"), ("Todos os arquivos", "*.*")]
        )
        if not input_path:
            return

        # Escolhe onde salvar o arquivo recuperado
        output_path = filedialog.asksaveasfilename(
            title="Salvar como (Ex: arquivo.txt ou imagem.png)",
            defaultextension=".*",
            filetypes=[("Todos os arquivos", "*.*")]
        )
        if not output_path:
            return

        # Descomprime
        try:
            self.status_label.config(text="Descomprimindo arquivo... Aguarde.", fg="blue")
            self.window.update()

            decompress_file(input_path, output_path)

            self.status_label.config(text="Arquivo restaurado com sucesso!", fg="green")
            messagebox.showinfo("Sucesso", f"Arquivo restaurado salvo em:\n{output_path}")

        except Exception as e:
            self.status_label.config(text="Erro na descompressão.", fg="red")
            messagebox.showerror("Erro", f"Ocorreu um erro ao descomprimir:\n{str(e)}")


if __name__ == "__main__":
    window = tk.Tk()
    app = HuffmanApp(window)
    window.mainloop()