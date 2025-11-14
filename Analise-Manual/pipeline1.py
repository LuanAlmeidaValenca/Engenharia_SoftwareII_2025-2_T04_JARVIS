#Estágio 1: Task Planning
#Arquivo: server/awesome_chat.py
#python# Endpoint /tasks - Retorna apenas o planejamento
@app.route('/tasks', methods=['POST'])
def tasks_endpoint():
    """
    Pipeline Stage 1 - Expõe planejamento para inspeção
    """
    user_input = request.json['messages'][-1]['content']
    
    # Template Method Pattern - Estágio 1
    tasks = parse_task(user_input)
    
    return jsonify(tasks)