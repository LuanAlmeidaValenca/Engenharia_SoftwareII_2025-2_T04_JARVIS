# Projeto de Análise Arquitetural – Microsoft JARVIS / HuggingGPT

## Universidade Federal de Sergipe – Departamento de Computação

- **Disciplina:** Engenharia de Software II
- **Professor:** Glauco de Figueiredo Carneiro
- **Data:** 13/11/2025

---

# 📌 1. Sobre o Projeto

Este repositório contém **toda a análise arquitetural** realizada pelo grupo sobre o projeto **Microsoft JARVIS (HuggingGPT)**, incluindo:

* Identificação manual da arquitetura
* Análise automatizada com modelos de linguagem
* Comparação dos resultados
* Conclusões finais
* Estrutura do projeto e como executar nossos scripts

O objetivo central da atividade foi **avaliar padrões arquiteturais** presentes no JARVIS por meio de investigação manual e com auxílio de modelos de IA.

---

# 👥 2. Integrantes e Organização

O grupo é composto por:

* Arthur Costa Oliveira (202300027104)
* Davi Lira Santana (202300083319)
* Gabriel Batista Barbosa (202300027249)
* João Henrique Britto Bomfim (202300027409)
* Luan Almeida Valença (202300027866)
* Matheus Nascimento dos Santos (202300083810)
* Paulo Henrique Melo Rugani de Sousa (202300027919)
* Tassio Mateus de Carvalho (202300083963)

### Estrutura de Trabalho do Grupo

O grupo se dividiu em **4 duplas**, cada uma responsável por uma parte da análise:

* **Dupla 1 – Tássio e João:** Identificação manual da arquitetura e documentação.
* **Dupla 2 – Davi e Paulo:** Análise com *facebook/bart-large-mnli* (classificação zero-shot).
* **Dupla 3 – Luan e Matheus:** Análise por similaridade de código usando *UniXcoder-base*.
* **Dupla 4 – Gabriel e Arthur:** Análise com embeddings e clustering via *all-MiniLM-L6-v2*.

Além disso, todo o grupo discutiu os achados em conjunto em reuniões gerais de alinhamento.

---

# 🧩 3. Projeto Selecionado – Microsoft JARVIS

O **Microsoft JARVIS / HuggingGPT** é um sistema que integra múltiplos modelos de IA, utilizando um **LLM como orquestrador central**. Ele transforma comandos em linguagem natural em um **pipeline de 4 estágios**:

1. Planejamento de tarefas
2. Seleção de modelos
3. Execução das tarefas
4. Geração da resposta final

O projeto foi escolhido pela sua natureza modular e altamente arquitetural, sendo ideal para esta atividade.

---

# 🏗️ 4. Identificação Manual da Arquitetura

A análise manual concluiu que o JARVIS segue principalmente:

### ✔ **Padrão Controlador–Executor**

Um LLM atua como **controlador inteligente**, e os modelos do Hugging Face como **executores especializados**.

### ✔ **Pipeline de 4 Estágios (Pipe-and-Filter)**

O fluxo da aplicação é rigidamente dividido em:

1. Planejamento
2. Seleção de modelo
3. Execução
4. Geração de resposta

O sistema **não** se encaixa bem em:

* Arquitetura em camadas (violação de chamadas diretas)
* Arquitetura multi‑agente (executores não possuem autonomia)

Um documento completo com descrições detalhadas está incluído neste repositório.

---

# 🤖 5. Análise com Modelos de Linguagem

O projeto contém **3 frentes de análise automatizada**:

## 🔹 5.1 facebook/bart-large-mnli (classificação zero-shot)

Baseado na estrutura de diretórios. O modelo retornou maior probabilidade para **arquitetura multi-agente**, embora isso não se confirme completamente na análise manual.

O script coletou a estrutura do repositório e classificou entre diversas arquiteturas.

## 🔹 5.2 UniXcoder-base (similaridade de código)

Compara a semântica entre funções diferentes para identificar papéis arquiteturais semelhantes.

## 🔹 5.3 all-MiniLM-L6-v2 (embeddings + clustering)

Clustering identificou grupos coerentes relacionados a etapas funcionais do JARVIS.

---

# 📂 6. Estrutura Deste Repositório

```

 ┣ all_MiniLM_L6_v2
 ┃ ┣ sentence_transformers.ipynb
 ┃ ┗ sentence_transformers.py
 ┣ Analise-Manual
 ┃ ┣ orquestrador-controlador.py
 ┃ ┣ pipeline1.py
 ┃ ┣ pipeline2.py
 ┃ ┣ pipeline3.py
 ┃ ┗ pipeline4.py
 ┣ facebook_bart_large_mnli
 ┃ ┣ utils/
 ┃ ┣ __init__
 ┃ ┣ analise_ignore_files.py
 ┃ ┣ analise_ing_contexto.py
 ┃ ┣ analise_ing_v2.py
 ┃ ┣ analise_ing.py
 ┃ ┗ analise_ptbr.py
 ┣ JARVIS
 ┣ UniXCoder_Base
 ┃ ┣ __init__.py
 ┃ ┣ Execução.ipynb
 ┃ ┗ Execução.py
 ┣ README.md               # Documentação do projeto
 ┗ requirements.txt        # Dependências
```

---

# ▶️ 7. Como Executar o Projeto

Instale as dependências:

```bash
pip install -r requirements.txt
```

Dependências incluem:

* transformers
* torch
* sentence-transformers
* numpy

```bash
py main.py
```

---

# 🧪 7.2. Análise do BART MNLI

Saída: lista de probabilidades por arquitetura.

---

# 🧪 7.3. Análise Embeddings com UniXcoder

O script imprime a similaridade de cosseno entre funções.

---

# 🧪 7.4. Análise Clustering com all-MiniLM-L6-v2

O script gera clusters de significado entre trechos do código.

---

# 📌 8. Conclusão Geral

A combinação das três análises e da investigação manual permitiu concluir que:

### ✔ O Microsoft JARVIS segue primariamente:

* **Arquitetura Controlador–Executor**
* **Pipeline Pipe-and-Filter com 4 estágios**

### ✔ Outras arquiteturas aparecem superficialmente, mas não definem o sistema.

A modularidade e a dependência centralizada do LLM são elementos marcantes que tornam essa arquitetura eficiente e extensível.

---
