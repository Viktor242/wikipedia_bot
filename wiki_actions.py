# Основные действия с Википедией
from selenium.webdriver.common.by import By

class WikipediaPage:
    """
    Класс для работы с одной статьёй Википедии через Selenium.
    Позволяет открывать статью, получать параграфы и внутренние ссылки.
    """
    def __init__(self, browser, title, lang="ru"):
        """
        Инициализирует страницу Википедии и открывает её в браузере.
        
        Args:
            browser (WikiBrowser): Экземпляр браузера для управления страницей.
            title (str): Название статьи (в URL-формате).
            lang (str): Язык Википедии (по умолчанию 'ru').
        """
        self.browser = browser
        self.title = title
        self.lang = lang
        self.open()

    def open(self):
        """
        Открывает статью Википедии по заданному названию и языку.
        """
        url = f"https://{self.lang}.wikipedia.org/wiki/{self.title}"
        self.browser.get(url)

    def get_paragraphs(self):
        """
        Возвращает список параграфов из основного текста статьи.
        
        Returns:
            list[str]: Список непустых параграфов статьи.
        """
        paragraphs = []
        for p in self.browser.driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output > p"):
            text = p.text.strip()
            if text:
                paragraphs.append(text)
        return paragraphs

    def get_internal_links(self, limit=5):
        """
        Возвращает список первых уникальных внутренних ссылок (текст, href) из основного контента.
        
        Args:
            limit (int): Максимальное количество ссылок (по умолчанию 5).
        Returns:
            list[tuple[str, str]]: Список кортежей (текст, ссылка).
        """
        links = []
        seen = set()
        for a in self.browser.driver.find_elements(By.CSS_SELECTOR, "div.mw-parser-output a"):
            href = a.get_attribute("href")
            text = a.text.strip()
            if (
                href
                and "/wiki/" in href
                and not ":" in href.split("/wiki/")[1]
                and href not in seen
                and text
            ):
                links.append((text, href))
                seen.add(href)
            if len(links) >= limit:
                break
        return links
