@echo off

:: Запуск серверу
echo Starting server...
start python server.py

:: Чекаємо 5 секунд для ініціалізації серверу
timeout /t 5 /nobreak

:: Запуск бота (якщо він потрібен для тестування)
echo Starting bot...
start python bot.py

:: Запуск кількох нод (наприклад, 5 нод)
for /l %%i in (1,1,5) do (
    echo Starting node %%i...
    start python node.py
    timeout /t 1 /nobreak
)

:: Запуск клієнта (щоб тестувати взаємодію з сервером)
echo Starting client...
start python client.py

:: Чекаємо, поки всі процеси завершаться
pause

