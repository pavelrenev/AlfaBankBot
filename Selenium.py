import hashlib
import re
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def chooseFilters(driver):
    driver.find_element(By.CSS_SELECTOR, ".select-button.select-button_view_default.select-button_size_m.select-button_theme_alfa-on-white").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[(@class='menu-item__control') and (text() = 'Без опыта')]").click()




def scroll_and_save_page(driver, file_path, scroll_pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    last_content_hash = None

    while True:
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

        current_content_hash = hashlib.sha256(driver.page_source.encode('utf-8')).hexdigest()
        if current_content_hash != last_content_hash:
            with open(file_path, "w") as file:
                file.write(driver.page_source)
            last_content_hash = current_content_hash

        last_height = new_height


def main():
    url = "https://job.alfabank.ru/vacancies"

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(url)
        chooseFilters(driver)
        time.sleep(120)
        # scroll_and_save_page(driver, "source.html")

        # with open("source.html", "r") as file:
        #     html_content = file.read()
        #
        # soup = BeautifulSoup(html_content, "html.parser")
        # regex = re.compile(r'title title_size-s vacancy__title VacanciesItem_vacancy__title')
        # vacancy_tags = soup.findAll(class_=regex)
        #
        # # Получение текста из каждого тега и добавление его в список
        # all_vacancies = [tag.text.strip() for tag in vacancy_tags]
        #
        # # Вывод списка всех вакансий
        # print(len(all_vacancies))
        # print("\n".join(all_vacancies))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()





