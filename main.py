import os
import sys
from facebook_bart_large_mnli.analise_ptbr import analisar_padrao_arquitetural as fb_ptbr
from facebook_bart_large_mnli.analise_ing import analisar_padrao_arquitetural as fb_ing
from facebook_bart_large_mnli.analise_ing_contexto import analisar_padrao_arquitetural as fb_ing_contexto
from facebook_bart_large_mnli.analise_ignore_files import analisar_padrao_arquitetural as fb_ing_ignore
from facebook_bart_large_mnli.analise_ing_v2 import analisar_padrao_arquitetural as fb_ing_v2

# ------------------------------------------------------------
# Funções de escolha de modelo/método
# ------------------------------------------------------------

def escolher_modelo():
    modelos = {
        1: "facebook/bart-large-mnli",
        2: "UniXcoder-Base",
        3: "Sentence Transformers",
    }

    print("\n=== Escolha o MODELO de classificação ===")
    for chave, valor in modelos.items():
        print(f"  {chave}. {valor}")

    while True:
        try:
            escolha = int(input("Digite o número do modelo desejado (1/2/3): ").strip())
            if escolha in modelos:
                return escolha
            print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def escolher_modo_modelo():
    modos = {
        1: "português sem contexto",
        2: "inglês sem contexto",
        3: "inglês v2 com novas categorias",
        3: "inglês com contexto",
        5: "inglês ignorando arquivos/pastas comuns",
    }

    print("\n=== Escolha o MODO de análise ===")
    for chave, valor in modos.items():
        print(f"  {chave}. {valor}")

    while True:
        try:
            escolha = int(input("Digite o número do modo desejado (1/2/3/4/5): ").strip())
            if escolha in modos:
                return escolha
            print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


# ------------------------------------------------------------
# Implementação do modelo BART
# ------------------------------------------------------------

def modelo_bart_large_mnli():
    caminho = os.path.join(os.getcwd(), "JARVIS")
    modo = escolher_modo_modelo()

    # Seleção correta de cada módulo
    print("\nExecutando análise...")
    if modo == 1:
        fb_ptbr(caminho)
    elif modo == 2:
        fb_ing(caminho)
    elif modo == 3:
        fb_ing_v2(caminho)
    elif modo == 4:
        fb_ing_contexto(caminho)
    elif modo == 5:
        fb_ing_ignore(caminho)
    else:
        print("Modo inválido.")
        sys.exit(1)


# ------------------------------------------------------------
# Implementações futuras
# ------------------------------------------------------------

def modelo_unixcoder_base():
    print("⚠ Módulo UniXcoder-Base ainda não implementado.")


def modelo_sentence_transformers():
    print("⚠ Módulo Sentence Transformers ainda não implementado.")


# ------------------------------------------------------------
# Direcionador principal
# ------------------------------------------------------------

def go_to_modelo(escolha: int):
    if escolha == 1:
        modelo_bart_large_mnli()
    elif escolha == 2:
        modelo_unixcoder_base()
    elif escolha == 3:
        modelo_sentence_transformers()
    else:
        raise ValueError("Escolha inválida.")


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
if __name__ == "__main__":
    escolha = escolher_modelo()
    go_to_modelo(escolha)
