import os
from transformers import pipeline

def coletar_estrutura_projeto(base_path, max_entries=None):
    """
    Percorre recursivamente o projeto e retorna uma string com a estrutura de arquivos e pastas.
    Exemplo:
    src/
      controller/
        main_controller.py
      model/
        user_model.py
    public/
      index.html
    """
    ignorar_pastas = {".git", "__pycache__", "node_modules", "venv", "env", ".idea", ".vscode"}
    base_path = os.path.abspath(base_path)
    estrutura = []
    for root, dirs, files in os.walk(base_path):
        if any(ignorar in root for ignorar in ignorar_pastas):
            continue
        rel_path = os.path.relpath(root, base_path)
        if rel_path == ".":
            rel_path = os.path.basename(base_path)
        estrutura.append(rel_path.replace("\\", "/") + "/")
        for f in files:
            estrutura.append(f"  {rel_path.replace('\\', '/')}/{f}")
        if max_entries and len(estrutura) > max_entries:
            estrutura.append("  ... (estrutura truncada)")
            break

    texto_estrutura = "\n".join(estrutura)
    return texto_estrutura, len(estrutura)

def analisar_padrao_arquitetural(base_path):
    """
    Analisa a estrutura do projeto para identificar o padrão arquitetural usando
    o modelo BART Large MNLI do Hugging Face.
    """
    estrutura_texto, total = coletar_estrutura_projeto(base_path)
    print(f"\n✅ Estrutura coletada: {total} entradas")
    print("--------------------------------------------------")
    print("\n".join(estrutura_texto.splitlines()[:30]))  # mostra início da estrutura
    print("...\n--------------------------------------------------")

    # Inicializa modelo
    print("Carregando modelo do Hugging Face...")
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Categorias de arquitetura conforme atividade
    categorias = [
        "monolithic architecture",
        "layered architecture",
        "MVC architecture",
        "microservices architecture",
        "event-driven architecture",
        "pipe-and-filter architecture"
    ]

    # Executa análise
    print("Analisando estrutura do projeto...")
    resultado = classifier(estrutura_texto, candidate_labels=categorias)

    print("\nResultados da Classificação:")
    for label, score in zip(resultado["labels"], resultado["scores"]):
        print(f"  {label}: {score:.3f}")

    print(f"\nArquitetura mais provável: {resultado['labels'][0].upper()}")
    return resultado

if __name__ == "__main__":
    caminho = r"C:\Workspace\JARVIS"

    if not os.path.isdir(caminho):
        print("❌ Caminho inválido. Verifique e tente novamente.")
    else:
        analisar_padrao_arquitetural(caminho)
