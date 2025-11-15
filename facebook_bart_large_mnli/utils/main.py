import os

class Utils:

    @classmethod
    def coletar_estrutura_projeto(cls, base_path, max_entries=None, ignore_files=False):
        """
        Percorre recursivamente o projeto e retorna uma string com a estrutura de arquivos e pastas.
        Exemplo:
        src/
        controller/
            main_controller.py
        model/
            user_model.py
        public/
        index.html
        """


        ignorar_pastas = {".git", "__pycache__", "node_modules", "venv", "env", ".idea", ".vscode"} if ignore_files else ...

        base_path = os.path.abspath(base_path)
        estrutura = []
        for root, dirs, files in os.walk(base_path):
            if ignore_files:
                if any(ignorar in root for ignorar in ignorar_pastas):
                    continue
            rel_path = os.path.relpath(root, base_path)
            if rel_path == ".":
                rel_path = os.path.basename(base_path)
            estrutura.append(rel_path.replace("\\", "/") + "/")
            for f in files:
                estrutura.append(f"  {rel_path.replace('\\', '/')}/{f}")
            if max_entries and len(estrutura) > max_entries:
                estrutura.append("  ... (estrutura truncada)")
                break

        texto_estrutura = "\n".join(estrutura)
        return texto_estrutura, len(estrutura)
    
    @classmethod
    def contexto_arquiteturas(cls):
        return """
            Software Architectural Patterns Overview:

            1. Layered Architecture (Layers):
            - Organizes the system into layers (e.g., presentation, business, data).
            - Each layer has a specific responsibility.
            - Promotes maintainability, modularity, and separation of concerns.

            2. Model-View-Controller (MVC):
            - Divides the system into Model (data), View (user interface), and Controller (logic).
            - Common in web frameworks like Laravel, Django, and Spring.
            - Encourages clear separation between business logic and UI.

            3. Microservices Architecture:
            - System composed of independent services communicating through APIs.
            - Promotes scalability, fault isolation, and technology diversity.
            - Common in cloud-native applications (e.g., Netflix, Uber).

            4. Pipe-and-Filter Architecture:
            - Data flows through a series of filters connected by pipes.
            - Each filter transforms data and passes it along.
            - Common in data processing and streaming pipelines.

            5. Event-Driven Architecture:
            - Components communicate through events.
            - Promotes loose coupling and real-time responsiveness.
            - Used in message brokers and reactive systems.

            6. Monolithic Architecture:
            - Single unified codebase for the entire application.
            - Easier to develop and deploy initially.
            - Can lead to scalability and maintainability challenges as the system grows.

            7. Orchestrator-Executor Architecture:
            - Separates decision-making (orchestrator) from task execution (executor).
            - Common in workflow management and automation systems.

            8. Multi-Agent Architecture:
            - System composed of autonomous agents that interact.
            - Promotes distributed problem-solving and adaptability.
            - Used in simulations, robotics, and AI systems.
        """