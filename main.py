# Точка входа, реализует логику взаимодействия с пользователем
from browser import WikiBrowser
from wiki_actions import WikipediaPage
from urllib.parse import unquote

class WikipediaBot:
    """
    Класс-бот для интерактивной работы с Википедией через Selenium.
    Управляет циклом взаимодействия с пользователем и навигацией по статьям.
    """
    def __init__(self):
        """
        Инициализирует бота и браузер, задаёт язык Википедии.
        """
        self.browser = WikiBrowser()
        self.lang = "ru"

    def run(self):
        """
        Запускает основной цикл работы бота: запрашивает у пользователя статью и запускает меню навигации.
        """
        try:
            while True:
                query = input("Введите запрос для поиска на Википедии: ")
                page = WikipediaPage(self.browser, query.replace(" ", "_"), self.lang)
                self.article_menu(page)
        finally:
            self.browser.quit()

    def article_menu(self, page):
        """
        Меню навигации по статье: просмотр параграфов, переход по внутренним ссылкам, выход.
        
        Args:
            page (WikipediaPage): Текущая открытая страница Википедии.
        """
        while True:
            paragraphs = page.get_paragraphs()
            links = page.get_internal_links()
            if not paragraphs:
                print("Нет содержимого для отображения.")
                break
            idx = 0
            while True:
                print(f"\nПараграф {idx+1} из {len(paragraphs)}:\n{paragraphs[idx]}\n")
                print("Выберите действие:")
                print("1. Следующий параграф")
                print("2. Предыдущий параграф")
                print("3. Перейти на одну из внутренних статей")
                print("4. Выйти")
                choice = input("Ваш выбор: ")
                if choice == "1":
                    if idx < len(paragraphs) - 1:
                        idx += 1
                    else:
                        print("Это последний параграф.")
                elif choice == "2":
                    if idx > 0:
                        idx -= 1
                    else:
                        print("Это первый параграф.")
                elif choice == "3":
                    if not links:
                        print("Нет внутренних статей для перехода.")
                        continue
                    print("\nВнутренние статьи:")
                    for i, (text, href) in enumerate(links, 1):
                        print(f"{i}. {text} ({unquote(href)})")
                    num = input("Введите номер статьи для перехода (или Enter для отмены): ")
                    if num.isdigit() and 1 <= int(num) <= len(links):
                        next_title = links[int(num)-1][1].split("/wiki/")[-1]
                        page = WikipediaPage(self.browser, next_title, self.lang)
                        break  # Переходим к новой статье
                    else:
                        print("Некорректный выбор.")
                elif choice == "4":
                    print("Выход.")
                    exit()
                else:
                    print("Некорректный ввод.")

if __name__ == "__main__":
    WikipediaBot().run() 