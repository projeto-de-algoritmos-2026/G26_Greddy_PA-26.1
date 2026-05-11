import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

from core.encoder import compress_file
from core.decoder import decompress_file

ctk.set_appearance_mode("dark")

class HuffmanApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configurações da Janela ---
        self.title("Compressor")
        width = 500
        height = 400
        self.center_window(width, height)
        self.resizable(False, False)
        
        # Cores customizadas
        self.accent_green = "#2ECC71"
        self.accent_blue = "#3498DB"
        self.bg_card = "#2B2B2B"

        # --- Layout Principal ---
        # Header com cor de destaque
        self.header_frame = ctk.CTkFrame(self, fg_color="#1f538d", height=80, corner_radius=0)
        self.header_frame.pack(fill="x", side="top")

        self.title_label = ctk.CTkLabel(
            self.header_frame, 
            text="COMPRESSOR DE HUFFMAN", 
            font=ctk.CTkFont(family="Orbitron", size=24, weight="bold"),
            text_color="white"
        )
        self.title_label.place(relx=0.5, rely=0.5, anchor="center")

        # Container Central (O "Card")
        self.card = ctk.CTkFrame(self, fg_color=self.bg_card, corner_radius=15, border_width=2, border_color="#3D3D3D")
        self.card.pack(pady=30, padx=40, fill="both", expand=True)

        self.info_label = ctk.CTkLabel(
            self.card, 
            text="Escolha uma operação abaixo:", 
            font=ctk.CTkFont(size=14),
            text_color="#AAAAAA"
        )
        self.info_label.pack(pady=(20, 10))

        # --- Botões Estilizados ---
        self.btn_compress = ctk.CTkButton(
            self.card,
            text="📦  COMPRIMIR ARQUIVO",
            command=self.compress_action,
            height=50,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.accent_green,
            hover_color="#27AE60",
            text_color="#1A1A1A"
        )
        self.btn_compress.pack(pady=10, padx=30, fill="x")

        self.btn_decompress = ctk.CTkButton(
            self.card,
            text="🔓  RESTAURAR (.HUFF)",
            command=self.decompress_action,
            height=50,
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=self.accent_blue,
            hover_color="#2980B9",
            text_color="white"
        )
        self.btn_decompress.pack(pady=10, padx=30, fill="x")

        # --- Footer de Status ---
        self.status_label = ctk.CTkLabel(
            self, 
            text="● Sistema Pronto", 
            font=ctk.CTkFont(size=11),
            text_color="#777777"
        )
        self.status_label.pack(pady=(0, 15))

    def center_window(self, width, height):
        """Calcula o centro real da tela para posicionar a janela."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        
        self.geometry(f"{width}x{height}+{x}+{y}")

    def update_status(self, text, color="#AAAAAA"):
        self.status_label.configure(text=f"● {text}", text_color=color)
        self.update()

    def compress_action(self):
        input_path = filedialog.askopenfilename(title="Selecione o arquivo")
        if not input_path: return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".huff",
            filetypes=[("Huffman Files", "*.huff")]
        )
        if not output_path: return

        try:
            self.update_status("Comprimindo dados...", self.accent_green)
            compress_file(input_path, output_path)
            
            t_orig = os.path.getsize(input_path)
            t_comp = os.path.getsize(output_path)
            ganho = (1 - (t_comp/t_orig)) * 100

            messagebox.showinfo("Sucesso", f"Compressão concluída!\nEconomia de {ganho:.1f}%")
            self.update_status("Compressão realizada com sucesso", self.accent_green)
        except Exception as e:
            self.update_status("Erro no processo", "#E74C3C")
            messagebox.showerror("Erro", str(e))

    def decompress_action(self):
        input_path = filedialog.askopenfilename(filetypes=[("Huffman Files", "*.huff")])
        if not input_path: return

        output_path = filedialog.asksaveasfilename(title="Salvar como...")
        if not output_path: return

        try:
            self.update_status("Restaurando arquivo...", self.accent_blue)
            decompress_file(input_path, output_path)
            self.update_status("Arquivo restaurado", self.accent_blue)
            messagebox.showinfo("Sucesso", "O arquivo original foi recuperado!")
        except Exception as e:
            self.update_status("Erro na descompressão", "#E74C3C")
            messagebox.showerror("Erro", str(e))

if __name__ == "__main__":
    app = HuffmanApp()
    app.mainloop()