import os
import subprocess

ALLOWED_COMMANDS = {
    "ls": ["ls"],
    "cat": ["cat"],
    "grep": ["grep"],
    "find": ["find"],
    "head": ["head"],
    "tail": ["tail"]
}

def read_file(file_path):
    if not os.path.exists(file_path):
        return "File does not exist."
    with open(file_path, "r") as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)
    return "File written successfully."

def list_dir(dir_path="."):
    if not os.path.exists(dir_path):
        return "Directory does not exist."
    return "\n".join(os.listdir(dir_path))

def run_shell(command, args):
    if command not in ALLOWED_COMMANDS:
        return "Command not allowed."
    full_command = [command] + args
    try:
        result = subprocess.run(full_command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr
