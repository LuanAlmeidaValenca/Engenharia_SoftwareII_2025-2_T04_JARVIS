#Estágio 3: Task Execution
#python# Endpoint /results - Retorna planejamento + execução
def execute_tasks(tasks, models):
    
    #Gerenciamento de dependências e execução paralela/sequencial
    
    results = {}
    
    # Separar tarefas independentes e dependentes
    independent_tasks = [t for t in tasks if t['dep'] == [-1]]
    dependent_tasks = [t for t in tasks if t['dep'] != [-1]]
    
    # Execução paralela de tarefas independentes
    with ThreadPoolExecutor() as executor:
        futures = []
        for task in independent_tasks:
            future = executor.submit(
                execute_single_task, 
                task, 
                models[task['id']]
            )
            futures.append((task['id'], future))
        
        for task_id, future in futures:
            results[task_id] = future.result()
    
    # Execução sequencial de tarefas dependentes
    for task in dependent_tasks:
        # Substituir placeholders <GENERATED>-X
        for dep_id in task['dep']:
            placeholder = f"<GENERATED>-{dep_id}"
            if placeholder in str(task['args']):
                task['args'] = replace_placeholder(
                    task['args'], 
                    placeholder, 
                    results[dep_id]
                )
        
        results[task['id']] = execute_single_task(
            task, models[task['id']])