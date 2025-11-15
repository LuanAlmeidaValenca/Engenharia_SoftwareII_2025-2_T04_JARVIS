import os
from transformers import pipeline
from facebook_bart_large_mnli.utils.main import Utils

class FacebookIngContexto:
    def __init__(self, caminho):
        self.caminho = caminho

    def analisar_padrao_arquitetural(self):
        # Collect structure
        estrutura_texto, total = Utils.coletar_estrutura_projeto(self.caminho)
        print(f"\n✅ Estrutura coletada: {total} entradas")
        print("--------------------------------------------------")
        print("\n".join(estrutura_texto.splitlines()[:30]))  # mostra início da estrutura
        print("...\n--------------------------------------------------")

        # Combine structure + architecture descriptions
        context = Utils.contexto_arquiteturas()
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
            "Monolithic Architecture",
            "Orchestrator-Executor Architecture",
            "Multi-Agent Architecture"
        ]

        print("Analisando estrutura do projeto...")
        resultado = classifier(full_text, candidate_labels=labels)

        print("\resultado da Classificação:")
        for label, score in zip(resultado["labels"], resultado["scores"]):
            print(f"  {label}: {score:.3f}")

        print(f"\nArquitetura mais provável: {resultado['labels'][0].upper()}")
        return resultado

    def run(self):
        if not os.path.isdir(self.caminho):
            print("Caminho inválido. Verifique e tente novamente.")
        else:
            self.analisar_padrao_arquitetural()
