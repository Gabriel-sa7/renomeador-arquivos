"""
Este módulo contém um script para renomear arquivos em massa
em um diretório especificado pelo usuário, usando uma interface
gráfica Tkinter.
"""
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def procurar_diretorio():
    """
    Abre uma janela de diálogo para o usuário selecionar um diretório.
    Atualiza o campo de entrada de diretório com o caminho selecionado.
    """
    diretorio = filedialog.askdirectory()
    entrada_diretorio.delete(0, tk.END)
    entrada_diretorio.insert(0, diretorio)


def renomear_arquivos():
    """
    Renomeia os arquivos no diretório especificado com base no padrão
    de nome fornecido. Exibe mensagens de status na interface gráfica.
    """
    diretorio = entrada_diretorio.get()
    padrao_nome = entrada_padrao.get()

    if not diretorio or not padrao_nome:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    try:
        contador = 1
        for nome_arquivo in os.listdir(diretorio):
            if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
                _, extensao = os.path.splitext(nome_arquivo)
                novo_nome = f"{padrao_nome}{contador}{extensao}"
                caminho_antigo = os.path.join(diretorio, nome_arquivo)
                caminho_novo = os.path.join(diretorio, novo_nome)
                os.rename(caminho_antigo, caminho_novo)
                area_status.insert(
                    tk.END, f"Arquivo '{
                        nome_arquivo}' renomeado para '{novo_nome}'\n"
                )
                contador += 1
        messagebox.showinfo("Sucesso", "Arquivos renomeados com sucesso!")

    except OSError as e:
        messagebox.showerror("Erro", f"Erro ao renomear arquivo: {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")


# Configuração da janela principal
janela = tk.Tk()
janela.title("Renomeador de Arquivos em Massa")

# Frame para o diretório
frame_diretorio = tk.Frame(janela)
frame_diretorio.pack(pady=10)

label_diretorio = tk.Label(frame_diretorio, text="Diretório:")
label_diretorio.pack(side=tk.LEFT)

entrada_diretorio = tk.Entry(frame_diretorio, width=40)
entrada_diretorio.pack(side=tk.LEFT, padx=5)

botao_procurar = tk.Button(
    frame_diretorio, text="Escolher...", command=procurar_diretorio
)
botao_procurar.pack(side=tk.LEFT)

# Frame para o padrão de nome
frame_padrao = tk.Frame(janela)
frame_padrao.pack(pady=10)

label_padrao = tk.Label(frame_padrao, text="Padrão de Nome:")
label_padrao.pack(side=tk.LEFT)

entrada_padrao = tk.Entry(frame_padrao, width=40)
entrada_padrao.insert(0, "arquivo-")  # Valor padrão
entrada_padrao.pack(side=tk.LEFT, padx=5)

# Botão Renomear
botao_renomear = tk.Button(
    janela, text="Renomear Arquivos", command=renomear_arquivos
)
botao_renomear.pack(pady=20)

# Área de Status
area_status = tk.Text(janela, height=10, width=50)
area_status.pack()

janela.mainloop()
