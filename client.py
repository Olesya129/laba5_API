import requests

TOKEN = 123  # токен
BASE_URL = "http://127.0.0.1:8000"  # Адрес API

# Проверка наличия токена
if not TOKEN:
    print("API_TOKEN не найден в переменных окружения!")
    exit(1)

# Функция для добавления токена в заголовки запроса
def get_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",  # Добавление токена в заголовки для авторизации
        "Content-Type": "application/json",  # Установка типа контента
    }

# Функция для создания заметки
def create_note():
    text = input("Введите текст новой заметки: ")
    try:
        response = requests.post(
            f"{BASE_URL}/notes/",  # Адрес для создания заметки
            headers=get_headers(),  # Заголовки с токеном
            json={"text": text},  # Отправка текста заметки
        )
        response.raise_for_status()  # Проверка на ошибки
        note_data = response.json()  # Преобразование ответа в JSON
        print(f"Заметка создана! ID: {note_data['id']}")  # Вывод ID созданной заметки
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при создании заметки: {e}")  # Обработка ошибок

# Функция для получения всех заметок
def list_notes():
    try:
        response = requests.get(f"{BASE_URL}/notes", headers=get_headers())  # GET Запрос списка заметок
        response.raise_for_status()  # Проверка на ошибки
        notes = response.json()  # Преобразование ответа в JSON
        print("Ответ от сервера:", notes)  # Вывод ответа для отладки
        if isinstance(notes, dict):  # Если ответ — словарь (например, ID заметок)
            notes = list(notes.values())  # Извлекаем значения из словаря
        if notes:
            print("Список заметок:")
            for note_id in notes:  # Перебор всех ID заметок
                print(f"ID: {note_id}")  # Вывод ID заметки
        else:
            print("Список заметок пуст.")  # Если нет заметок
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении списка заметок: {e}")  # Обработка ошибок

# Функция для получения заметки по ID
def get_note():
    note_id = input("Введите ID заметки: ")  # Запрос ID заметки
    try:
        response = requests.get(f"{BASE_URL}/notes/{note_id}", headers=get_headers())  # GET Запрос по ID
        response.raise_for_status()  # Проверка на ошибки
        note = response.json()  # Преобразование ответа в JSON
        # Вывод информации о заметке
        print(f"Заметка найдена:\nID: {note['id']}, Текст: {note['text']}, Создано: {note['created_at']}, Обновлено: {note['updated_at']}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении заметки: {e}")  # Обработка ошибок

# Функция для обновления заметки
def update_note():
    note_id = input("Введите ID заметки для обновления: ")  # Запрос ID заметки
    new_text = input("Введите новый текст заметки: ")  # Запрос нового текста
    try:
        response = requests.patch(
            f"{BASE_URL}/notes/{note_id}",  # Адрес для обновления заметки по ID
            json={"text": new_text},  # Отправка нового текста
            headers=get_headers(),  # Заголовки с токеном
        )
        response.raise_for_status()  # Проверка на ошибки
        print("Заметка успешно обновлена.")  # Успешное обновление
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при обновлении заметки: {e}")  # Обработка ошибок

# Функция для удаления заметки
def delete_note():
    note_id = input("Введите ID заметки для удаления: ")  # Запрос ID заметки
    try:
        response = requests.delete(f"{BASE_URL}/notes/{note_id}", headers=get_headers())  # Запрос на удаление
        response.raise_for_status()  # Проверка на ошибки
        print("Заметка успешно удалена.")  # Успешное удаление
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при удалении заметки: {e}")  # Обработка ошибок

# Основное меню программы
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Создать заметку")
        print("2. Вывести список заметок")
        print("3. Получить заметку по ID")
        print("4. Обновить заметку")
        print("5. Удалить заметку")
        print("6. Выйти")

        choice = input("Введите номер действия: ")  # Запрос действия
        if choice == "1":
            create_note()  # Вызов функции создания заметки
        elif choice == "2":
            list_notes()  # Вызов функции списка заметок
        elif choice == "3":
            get_note()  # Вызов функции получения заметки по ID
        elif choice == "4":
            update_note()  # Вызов функции обновления заметки
        elif choice == "5":
            delete_note()  # Вызов функции удаления заметки
        elif choice == "6":
            print("Выход из программы.")  # Выход из программы
            break  # Завершение цикла
        else:
            print("Некорректный выбор. Попробуйте снова.")  # Если выбор некорректен

# Запуск программы
if __name__ == "__main__":
    main()
