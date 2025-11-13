# Análise Arquitetural do Microsoft JARVIS com Modelos de Linguagem

Este repositório contém o estudo, implementação e comparação de diferentes técnicas de Inteligência Artificial aplicadas para identificar padrões arquiteturais no projeto **Microsoft JARVIS (HuggingGPT)**.
Foram utilizados três modelos principais e múltiplas variações de código para avaliar automaticamente a arquitetura a partir da estrutura de diretórios e arquivos do projeto.

---

# Sobre o Projeto JARVIS

O **Microsoft JARVIS/HuggingGPT** é um sistema que integra múltiplos modelos de IA para resolver tarefas complexas.
Ele funciona como um **Orquestrador-Executor**, onde:

* O **Orquestrador** é um LLM (como GPT-4), responsável por interpretar a solicitação, decompor tarefas, selecionar modelos especializados e integrar os resultados.
* Os **Executores** são modelos especializados hospedados no Hugging Face, acionados sob demanda via API.

Internamente, o orquestrador segue um **pipeline em quatro estágios**:

1. Task Planning
2. Model Selection
3. Task Execution
4. Response Generation

Esse fluxo confere ao sistema características que lembram:

* Arquitetura Orquestrador-Executor (padrão central)
* Estilo Pipe-and-Filter no pipeline interno
* Modularidade semelhante a arquiteturas em camadas e plugins

---

# Modelos de IA Utilizados na Análise

Três modelos foram aplicados para avaliar o projeto sob perspectivas diferentes, explorando estrutura de diretórios, código-fonte e conteúdo textual.

---

## 1. BART Large MNLI (HuggingFace)

Modelo de zero-shot classification usado para inferir padrões arquiteturais observando **somente os nomes das pastas e arquivos**.

### Objetivo

Identificar qual arquitetura o projeto mais se aproxima com base em texto semântico gerado pela estrutura do repositório.

### Como funciona

1. A estrutura do projeto é percorrida recursivamente.
2. Os nomes de diretórios e arquivos são convertidos em texto.
3. O texto é enviado ao modelo BART-MNLI.
4. O modelo gera probabilidades para cada arquitetura candidata.

### Observações sobre as variações utilizadas

Durante o estudo, o método foi testado em diferentes cenários:

* categorias em português
* categorias em inglês
* categorias modernas (como RAG, Federated Learning)
* versões com contexto adicional sobre cada arquitetura
* variações que ignoram pastas irrelevantes, como `.git` e `node_modules`

Essas versões serviram apenas para comparar como pequenas mudanças de contexto, idioma e filtragem de arquivos influenciam o comportamento do modelo.

---

## 2. UniXcoder-Base (Microsoft)

Modelo transformer voltado para código-fonte, capaz de extrair embeddings semânticos de funções e analisar similaridade estrutural.

### Objetivo

Comparar trechos de código para identificar:

* padrões funcionais
* similaridade entre módulos
* organização arquitetural

### Funcionamento

1. O código é transformado em vetores (embeddings).
2. Calcula-se a similaridade de cosseno entre funções.
3. Similaridades elevadas indicam papéis equivalentes entre módulos.
4. Os padrões encontrados apontam para um comportamento alinhado a **Arquitetura em Camadas**.

---

## 3. MiniLM-L6-v2 (Sentence Transformers)

Modelo eficiente para gerar embeddings textuais, permitindo análises de agrupamento.

### Objetivo

Realizar uma análise arquitetural baseada em:

* embeddings textuais
* clusterização (KMeans)
* redução de dimensionalidade (PCA)

### Resultado

Os clusters identificados correspondem a:

* camada de interface
* lógica de negócio
* gerenciamento de dados
* infraestrutura
* extensões e plugins

Caracterizando uma **Arquitetura em Camadas com Suporte a Plugins**.

---

# Como Rodar

## 1. Instale dependências

```bash
pip install transformers sentence-transformers torch numpy scikit-learn matplotlib
```

## 2. Clone o repositório do JARVIS

```bash
git clone https://github.com/microsoft/JARVIS
```

## 3. Ajuste o caminho no código

```python
caminho = r"C:\Workspace\JARVIS"
```

## 4. Execute o script desejado

```bash
python nome_do_script.py
```

## 5. Para UniXcoder

```python
codigo_1 = """ ... """
codigo_2 = """ ... """
```

## 6. Para MiniLM + Clustering

```bash
python analisar_clusters.py
```

---

# Conclusão Geral do Trabalho

A análise manual indica que o JARVIS utiliza predominantemente a arquitetura **Orquestrador-Executor**, organizada internamente como um pipeline **Pipe-and-Filter**.

As análises feitas pelos modelos de IA apresentaram variações naturais:

* O BART alternou entre Multi-Agent, Layered e Event-Driven, dependendo do idioma, categorias e contexto.
* O UniXcoder identificou padrões robustos de Arquitetura em Camadas.
* O MiniLM apontou uma estrutura em camadas com componentes plugináveis.

Apesar das diferenças, um padrão recorrente apareceu entre os resultados:
o modelo frequentemente associou o projeto a conceitos de **arquitetura multi-agente**, devido ao grande número de “executores”. Porém, essa interpretação não reflete a realidade estrutural do sistema.

Os executores não tomam decisões — apenas respondem quando acionados. Por isso, a classificação correta, após conciliar análise automática e manual, é:

## Arquitetura Orquestrador-Executor com Pipeline Pipe-and-Filter

Esse padrão explica a modularidade, a escalabilidade e a flexibilidade do sistema, além das características semelhantes a camadas e plugins identificadas nas demais abordagens.
