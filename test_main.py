from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.content.decode() == """
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
            <h2>Это ИИ приложение для курса 'Программная инженерия'</h2>
            <h3><i>Данное приложение предназначено для определения ключевых фраз в научных текстах<h3><i>
        </main>
    </body>
    </html>
    """
