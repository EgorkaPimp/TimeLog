import requests
from bs4 import BeautifulSoup

# URL сайта
url = "https://products.aspose.app/cells/form/time-log"

# Выполняем GET-запрос к сайту
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    s = soup.find_all('div', class_='cells-row')
    for start in s:
        if start:
            # Ищем <div> по классу и имени, затем находим <input> внутри него
            div_element = start.find('div', {'name': 'C12'})

            if div_element:
                # Ищем <input> внутри найденного <div>
                input_element = div_element.find("input")
                if input_element:
                    # Получаем значения атрибутов элемента
                    input_value = input_element.get("value")  # Если есть текущее значение

                    print(f"Найден элемент:value={input_value}")
                else:
                    print("Элемент <input> не найден внутри <div>.")
            else:
                    # print("Элемент <div> не найден.")
                a = 1
        else:
            print('Элемент старт не найден')
else:
    print(f"Ошибка: не удалось получить доступ к сайту, код ответа {response.status_code}")
