from flask import Flask

# Ініціалізація Flask-додатку
app = Flask(__name__)

# Головний маршрут для кореневої сторінки
@app.route('/')
def home():
    return 'Hello, World!'  # Ви можете повернути будь-яке повідомлення або HTML

# Маршрут для favicon.ico
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Повертає порожній 204 статус для запиту favicon

# Запуск серверу
if __name__ == '__main__':
    app.run(debug=True)  # Запускає сервер у режимі налагодження на порту 5000
