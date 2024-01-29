from playwright.sync_api import Page, Locator


class Card:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator
        self.title_locator = self.base_locator.get_by_test_id('bull_title').locator('//..').first
        self.milage_locator = self.base_locator.get_by_test_id('bull_description-item').nth(4)
        self.cost_locator = self.base_locator.get_by_test_id('bull_price')
        self.favorite_locator = self.base_locator.locator('svg')

    def get_year(self) -> int:
        title = self.title_locator.locator('span').inner_text()
        return int(title[-4:])

    def get_milage(self) -> str:
        return self.milage_locator.inner_text()

    def get_title(self) -> str:
        return self.title_locator.inner_text()

    def get_cost(self) -> int:
        cost_string = self.cost_locator.inner_text().replace('\xa0', '')
        return int(cost_string)

    def click_add_favorites(self) -> None:
        self.favorite_locator.click(force=True)
