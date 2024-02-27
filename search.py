import os
import tkinter as tk
from tkinter import filedialog

def buscar_arquivos():
    # Obter a pasta selecionada
    pasta = pasta_var.get()

    # Obter os números da sequência para buscar
    sequencia = sequencia_entry.get().strip().split('OU')

    # Lista para armazenar os resultados da busca
    resultados = []

    # Realizar a busca pelos arquivos na pasta para cada número da sequência
    for num in sequencia:
        encontrado = False
        print(f"Procurando o número da sequência: {num.strip()}")
        for root, dirs, files in os.walk(pasta):
            for filename in files:
                print(f"  Verificando o arquivo: {filename}")
                # Verificar se o arquivo é PDF ou JPEG
                if filename.lower().endswith('.pdf') or filename.lower().endswith('.jpeg'):
                    # Verificar se o nome do arquivo corresponde exatamente ao número da sequência
                    nome_arquivo = os.path.splitext(filename)[0]  # Remove a extensão do arquivo
                    if num.strip() == nome_arquivo:
                        resultados.append(f"{num}: {filename}")
                        encontrado = True
                        print(f"    Arquivo {nome_arquivo} encontrado!")
                        break
            if encontrado:
                break
        if not encontrado:
            resultados.append(f"{num}: Não encontrado")

    # Escrever os resultados em um arquivo txt
    with open("resultados_busca.txt", "w") as arquivo:
        arquivo.write('\n'.join(resultados))
    print("Resultados salvos em resultados_busca.txt")
    resultado_text.config(text="Busca concluída. Resultados salvos em resultados_busca.txt")

# Criar a janela principal
root = tk.Tk()
root.title("Sistema de Busca")

# Criar uma variável para armazenar a pasta selecionada
pasta_var = tk.StringVar()

# Criar o botão para selecionar a pasta
selecionar_pasta_button = tk.Button(root, text="Selecionar Pasta", command=lambda: pasta_var.set(filedialog.askdirectory()))
selecionar_pasta_button.pack()

# Caixa de entrada para inserir os números da sequência
sequencia_label = tk.Label(root, text="Números da sequência (separados por 'OU'):")
sequencia_label.pack()
sequencia_entry = tk.Entry(root)
sequencia_entry.pack()

# Botão para iniciar a busca
buscar_button = tk.Button(root, text="Buscar Arquivos", command=buscar_arquivos)
buscar_button.pack()

# Exibição dos resultados da busca
resultado_text = tk.Label(root, text="")
resultado_text.pack()

# Executar a interface
root.mainloop()