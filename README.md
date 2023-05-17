# Приложение для определения ключевых фраз в научных текстах
Приложение определяет ключевые фразы в научных текстах текста с помощью библиотеки Hugging Face. Приложение разработано на базе модели ml6team/keyphrase-extraction-kbir-inspec использующей KBIR в качестве базовой модели и обученной на наборе данных Inspec.

Для создания серверной части приложения использовался фреймворк FastAPI. В качестве  пользовательского клиента рекомендуется использовать Postman.

# Инструкция по запуску приложения

1.	В командной строке активируем виртуальное окружение: 
путь до Вашей папки с приложением/.ml-venv/Scripts/activate.bat
2.	Убедитесь, что на вашей машине имеются все необходимые библиотеки, включая Python 3.10.8. Для этого смотрим список в requirements.txt. Чтобы установить библиотеки, необходимые для работы приложения в командной строке пишем: 
pip install requirements.txt
3.	Запускаем в командной строке веб-сервер uvicorn, используемый для запуска приложения: 
uvicorn main:app --reload 
4.	Устанавливаем (https://www.postman.com/downloads/) и открываем Postman. Выбираем метод GET, в поле метода вставляем адрес сервера http://127.0.0.1:8000/, нажимаем кнопку Send.В поле ответа должны получить данные с информационной страницы, а также статус успешного обращения на сервер «Status: 200 OK».
5.	Для работы с приложением в Postman выбираем метод POST, формат отправляемых данных raw: json. В поле метода добавляем адрес: http://127.0.0.1:8000/predict. В окне ввода вставляем отрывок научного текста на английском языке в формате:
{
"text": " Отрывок научного текста на английском языке"
}
6. В поле ответа должны получить список ключевых фраз. 
