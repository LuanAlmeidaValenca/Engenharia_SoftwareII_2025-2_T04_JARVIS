import os
import sys

from facebook_bart_large_mnli import FacebookIngV2, FacebookIgnoreFiles, FacebookIng, FacebookIngContexto, FacebookPtbr
from UniXCoder_Base import UniXCoder


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
        4: "inglês com contexto",
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
        fb_ptbr = FacebookPtbr(caminho)
        fb_ptbr.run()
    elif modo == 2:
        fb_ing = FacebookIng(caminho)
        fb_ing.run()
    elif modo == 3:
        fb_ing_v2 = FacebookIngV2(caminho)
        fb_ing_v2.run()
    elif modo == 4:
        fb_ing_contexto = FacebookIngContexto(caminho)
        fb_ing_contexto.run()
    elif modo == 5:
        fb_ing_ignore = FacebookIgnoreFiles(caminho)
        fb_ing_ignore.run()
    else:
        print("Modo inválido.")
        sys.exit(1)


# ------------------------------------------------------------
# Implementações futuras
# ------------------------------------------------------------

def modelo_unixcoder_base():
    codigo_1 = input('Digite o primeiro código que deseja comparar: ')
    codigo_2 = input('Digite o segundo código que deseja comparar: ')

    model = UniXCoder()
    similaridade = model.run(codigo_1, codigo_2)

    print(f"Similaridade Semântica: {similaridade:.4f}")


def modelo_sentence_transformers():
    print("⚠ Módulo Sentence Transformers ainda não implementado.")


def go_to_modelo(escolha: int):
    if escolha == 1:
        modelo_bart_large_mnli()
    elif escolha == 2:
        modelo_unixcoder_base()
    elif escolha == 3:
        modelo_sentence_transformers()
    else:
        raise ValueError("Escolha inválida.")


if __name__ == "__main__":
    escolha = escolher_modelo()
    go_to_modelo(escolha)
