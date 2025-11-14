#Estágio 4: Response Generation
#python# Endpoint /hugginggpt - Serviço completo com resposta final
def generate_response(user_input, tasks, models, results):
    
    #Stage 4 - Agregação de resultados via LLM
    
    prompt = f"""
    #4 Response Generation Stage - Describe the process and results.
    User Input: {user_input}
    Task Planning: {json.dumps(tasks)}
    Model Selection: {json.dumps(models)}
    Task Execution: {json.dumps(results)}
    
    Describe in first person. Include file paths for generated content.
    """
    
    return send_request_to_openai(prompt)