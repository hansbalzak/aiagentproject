import json
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
from agent_work.sandbox import read_file, write_file, list_dir, run_shell

def ensure_venv():
    # Ensure virtual environment is activated
    pass

class SimpleAI:
    def __init__(self, base_url="http://127.0.0.1:8080/v1", model="gpt-3.5-turbo"):
        self.base_url = base_url.rstrip("/")
        self.model = model

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        self.session.mount("http://", HTTPAdapter(max_retries=retries))
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

        # Ensure personality.txt exists
        self.ensure_personality_file()

    def ensure_personality_file(self):
        if not os.path.exists("personality.txt"):
            with open("personality.txt", "w") as f:
                f.write("")

    def load_conversation(self):
        # Load conversation history
        pass

    def load_profile(self):
        with open("profile.json", "r") as f:
            return json.load(f)

    def load_facts(self):
        with open("facts.jsonl", "r") as f:
            return [json.loads(line) for line in f]

    def save_conversation(self):
        # Save conversation history
        pass

    def save_profile(self, profile):
        with open("profile.json", "w") as f:
            json.dump(profile, f, indent=4)

    def save_facts(self, facts):
        with open("facts.jsonl", "w") as f:
            for fact in facts:
                f.write(json.dumps(fact) + "\n")

    def chat(self, user_text: str) -> str:
        # Chat with the user
        pass

    def create_plan(self, user_text: str):
        # Create a plan based on user input
        pass

    def execute_step(self):
        # Execute a step in the plan
        pass

    def check_result(self, result):
        # Check the result of an executed step
        pass

    def clear_conversation(self):
        # Clear the conversation history
        pass

    def help(self):
        # Provide help information
        pass

    def summarize_file(self, file_path: str) -> str:
        # Summarize a file
        pass

    def analyze_code(self):
        # Analyze code
        pass

    def remember_fact(self, fact):
        facts = self.load_facts()
        new_fact = {
            "id": len(facts) + 1,
            "fact": fact,
            "confidence": 1.0,
            "source": "user",
            "timestamp": datetime.now().isoformat()
        }
        facts.append(new_fact)
        self.save_facts(facts)

    def forget_fact(self, fact_id):
        facts = self.load_facts()
        facts = [fact for fact in facts if fact["id"] != fact_id]
        self.save_facts(facts)

    def show_profile(self):
        profile = self.load_profile()
        return json.dumps(profile, indent=4)

    def handle_command(self, command):
        if command.startswith("/remember "):
            fact = command[len("/remember "):]
            self.remember_fact(fact)
            return "Fact remembered."
        elif command.startswith("/forget "):
            fact_id = int(command[len("/forget "):])
            self.forget_fact(fact_id)
            return "Fact forgotten."
        elif command == "/profile":
            return self.show_profile()
        elif command.startswith("/read "):
            file_path = command[len("/read "):]
            return read_file(file_path)
        elif command.startswith("/write "):
            parts = command[len("/write "):].split(" ", 1)
            if len(parts) != 2:
                return "Invalid command format."
            file_path, content = parts
            return write_file(file_path, content)
        elif command.startswith("/list "):
            dir_path = command[len("/list "):]
            return list_dir(dir_path)
        elif command.startswith("/run "):
            parts = command[len("/run "):].split(" ", 1)
            if len(parts) != 2:
                return "Invalid command format."
            command_name, args = parts
            return run_shell(command_name, args.split())
        else:
            return "Unknown command."

def main():
    ai = SimpleAI()
    while True:
        user_input = input("You: ")
        if user_input.startswith("/"):
            response = ai.handle_command(user_input)
        else:
            response = ai.chat(user_input)
        print(f"AI: {response}")
        proceed = input("Proceed? (y/n): ").strip().lower()
        if proceed != 'y':
            break

if __name__ == '__main__':
    main()
