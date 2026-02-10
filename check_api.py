import requests
import json

print("=== Проверка доступности API ===\n")

urls_to_test = [
    "https://reqres.in/api/users/2",
    "https://reqres.in/",
    "http://httpbin.org/get"  # альтернативное API для проверки
]

for url in urls_to_test:
    print(f"Тестируем: {url}")
    try:
        response = requests.get(url, timeout=10)
        print(f"  Статус: {response.status_code}")
        print(f"  Ответ: {response.text[:200]}...")  # первые 200 символов
    except Exception as e:
        print(f"  Ошибка: {e}")
    print()