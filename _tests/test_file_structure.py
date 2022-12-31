import requests

# Set the file structure
response = requests.post("http://localhost:8000/set-file-structure", data={"file_structure": "File structure goes here"})

# Ask the model a question
response = requests.post("http://localhost:8000/ask-question", data={"question": "What is the capital of France?"})
print(response.text)