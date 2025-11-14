#Estágio 2: Model Selection
#python# Linhas ~400-500
def select_models(tasks):
    
    #Pipeline Stage 2 - Seleção de modelos via LLM
    
    selected_models = {}
    
    for task in tasks:
        # 1. Query HuggingFace Hub por tipo de tarefa
        candidates = query_huggingface_hub(task['task'])
        
        # 2. Ordenar por popularidade (downloads)
        candidates.sort(key=lambda x: x['downloads'], reverse=True)
        
        # 3. Top-K filtering
        top_k_models = candidates[:10]
        
        # 4. LLM seleciona o melhor modelo
        prompt = f"""
        #2 Model Selection Stage - Select a suitable model
        Task: {task}
        Candidate Models: {json.dumps(top_k_models)}
