# Teste velocidade internet

import speedtest
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk

def medir_velocidade_internet():
    # Inicializar o teste de velocidade
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()

    # Medir velocidades de download e upload
    velocidade_download = s.download(threads=None) / 1000000  # Converter para Mbps
    velocidade_upload = s.upload(threads=None) / 1000000  # Converter para Mbps

    return velocidade_download, velocidade_upload

def gerar_grafico_velocidade():
    # Obter valores de velocidade
    velocidade_download, velocidade_upload = medir_velocidade_internet()

    # Criar os dados para o gráfico
    categorias = ['Download', 'Upload']
    velocidades = [velocidade_download, velocidade_upload]

    # Criar o gráfico de barras
    plt.figure(figsize=(8, 6))
    plt.bar(categorias, velocidades, color=['blue', 'orange'])
    plt.ylabel('Velocidade (Mbps)')
    plt.title('Velocidade de Download e Upload da Internet')

    # Exibir valores nas barras
    for i, valor in enumerate(velocidades):
        plt.text(i, valor + 0.5, f'{valor:.2f} Mbps', ha='center', color='black', fontsize=12)

    # Mostrar o gráfico
    plt.show()

def plotar_grafico_linha():
    # Inicializar listas vazias para armazenar as velocidades e os horários
    velocidades_download = []
    velocidades_upload = []
    tempos = []

    # Número de medições desejadas
    num_medicoes = 3

    # Realizar medições e armazenar os valores
    for _ in range(num_medicoes):
        # Medir velocidades
        velocidade_download, velocidade_upload = medir_velocidade_internet()

        # Adicionar as velocidades medidas e o tempo atual às listas
        velocidades_download.append(velocidade_download)
        velocidades_upload.append(velocidade_upload)
        tempos.append(datetime.now().strftime("%H:%M:%S"))

    # Criar o gráfico de linha
    plt.figure(figsize=(10, 6))
    plt.plot(tempos, velocidades_download, marker='o', label='Download', color='blue')
    plt.plot(tempos, velocidades_upload, marker='o', label='Upload', color='orange')
    plt.xlabel('Hora da Medição')
    plt.ylabel('Velocidade (Mbps)')
    plt.title('Velocidade de Download e Upload ao longo do Tempo')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Exibir o gráfico
    plt.tight_layout()
    plt.show()

def chamar_funcao_escolhida(escolha):
    if escolha == 1:
        medir_velocidade_internet()
    elif escolha == 2:
        gerar_grafico_velocidade()
    elif escolha == 3:
        plotar_grafico_linha()

def criar_interface_grafica():
    root = tk.Tk()
    root.title("Menu de Opções")

    def botao_clicado(escolha):
        chamar_funcao_escolhida(escolha)

    botao_medir = tk.Button(root, text="Medir velocidade", command=lambda: botao_clicado(1))
    botao_medir.pack()

    botao_gerar_grafico = tk.Button(root, text="Gerar gráfico de velocidade", command=lambda: botao_clicado(2))
    botao_gerar_grafico.pack()

    botao_plotar_grafico = tk.Button(root, text="Plotar gráfico de linha", command=lambda: botao_clicado(3))
    botao_plotar_grafico.pack()

    root.mainloop()

criar_interface_grafica()