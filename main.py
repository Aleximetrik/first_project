print('Hello from repository!')

import os
from dotenv import load_dotenv

def print_author():
    # Загружаем переменные из .env в окружение
    load_dotenv()
    # Читаем значение переменной AUTHOR
    author = os.getenv("AUTHOR")
    # Выводим результат
    print(f"Автор проекта: {author}")

if __name__ == "__main__":
    print_author()