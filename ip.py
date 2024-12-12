import socket


def get_local_ip():
    # Створюємо сокет для підключення до будь-якого адреса в Інтернеті
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)

    try:
        # Підключаємось до Google DNS (8.8.8.8) для отримання локальної IP-адреси
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]  # Отримуємо локальну IP-адресу
    except Exception as e:
        local_ip = "Не вдалося визначити IP"
    finally:
        s.close()

    return local_ip


# Викликаємо функцію і виводимо результат
print("Локальна IP-адреса:", get_local_ip())
