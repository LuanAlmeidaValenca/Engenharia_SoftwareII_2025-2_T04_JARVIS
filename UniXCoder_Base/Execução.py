import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np

class UniXCoder():
    def __init__(self):
        # Define o dispositivo (GPU se disponível, senão CPU)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        # Nome do modelo pré-treinado a ser utilizado
        self.model_name = "microsoft/unixcoder-base"
        # Carrega o tokenizer do modelo
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        # Carrega o modelo e move para o dispositivo selecionado
        self.model = AutoModel.from_pretrained(self.model_name).to(self.device)

    # Gera o embedding do código passado como string
    def get_unixcoder_embedding(self, code: str) -> np.ndarray:
        # Tokeniza o código fonte para o formato aceito pelo modelo
        tokens = self.tokenizer(
            code,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        ).to(self.device)

        # Desativa o cálculo de gradiente para não consumir memória desnecessária
        with torch.no_grad():
            outputs = self.model(**tokens)

        # Pega o embedding do primeiro token (CLS) e normaliza
        embedding = outputs.last_hidden_state[:, 0, :].cpu().numpy().flatten()
        return embedding / np.linalg.norm(embedding)


    # Calcula a similaridade do cosseno entre dois vetores
    @staticmethod
    def cosine_similarity(v1, v2):
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

    # Executa o processo de obtenção dos embeddings e calcula a similaridade entre dois códigos
    def run(self, codigo_1: str, codigo_2: str) -> float:
        emb1 = self.get_unixcoder_embedding(codigo_1)
        emb2 = self.get_unixcoder_embedding(codigo_2)
        similaridade = UniXCoder.cosine_similarity(emb1, emb2)
        return similaridade