"""
FarmTech Solutions — Aplicativo Python

Funcionalidades:
- Culturas: SOJA (retangular) e CAFÉ (circular)
- Cálculo de área
- Cálculo de manejo de insumos (por área ou por linha)
"""

import math
import csv

# Vetores de dados
TALHOES = []
MANEJOS = []

# Funções auxiliares
def gerar_id(lista):
    return len(lista) + 1

def escolher_cultura():
    op = input("1) SOJA | 2) CAFÉ: ").strip()
    return "SOJA" if op == "1" else "CAFÉ"

# Talhões
def cadastrar_talhao():
    cultura = escolher_cultura()
    if cultura == "SOJA":
        c = float(input("Comprimento (m): "))
        l = float(input("Largura (m): "))
        area = c * l
        TALHOES.append({"id": gerar_id(TALHOES), "cultura": cultura, "area": area})
    else:
        r = float(input("Raio (m): "))
        area = math.pi * r**2
        TALHOES.append({"id": gerar_id(TALHOES), "cultura": cultura, "area": area})
    print("Talhão cadastrado!")

def listar_talhoes():
    for t in TALHOES:
        print(f"ID {t['id']} | {t['cultura']} | Área: {t['area']:.2f} m²")

# Manejo
def cadastrar_manejo():
    cultura = escolher_cultura()
    produto = input("Produto: ")
    modo = input("1) Área | 2) Linha: ").strip()
    if modo == "1":
        if not TALHOES:
            print("Cadastre um talhão antes.")
            return
        listar_talhoes()
        tid = int(input("ID do talhão: "))
        dose = float(input("Dose (L/ha): "))
        talhao = next((t for t in TALHOES if t["id"] == tid), None)
        if talhao:
            total = dose * (talhao["area"]/10000)
            MANEJOS.append({"id": gerar_id(MANEJOS), "cultura": cultura, "produto": produto, "total": total})
            print(f"Total: {total:.2f} L")
    else:
        dose = float(input("Dose (mL/m): "))
        linhas = int(input("Nº linhas: "))
        comp = float(input("Comp/linha (m): "))
        total = (dose * linhas * comp) / 1000
        MANEJOS.append({"id": gerar_id(MANEJOS), "cultura": cultura, "produto": produto, "total": total})
        print(f"Total: {total:.2f} L")

def listar_manejos():
    for m in MANEJOS:
        print(f"ID {m['id']} | {m['cultura']} | {m['produto']} | Total: {m['total']:.2f} L")

# Exportação
def exportar_csv():
    if not TALHOES and not MANEJOS:
        print("Não há dados para exportar. Cadastre um talhão ou manejo primeiro.")
        return

    with open("dados_fazenda.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Escreve o cabeçalho
        writer.writerow(["Tipo", "ID", "Cultura", "Area_m2", "Produto", "Insumo_Total_L"])

        # Escreve os dados dos talhões
        for t in TALHOES:
            writer.writerow(["Talhao", t['id'], t['cultura'], f"{t['area']:.2f}", "", ""])

        # Escreve os dados dos manejos
        for m in MANEJOS:
            writer.writerow(["Manejo", m['id'], m['cultura'], "", m['produto'], f"{m['total']:.2f}"])

    print("Dados exportados com sucesso para 'dados_fazenda.csv'!")

# Menu principal
def menu():
    while True:
        print("\n1) Cadastrar Talhão\n2) Listar Talhões\n3) Cadastrar Manejo\n4) Listar Manejos\n5) Exportar para CSV\n0) Sair")
        op = input("Opção: ")
        if op == "1": cadastrar_talhao()
        elif op == "2": listar_talhoes()
        elif op == "3": cadastrar_manejo()
        elif op == "4": listar_manejos()
        elif op == "5": exportar_csv()
        elif op == "0": break
        else: print("Inválido!")

if __name__ == "__main__":
    menu()
