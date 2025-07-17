from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class WikiBrowser:
    """
    Класс для управления браузером Selenium Firefox в headless-режиме.
    Инкапсулирует запуск, переход по URL и завершение работы браузера.
    """
    def __init__(self):
        """
        Инициализирует headless-браузер Firefox с помощью webdriver-manager.
        """
        options = Options()
        options.add_argument("--headless")
        service = Service(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)

    def get(self, url):
        """
        Открывает указанный URL в браузере.
        
        Args:
            url (str): Ссылка для перехода.
        """
        self.driver.get(url)

    def quit(self):
        """
        Завершает работу браузера и освобождает ресурсы.
        """
        self.driver.quit()