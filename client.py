import os
import requests
from dotenv import load_dotenv

# Загрузить переменные окружения из .env файла
load_dotenv()

TOKEN = os.getenv("TOKEN")
BASE_URL = "http://127.0.0.1:8000"  # Адрес API

# Проверка наличия токена
if not TOKEN:
    print("API_TOKEN не установлен!")
    exit(1)

# Функция для добавления токена в заголовки
def get_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }

# Функция для создания заметки
def create_note(text: str) -> int:
    """
    Создает новую заметку и возвращает её ID.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/notes/",
            headers=get_headers(),
            json={"text": text},
        )
        response.raise_for_status()  # Проверяем наличие HTTP ошибок
        note_data = response.json()  # Получаем тело ответа в формате JSON
        print("Прошёл запрос:", note_data)
        return note_data["id"]  # Извлекаем и возвращаем ID заметки
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании заметки: {response.status_code} - {response.text}")
        raise e

# Функция для получения заметки по ID
def get_note(note_id):
    url = f"{BASE_URL}/notes/{note_id}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        print("Заметка найдена:")
        print(response.json())
    else:
        print(f"Ошибка при получении заметки: {response.status_code} - {response.text}")

# Пример использования
if __name__ == "__main__":
    # Создание заметки
    note_id = create_note("Первая заметка через API")
    get_note(note_id)