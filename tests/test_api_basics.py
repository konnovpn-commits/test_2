import requests
import json

BASE_URL = "https://httpbin.org"

print("\n" + "="*50)
print("НАЧАЛО ТЕСТИРОВАНИЯ API")
print("="*50)

def test_get_request():
    """Тест 1: GET запрос"""
    print("\n🔍 Тест 1: GET запрос")
    print(f"   URL: {BASE_URL}/get")
    
    response = requests.get(f"{BASE_URL}/get")
    
    # Проверка статус кода
    assert response.status_code == 200, f"Ожидался 200, получили {response.status_code}"
    print(f"   ✅ Статус код: {response.status_code} (OK)")
    
    # Проверка структуры ответа
    data = response.json()
    assert "url" in data, "В ответе нет поля 'url'"
    assert data["url"] == f"{BASE_URL}/get", f"URL не совпадает: {data['url']}"
    print(f"   ✅ URL верный: {data['url']}")
    
    # Проверка наличия стандартных полей
    assert "args" in data, "Нет поля 'args' для параметров"
    assert "headers" in data, "Нет поля 'headers'"
    assert "origin" in data, "Нет поля 'origin'"
    
    print("   🎉 Тест 1 пройден успешно!")

def test_get_with_params():
    """Тест 2: GET запрос с параметрами"""
    print("\n🔍 Тест 2: GET с параметрами")
    
    params = {
        "page": 1,
        "limit": 10,
        "search": "python testing"
    }
    
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    
    data = response.json()
    
    # ВАЖНО: httpbin возвращает ВСЕ параметры как строки
    # Преобразуем наши параметры в строки для сравнения
    expected_params = {k: str(v) for k, v in params.items()}
    
    # Проверяем, что параметры вернулись (как строки)
    assert data["args"] == expected_params, \
        f"Параметры не совпадают. Ожидалось: {expected_params}, Получено: {data['args']}"
    
    print(f"   ✅ Параметры переданы: {params}")
    print(f"   ✅ Параметры получены (как строки): {data['args']}")
    print("   🎉 Тест 2 пройден успешно!")

def test_post_request():
    """Тест 3: POST запрос с JSON данными"""
    print("\n🔍 Тест 3: POST запрос (создание данных)")
    
    # Данные для отправки
    new_data = {
        "name": "Алексей",
        "role": "Тестировщик",
        "skills": ["Python", "API Testing", "Pytest"],
        "experience_years": 1
    }
    
    print(f"   Отправляемые данные: {json.dumps(new_data, ensure_ascii=False)}")
    
    response = requests.post(f"{BASE_URL}/post", json=new_data)
    assert response.status_code == 200
    
    data = response.json()
    
    # Проверяем, что данные вернулись
    assert "json" in data, "Нет поля 'json' в ответе"
    assert data["json"] == new_data, "Отправленные и полученные данные не совпадают"
    
    print(f"   ✅ Данные отправлены и получены обратно")
    print(f"   ✅ ID запроса: {data.get('id', 'N/A')}")
    print("   🎉 Тест 3 пройден успешно!")

def test_post_form_data():
    """Тест 4: POST запрос с form-data"""
    print("\n🔍 Тест 4: POST с form-data (как HTML формы)")
    
    form_data = {
        "username": "test_user",
        "password": "test_pass_123",
        "remember_me": "true"
    }
    
    response = requests.post(f"{BASE_URL}/post", data=form_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "form" in data
    assert data["form"] == form_data
    
    print(f"   ✅ Form-data отправлено: {form_data}")
    print("   🎉 Тест 4 пройден успешно!")

def test_put_request():
    """Тест 5: PUT запрос (обновление)"""
    print("\n🔍 Тест 5: PUT запрос (обновление данных)")
    
    update_data = {
        "status": "updated",
        "version": "2.0",
        "changes": ["bug fixes", "performance improvements"]
    }
    
    response = requests.put(f"{BASE_URL}/put", json=update_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["json"] == update_data
    
    print(f"   ✅ Данные обновлены: {update_data}")
    print("   🎉 Тест 5 пройден успешно!")

def test_delete_request():
    """Тест 6: DELETE запрос"""
    print("\n🔍 Тест 6: DELETE запрос (удаление)")
    
    response = requests.delete(f"{BASE_URL}/delete")
    assert response.status_code == 200
    
    data = response.json()
    assert "url" in data
    
    print(f"   ✅ DELETE запрос выполнен: {data['url']}")
    print("   🎉 Тест 6 пройден успешно!")

def test_status_codes():
    """Тест 7: Проверка разных статус кодов"""
    print("\n🔍 Тест 7: Проверка статус кодов")
    
    test_cases = [
        (200, "OK - успешный запрос"),
        (404, "Not Found - страница не найдена"),
        (500, "Internal Server Error - ошибка сервера"),
        (403, "Forbidden - доступ запрещен"),
        (201, "Created - ресурс создан")
    ]
    
    for status_code, description in test_cases:
        print(f"\n   Проверка статуса {status_code}: {description}")
        response = requests.get(f"{BASE_URL}/status/{status_code}")
        
        # Для некоторых статусов httpbin может возвращать 200 с информацией
        # Проверим, что получили то, что запросили
        if status_code in [404, 500, 403]:
            # Для этих статусов httpbin возвращает их как есть
            assert response.status_code == status_code, \
                f"Ожидался {status_code}, получили {response.status_code}"
        else:
            # Для 200 и 201 httpbin может возвращать 200
            assert response.status_code in [200, status_code]
        
        print(f"      ✅ Статус {status_code} обработан")

def test_response_headers():
    """Тест 8: Проверка заголовков"""
    print("\n🔍 Тест 8: Кастомные заголовки")
    
    # Используем заголовки, которые точно поддерживаются httpbin
    custom_headers = {
        "X-Custom-Header": "test-value-123",
        "User-Agent": "Python-API-Tester/1.0",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest"  # Часто используется в веб-приложениях
    }
    
    response = requests.get(f"{BASE_URL}/headers", headers=custom_headers)
    assert response.status_code == 200
    
    data = response.json()
    headers_received = data["headers"]
    
    print(f"   📨 Отправленные заголовки: {custom_headers}")
    print(f"   📥 Все полученные заголовки:")
    
    # Выведем все заголовки для анализа
    for key, value in headers_received.items():
        if any(prefix in key.lower() for prefix in ['x-', 'user', 'accept']):
            print(f"      {key}: {value}")
    
    # Проверяем User-Agent
    assert headers_received.get("User-Agent") == custom_headers["User-Agent"], \
        f"User-Agent не совпадает: {headers_received.get('User-Agent')}"
    print("   ✅ User-Agent корректный")
    
    # Проверяем Accept
    assert headers_received.get("Accept") == custom_headers["Accept"], \
        f"Accept не совпадает: {headers_received.get('Accept')}"
    print("   ✅ Accept корректный")
    
    # Проверяем X-Custom-Header (может быть в нижнем регистре)
    x_custom_value = None
    for header_name in headers_received:
        if header_name.lower() == "x-custom-header":
            x_custom_value = headers_received[header_name]
            break
    
    assert x_custom_value == custom_headers["X-Custom-Header"], \
        f"X-Custom-Header не найден или не совпадает"
    print(f"   ✅ X-Custom-Header найден: {x_custom_value}")
    
    print("   🎉 Тест 8 пройден успешно!")

def test_basic_auth():
    """Тест 9: Базовая аутентификация"""
    print("\n🔍 Тест 9: Базовая аутентификация")
    
    username = "testuser"
    password = "testpass"
    
    # Позитивный тест - правильные credentials
    response = requests.get(
        f"{BASE_URL}/basic-auth/{username}/{password}",
        auth=(username, password)
    )
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] == True
    print("   ✅ Аутентификация с правильными данными успешна")
    
    # Негативный тест - неправильные credentials
    response = requests.get(
        f"{BASE_URL}/basic-auth/{username}/{password}",
        auth=(username, "wrong_password")
    )
    assert response.status_code == 401  # Unauthorized
    print("   ✅ Аутентификация с неправильными данными отклонена")
    
    print("   🎉 Тест 9 пройден успешно!")

def test_delay():
    """Тест 10: Задержка ответа"""
    print("\n🔍 Тест 10: Запрос с задержкой")
    
    print("   Отправляем запрос с задержкой 2 секунды...")
    response = requests.get(f"{BASE_URL}/delay/2", timeout=5)
    
    assert response.status_code == 200
    print("   ✅ Запрос с задержкой выполнен успешно")
    print("   🎉 Тест 10 пройден успешно!")

# Запуск всех тестов
if __name__ == "__main__":
    tests = [
        test_get_request,
        test_get_with_params,
        test_post_request,
        test_post_form_data,
        test_put_request,
        test_delete_request,
        test_status_codes,
        test_response_headers,
        test_basic_auth,
        test_delay
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            failed += 1
            print(f"\n❌ Тест '{test.__name__}' упал: {e}")
        except Exception as e:
            failed += 1
            print(f"\n⚠️  Тест '{test.__name__}' упал с ошибкой: {e}")
    
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ")
    print("="*50)
    print(f"Всего тестов: {len(tests)}")
    print(f"Пройдено: {passed}")
    print(f"Упало: {failed}")
    
    if failed == 0:
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print(f"\n⚠️  {failed} тестов не прошли")
    
    print("="*50)