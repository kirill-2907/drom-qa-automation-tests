import re
from operator import itemgetter

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

REGION = 25


def get_20_brands_sorted_by_count(region: int) -> None:
    with sync_playwright() as p:
        p.selectors.set_test_id_attribute('data-ftid')

        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        url = 'https://auto.drom.ru/'
        page.goto(url + 'region' + str(region))

        page.evaluate('const test = document.querySelector(\'div[data-ftid="component_select_dropdown"]\'); \
            test.style.cssText = \'max-height: fit-content\';')

        page.get_by_placeholder('Марка').click()

        html = page.content()

        context.close()
        browser.close()

    soup = BeautifulSoup(html, 'lxml')
    items = soup.find('div', {"data-ftid": "sales__filter_fid"}).find_all('div', {'role': 'option'})

    pattern_count = re.compile(r'\d+')

    list_items_and_counts = []
    for item in items:
        item_with_count = []
        count_by_item = (re.findall(pattern_count, item.text))
        if len(count_by_item) > 0:
            count = int(count_by_item[0])
        else:
            count = 0
        item = item.text.replace(f' ({count})', '')

        item_with_count.append(item)
        item_with_count.append(count)

        list_items_and_counts.append(item_with_count)

    list_items_without_top_5 = list_items_and_counts[5:]

    sorted_list_by_count_desc = sorted(list_items_without_top_5, key=itemgetter(1), reverse=True)

    print('| Фирма | Количество обьявлений |')
    for item in sorted_list_by_count_desc[:20]:
        print(f'| {item[0]} | {item[1]} |')


if __name__ == "__main__":
    get_20_brands_sorted_by_count(REGION)
