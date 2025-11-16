import os
import matplotlib.pyplot as plt
import networkx as nx
import re
from tqdm import tqdm
from collections import defaultdict
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

root_dir = "JARVIS"
texts = []
file_paths = []
valid_ext = (".md", ".json", ".py", ".yaml", ".yml")

for folder, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(valid_ext):
            path = os.path.join(folder, file)
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    texts.append(content)
                    file_paths.append(path)
            except Exception as e:
                print(f"Erro ao ler {path}: {e}")

print(f"Total de arquivos de texto extraídos: {len(texts)}")
print(f"Exemplo de arquivo: {file_paths[0]}")
print(texts[0][:500])

!pip install -q sentence-transformers

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

print(f"Tamanho da matriz de embeddings: {embeddings.shape}")
print(f"Exemplo de embedding (primeiro vetor):\n{embeddings[0][:10]}")

num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(embeddings)

for i in range(num_clusters):
    print(f"\n=== Cluster {i} ===")
    for j, label in enumerate(labels):
        if label == i:
            print(f"- {file_paths[j]}")


pca = PCA(n_components=2, random_state=42)
reduced = pca.fit_transform(embeddings)

plt.figure(figsize=(8,6))
plt.scatter(reduced[:,0], reduced[:,1], c=labels, cmap='tab10')
plt.title("Clusters de Arquivos JARVIS (KMeans)")
plt.xlabel("Componente 1")
plt.ylabel("Componente 2")
plt.colorbar(label="Cluster ID")
plt.show()

summary_model = SentenceTransformer('all-MiniLM-L6-v2')

for i in range(num_clusters):
    textos_cluster = [texts[j] for j, label in enumerate(labels) if label == i]
    resumo = textos_cluster[0][:400] if textos_cluster else "N/A"
    print(f"\n🔹 Cluster {i}: {len(textos_cluster)} arquivos")
    print(f"Exemplo de conteúdo:\n{resumo}\n")

G = nx.DiGraph()

for path, cluster in zip(file_paths, labels):
    G.add_node(path, cluster=int(cluster))

import_pattern = re.compile(r'(?:from|import)\s+([a-zA-Z0-9_.\-]+)')

for path, text in tqdm(zip(file_paths, texts), total=len(file_paths)):
    matches = import_pattern.findall(text)
    for m in matches:
        for other in file_paths:
            name = os.path.splitext(os.path.basename(other))[0]
            if name in m:
                G.add_edge(path, other)

cluster_colors = {
    0: "#FF6B6B",  # vermelho
    1: "#FFD93D",  # amarelo
    2: "#6BCB77",  # verde
    3: "#4D96FF",  # azul
    4: "#9D4EDD",  # roxo
    5: "#FF8C00"   # laranja
}

pos = nx.spring_layout(G, k=0.75, iterations=80, seed=42)

node_colors = [cluster_colors.get(G.nodes[n]['cluster'], "#CCCCCC") for n in G.nodes]
node_sizes = [300 if G.out_degree(n) > 2 else 150 for n in G.nodes]  # destaca nós mais conectados

plt.figure(figsize=(14, 10))
plt.style.use("seaborn-v0_8-whitegrid")

nx.draw_networkx_edges(
    G, pos,
    edge_color="lightgray",
    alpha=0.5,
    width=1
)

nodes = nx.draw_networkx_nodes(
    G,
    pos,
    node_size=node_sizes,
    node_color=node_colors,
    alpha=0.9,
    linewidths=0.5,
    edgecolors="black"
)

for cluster_id, color in cluster_colors.items():
    plt.scatter([], [], c=color, label=f"Cluster {cluster_id}")

plt.legend(
    title="Clusters Semânticos",
    loc="upper right",
    frameon=True,
    fontsize=9,
    title_fontsize=11
)

plt.title("🔍 Grafo de Dependências do Projeto JARVIS (por Cluster)", fontsize=18, weight='bold', pad=20)
plt.axis("off")

descricao = (
    "Cada nó representa um arquivo do projeto JARVIS. \nAs cores identificam os clusters semânticos (funções similares).\n"
    "As arestas indicam relações de dependência entre módulos.\n\n"
    "- Cluster 0: Configurações web (TypeScript / Electron)\n"
    "- Cluster 1: Documentação e exemplos\n"
    "- Cluster 2: Núcleo funcional (servidores e módulos principais em Python)\n"
    "- Cluster 3: Processamento e manipulação de dados\n"
    "- Cluster 4: Políticas, licenças e segurança\n"
    "- Cluster 5: Dados e ferramentas externas (JSON)"
)

plt.text(
    -1.15, -1.1,
    descricao,
    fontsize=10.5,
    color='black',
    verticalalignment='bottom',
    bbox=dict(boxstyle="round,pad=0.6", fc="white", ec="gray", alpha=0.8)
)

plt.tight_layout()
plt.show()

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(14, 10))
ax.axis('off')

texto = """
                            Análise Arquitetural do Projeto Microsoft JARVIS

    - Metodologia de Descoberta
1. Foram gerados embeddings com um modelo MiniLM (Hugging Face),
   representando semanticamente o conteúdo de cada arquivo.
2. Em seguida, aplicou-se clustering (K-Means) sobre esses vetores para agrupar
   arquivos com função e papel similares no sistema.
3. Os grupos resultantes (clusters) foram analisados conforme suas dependências e nomes,
   revelando um padrão de arquitetura em camadas com suporte a plugins.


    - Padrão Arquitetural Identificado: Arquitetura Modular em Camadas
Camada de Interface (Cluster 0)
   - Arquivos Web/Electron (`tsconfig.json`, `package.json`);
   - Responsável pela apresentação, build e interação com o usuário.

Camada de Lógica de Negócio (Cluster 2)
   - Módulos Python (`server`, `easytool`, `taskbench`);
   - Gerencia a oordenação entre modelos de IA e orquestra as tarefas.

Camada de Dados (Cluster 3)
   - Scripts de processamento e análise de datasets;
   - Responsável por tratar e avaliar dados externos.

Camada de Infraestrutura (Cluster 4)
   - Arquivos de configuração e segurança (`SECURITY.md`, `.yml`);
   - Define as políticas, deploy e governança do sistema.

Camada de Extensões (Cluster 5)
   - Arquivos JSON descrevendo ferramentas externas;
   - Implementa o mecanismo de plugins para expandir funcionalidades.


    - Conclusão
A análise dos embeddings e clusters revelou que o JARVIS:

- Segue uma arquitetura em camadas, separando interface, lógica e dados;
- Adota princípios de arquitetura em camadas com suporte a plugins, permitindo extensões modulares;
- Mantém baixo acoplamento entre camadas e alta extensibilidade do sistema.

Isso indica uma organização de software madura e flexível, voltada à integração entre
múltiplos modelos de IA e componentes externos.
"""

ax.text(
    0.02, 0.97, texto,
    fontsize=11.5,
    va='top',
    ha='left',
    color="#222222",
    wrap=True,
    bbox=dict(boxstyle="round,pad=0.6", fc="white", ec="lightgray", alpha=0.9)
)

plt.title(
    "Padrão Arquitetural do Projeto Microsoft JARVIS",
    fontsize=17,
    fontweight='bold',
    pad=25,
    color="#2b4c7e"
)

plt.tight_layout()
plt.show()