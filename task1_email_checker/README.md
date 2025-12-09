# Email Domain Checker — Polza Test Task

Этот простой Python-скрипт проверяет домены email-адресов и выводит один из трёх статусов:

- **домен валиден**
- **домен отсутствует**
- **MX-записи отсутствуют или некорректны**

Скрипт принимает список email-адресов в _любом формате_:

- по одному в строке
- через запятую
- через пробелы
- в смешанном формате

---

## Установка зависимостей

Рекомендуется использовать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
pip install dnspython
```

## Запуск

Создайте текстовый файл с email-адресами, например emails.txt.

Пример содержимого:

test@gmail.com, info@yandex.ru invalid-email
user@nonexistent-domain-12345.com
test@почта.рф

Запустите скрипт:

python check_emails.py emails.txt

## Пример вывода

test@gmail.com — домен валиден
info@yandex.ru — домен валиден
invalid-email — MX-записи отсутствуют или некорректны
user@nonexistent-domain-12345.com — домен отсутствует
test@почта.рф — домен валиден

## Требования

Python 3.8+

Библиотека dnspython
