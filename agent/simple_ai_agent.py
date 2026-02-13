import requests

class SimpleAI:
    def __init__(self, url="http://127.0.0.1:8080/api/v1"):
        if not url.endswith("/"):
            url += "/"
        self.url = url

    def send_command(self, command):
        headers = {"Content-Type": "application/json"}
        data = {"command": command}
        response = requests.post(self.url, headers=headers, json=data)
        print(f"Request URL: {self.url}")
        print(f"Request Headers: {headers}")
        print(f"Request Data: {data}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Content: {response.content}")
        if response.status_code != 200:
            print(f"Error: {response.json().get('error', 'Unknown error')}")
        return response.json().get("response", "No response")

    def hello(self):
        print(self.send_command("hello"))

    def how_are_you(self):
        print(self.send_command("how are you?"))

    def goodbye(self):
        print(self.send_command("goodbye"))

if __name__ == "__main__":
    ai = SimpleAI("http://127.0.0.1:8080")
    ai.hello()
    ai.how_are_you()
    ai.goodbye()
