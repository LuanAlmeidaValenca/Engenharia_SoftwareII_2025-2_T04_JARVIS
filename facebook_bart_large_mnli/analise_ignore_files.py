import os
from transformers import pipeline
from facebook_bart_large_mnli.utils.main import Utils

class FacebookIgnoreFiles:
    def __init__(self, caminho):
        self.caminho = caminho

    def analisar_padrao_arquitetural(self):
        """
        Analisa a estrutura do projeto para identificar o padrão arquitetural usando
        o modelo BART Large MNLI do Hugging Face.
        """
        estrutura_texto, total = Utils.coletar_estrutura_projeto(self.caminho, ignore_files=True)
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
            "pipe-and-filter architecture",
            "orchestrator-executor architecture",
            "multi-agent architecture"
        ]

        # Executa análise
        print("Analisando estrutura do projeto...")
        resultado = classifier(estrutura_texto, candidate_labels=categorias)

        print("\nResultados da Classificação:")
        for label, score in zip(resultado["labels"], resultado["scores"]):
            print(f"  {label}: {score:.3f}")

        print(f"\nArquitetura mais provável: {resultado['labels'][0].upper()}")
        return resultado

    def run(self):
        if not os.path.isdir(self.caminho):
            print("Caminho inválido. Verifique e tente novamente.")
        else:
            self.analisar_padrao_arquitetural()
