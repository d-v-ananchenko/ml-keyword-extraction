from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from extraction import KeyphraseExtractionPipeline


class Item(BaseModel):
    text: str


app = FastAPI()
model_name = "ml6team/keyphrase-extraction-kbir-inspec"
extractor = KeyphraseExtractionPipeline(model=model_name)


@app.get("/")
def root():
    html_page = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Учебный проект</title>
    </head>
    <body>
        <main>
            <h2>Это ИИ приложение для курса 'Программная 
            инженерия'</h2>
            <h3><i>Данное приложение предназначено для определения ключевых фраз в научных текстах<h3><i>  
        </main>
    </body>
    </html>
    """
    return HTMLResponse(content=html_page, status_code=200)


@app.post("/predict/")
def predict(item: Item):
    keyphrases = list(extractor(item.text))
    return {"keyphrases": keyphrases}
