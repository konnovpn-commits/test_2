# API Testing Project with Python

Проект для автоматизации тестирования REST API с использованием Python, requests и pytest.

## Результаты
- ✅ 100% тестов проходят успешно
- ✅ 10 различных тестовых сценариев
- ✅ Тестирование всех основных HTTP методов
- ✅ Проверка статус кодов и обработки ошибок

## Навыки, продемонстрированные в проекте
- Автоматизация тестирования REST API
- Работа с HTTP методами (GET, POST, PUT, DELETE)
- Проверка статус кодов ответов (200, 404, 500, 401 и др.)
- Отправка параметров и заголовков
- Тестирование аутентификации (Basic Auth)
- Обработка JSON данных
- Использование pytest для организации тестов

## Технологии
- **Python 3.14**
- **requests** - для отправки HTTP запросов
- **pytest** - фреймворк для тестирования
- **httpbin.org** - тестовое API

## Структура проекта
test_2-main/  
├── tests/  
│ ├── test_api_basics.py # Основные тесты API (10 тестов)  
│ └── init.py  
├── setup.bat # Скрипт установки для Windows  
├── run_tests.bat # Скрипт запуска тестов  
├── requirements.txt # Зависимости проекта  
├── .gitignore # Игнорируемые файлы  
└── README.md # Документация  


## Быстрый старт для Windows

### Способ 1: Использовать готовые скрипты (рекомендуется)

1. **Скачайте проект** с GitHub
2. **Запустите `setup.bat`** - установит зависимости
3. **Запустите `run_tests.bat`** - запустит все тесты

### Способ 2: Ручная установка

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ваш-username/api-testing-project.git
cd test_2-main

# 2. Установить зависимости (выберите один вариант):

# Вариант A: Используйте py вместо python
py -m pip install requests pytest

# Вариант B: Установите virtualenv если venv не работает
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install requests pytest

# 3. Запустить тесты
python tests/test_api_basics.py
# или
pytest tests/ -v

# Содержимое скриптов
setup.bat
batch
@echo off
echo Установка зависимостей для проекта API тестирования...
echo.

echo Установка requests и pytest...
py -m pip install requests pytest

echo.
echo Установка завершена!
echo Для запуска тестов выполните: run_tests.bat
pause
run_tests.bat
batch
@echo off
echo Запуск тестов API...
echo.

echo 1. Запуск основных тестов с подробным выводом...
python tests/test_api_basics.py

echo.
echo 2. Запуск через pytest с подробным отчетом...
pytest tests/ -v

echo.
echo Тестирование завершено!
pause
```

## Что тестируется
1. Базовые HTTP методы
✅ GET запросы с проверкой ответа

✅ POST запросы с JSON данными

✅ PUT запросы для обновления

✅ DELETE запросы для удаления

2. Параметры и данные
✅ Передача query-параметров в URL

✅ Отправка JSON в теле запроса

✅ Проверка структуры ответа

3. Статус коды и ошибки
✅ Успешные ответы (200, 201)

✅ Ошибки клиента (404, 400)

✅ Ошибки сервера (500)

✅ Аутентификация (401)

4. Заголовки
✅ Кастомные заголовки запросов

✅ Анализ заголовков ответа
