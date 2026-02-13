import requests

class LlamaAgent:
    def __init__(self, url):
        self.url = url

    def query(self, prompt):
        response = requests.post(self.url, json={"prompt": prompt})
        return response.json().get("result", "")

    def handle_command(self, command):
        if command == "hello":
            return self.query("hello")
        elif command == "how are you?":
            return self.query("how are you?")
        elif command == "goodbye":
            return self.query("goodbye")
        else:
            return "Unknown command"
