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
    base_path = os.path.abspath(base_path)
    estrutura = []
    for root, dirs, files in os.walk(base_path):
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

def contexto_arquiteturas():
    return """
        Software Architectural Patterns Overview:

        1. Layered Architecture (Layers):
        - Organizes the system into layers (e.g., presentation, business, data).
        - Each layer has a specific responsibility.
        - Promotes maintainability, modularity, and separation of concerns.

        2. Model-View-Controller (MVC):
        - Divides the system into Model (data), View (user interface), and Controller (logic).
        - Common in web frameworks like Laravel, Django, and Spring.
        - Encourages clear separation between business logic and UI.

        3. Microservices Architecture:
        - System composed of independent services communicating through APIs.
        - Promotes scalability, fault isolation, and technology diversity.
        - Common in cloud-native applications (e.g., Netflix, Uber).

        4. Pipe-and-Filter Architecture:
        - Data flows through a series of filters connected by pipes.
        - Each filter transforms data and passes it along.
        - Common in data processing and streaming pipelines.

        5. Event-Driven Architecture:
        - Components communicate through events.
        - Promotes loose coupling and real-time responsiveness.
        - Used in message brokers and reactive systems.
    """

def analyze_architecture(base_path):
    # Collect structure
    estrutura_texto, total = coletar_estrutura_projeto(base_path)
    print(f"\n✅ Estrutura coletada: {total} entradas")
    print("--------------------------------------------------")
    print("\n".join(estrutura_texto.splitlines()[:30]))  # mostra início da estrutura
    print("...\n--------------------------------------------------")

    # Combine structure + architecture descriptions
    context = contexto_arquiteturas()
    full_text = context + "\n\n--- Project Structure ---\n" + estrutura_texto

    # Initialize the zero-shot classifier
    print("Carregando modelo do Hugging Face...")
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

    # Candidate architectural styles (labels)
    labels = [
        "Layered Architecture",
        "Model-View-Controller (MVC)",
        "Microservices Architecture",
        "Pipe-and-Filter Architecture",
        "Event-Driven Architecture",
        "Monolithic Architecture"
    ]

    print("Analisando estrutura do projeto...")
    resultado = classifier(full_text, candidate_labels=labels)

    print("\resultado da Classificação:")
    for label, score in zip(resultado["labels"], resultado["scores"]):
        print(f"  {label}: {score:.3f}")

    print(f"\nArquitetura mais provável: {resultado['labels'][0].upper()}")
    return resultado

if __name__ == "__main__":
    path = r"C:\Workspace\Senac-PSG"
    if not os.path.isdir(path):
        print("Caminho inválido. Verifique e tente novamente.")
    else:
        analyze_architecture(path)
