![screenshot](https://i.imgur.com/ghYxrOO.png)

### Check out [how to deploy this project](deployment.md).

## Project Description

This project is a FastAPI app that exposes an interface route where users can talk to the OpenAI GPT-3 language model using the OpenAI API. The app also includes a HTML interface with a chatbox for interacting with GPT-3.

## Getting Started

1.  Clone the repository:

`git clone https://github.com/[username]/gpt3-fastapi-app.git` 

2.  Navigate to the project directory:

`cd gpt3-fastapi-app` 

3.  Install the required packages:

`pip install -r requirements.txt` 

4.  Start the app:

`uvicorn main:app --reload` 

5.  Open the app in your web browser at [http://localhost:8000](http://localhost:8000).

## Usage

To use the app, enter a prompt in the input field and click the "Submit" button. The app will use the OpenAI GPT-3 language model to generate a response, which will be displayed in the chatbox. You can adjust the value of the `max_tokens` parameter by entering a value in the `max_tokens` input field.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://chat.openai.com/chat/LICENSE).

## Acknowledgements

-   [OpenAI](https://openai.com/) for providing the GPT-3 language model.
-   [FastAPI](https://fastapi.tiangolo.com/) for the web framework.
-   [marked](https://marked.js.org/) for Markdown parsing.
