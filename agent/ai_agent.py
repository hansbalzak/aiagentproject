from agent.llama_agent import LlamaAgent

class AIAgent:
    def __init__(self, llama_url):
        self.llama_agent = LlamaAgent(llama_url)

    def run(self):
        while True:
            command = input("Enter command (or 'exit' to quit): ")
            if command == "exit":
                break
            response = self.llama_agent.handle_command(command)
            print(f"Response: {response}")

if __name__ == "__main__":
    ai_agent = AIAgent("http://127.0.0.1:8080/v1")
    ai_agent.run()
