import requests
from bs4 import BeautifulSoup

alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

with open("beasts.csv","w",encoding="utf-8") as f:
    for sym in alphabet:
        print(1111111)
        count = 0
        page_url = requests.get(
            f"https://ru.wikipedia.org/w/index.php?title=Категория%3AЖивотные_по_алфавиту&from={sym}")
        next_animal = False
        while page_url:
            if page_url.status_code == 200:
                soup = BeautifulSoup(page_url.text, 'html.parser')
                animal_list = soup.find('div', {'class': 'mw-category mw-category-columns'}).find('ul')

                # Извлекаем животных из списка
                animals = []
                for li in animal_list.find_all('li'):
                    print(li.text)
                    part1 = li.text.strip()[0].upper() == sym or li.text.strip()[0].upper() == "Ё"
                    part3 = len(li.text)>1
                    if len(li.text.strip().split())>1:
                        part2 = li.text.strip().split()[1][0].upper() == sym or li.text.strip().split()[1][0].upper() == "Ё"
                    if (part1 or part2) and part3:
                        animals.append(li.text.strip())
                    else:
                        next_animal = True
                        break
                count += len(animals)
                if next_animal:
                    break

                next_page_link = soup.find('div', {'id': 'mw-pages'}).findAll('a', {'title': 'Категория:Животные по алфавиту'})
                if next_page_link:
                    for link in next_page_link:
                        if link.text == "Следующая страница":
                            next_page_link = 'https://ru.wikipedia.org' + link["href"]
                            page_url = requests.get(next_page_link)
                            break
                else:
                    page_url = None
            else:
                print(f"Не удалось получить данные для символа {sym}")
        f.write(f"{sym},{count}\n")
