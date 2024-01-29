from playwright.sync_api import Page, Locator


class FavoriteCard:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator
        self.title_locator = self.base_locator.locator('.bull-item__subject-container')
        self.cost_locator = self.base_locator.locator('.price-block__price')

    def get_title(self) -> str:
        return self.title_locator.inner_text()

    def get_cost(self) -> int:
        cost_string = self.cost_locator.inner_text()[:-1].replace(' ', '')
        return int(cost_string)

    def click_button_remove(self) -> None:
        self._button_remove.click()

    @property
    def _button_remove(self) -> Locator:
        return self.base_locator.locator('.removeBookmark')
