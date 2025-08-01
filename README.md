# Wikipedia Bot

Бот для поиска информации на русском языке в Википедии с помощью Selenium WebDriver (Firefox).

## Структура проекта

- `main.py` — точка входа, взаимодействие с пользователем
- `browser.py` — настройка и запуск Selenium WebDriver (Firefox)
- `wiki_actions.py` — логика поиска, получения параграфов и ссылок
- `requirements.txt` — зависимости

## Установка

1. Установите Python 3.7+
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. GeckoDriver будет автоматически загружен через webdriver-manager при первом запуске.

## Запуск

```bash
python main.py
```

Следуйте инструкциям в консоли: введите поисковый запрос, бот выведет параграфы и внутренние ссылки с найденной страницы Википедии. Для перехода по внутренним ссылкам следуйте подсказкам в меню.

## Требования
- Python 3.7+
- Firefox
- GeckoDriver (автоматически устанавливается)
- Selenium
- webdriver-manager

## Примечания
- По умолчанию бот работает с русской Википедией.
- Браузер запускается в headless-режиме (без открытия окна браузера). 