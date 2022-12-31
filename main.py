import fastapi
import marked
import openai
import uvicorn
from fastapi import Request, Response
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

app = fastapi.FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def parse_markdown(text):
    return marked.markup_to_markdown(text)


def remove_quotes(text):
    return text.replace('"', '')


def replace_newlines(text):
    return text.replace('\n', '<br>')


@app.get("/interface")
def interface(prompt: str, max_tokens: int, model: str = "davinci"):
    openai.api_key = ""
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return replace_newlines(remove_quotes(parse_markdown(response.choices[0].text)))


@app.get("/")
def chat(request: Request, response: Response):
    return templates.TemplateResponse("template.html", {
        "request": request
    })


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
