@echo off
echo ========================================
echo ЗАПУСК ТЕСТОВ API
echo ========================================
echo.

echo 1. Проверка зависимостей...
pip list | findstr "requests pytest"

echo.
echo 2. Запуск основных тестов...
python tests/test_api_basics.py

echo.
echo 3. Запуск через pytest...
pytest tests/ -v

echo.
echo ========================================
echo ТЕСТИРОВАНИЕ ЗАВЕРШЕНО
echo ========================================
pause