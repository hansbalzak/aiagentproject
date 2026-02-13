import json
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime
from agent_work.sandbox import read_file, write_file, list_dir, run_shell
import re
from collections import defaultdict

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

        self.plan = []
        self.current_step = 0
        self.loop_detected = False
        self.index = self.load_index()

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
        self.plan = [
            "Step 1: Understand the user's request.",
            "Step 2: Generate a plan with up to 6 bullets.",
            "Step 3: Execute one step of the plan.",
            "Step 4: Check the result of the executed step.",
            "Step 5: Detect loops.",
            "Step 6: Stop when the plan is complete."
        ]
        self.current_step = 0
        self.loop_detected = False
        return "Plan created."

    def execute_step(self):
        if self.current_step >= len(self.plan):
            return "Plan execution complete."
        step = self.plan[self.current_step]
        self.current_step += 1
        return f"Executing step: {step}"

    def check_result(self, result):
        if "loop detected" in result.lower():
            self.loop_detected = True
            return "Loop detected. Stopping execution."
        return "Result checked."

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

    def load_index(self):
        index = defaultdict(list)
        for root, _, files in os.walk("."):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                    for i, line in enumerate(content.splitlines()):
                        index[line].append((file_path, i + 1))
        return index

    def search_repo(self, keyword):
        results = []
        for line, locations in self.index.items():
            if re.search(r"\b" + re.escape(keyword) + r"\b", line, re.IGNORECASE):
                for file_path, line_number in locations:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                        context = lines[max(0, line_number - 3):min(len(lines), line_number + 3)]
                        context = "".join(context).strip()
                    results.append((file_path, line_number, context))
        return results

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
        elif command == "/create_plan":
            return self.create_plan("")
        elif command == "/execute_step":
            return self.execute_step()
        elif command == "/check_result":
            return self.check_result("")
        elif command.startswith("/askrepo "):
            keyword = command[len("/askrepo "):]
            results = self.search_repo(keyword)
            if not results:
                return "No results found."
            response = "Relevant snippets:\n"
            for file_path, line_number, context in results:
                response += f"File: {file_path}, Line: {line_number}\nContext: {context}\n\n"
            return response
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
