from playwright.sync_api import Page, Locator


class Pagination:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def select_page(self, page_number: int) -> None:
        self._pagination_page.get_by_text(str(page_number)).click()

    def get_current_page(self) -> int:
        current_page_string = self._current_page.inner_text()
        return int(current_page_string)

    @property
    def _current_page(self) -> Locator:
        return self.base_locator.locator('.css-xz6vp0.e10f3cqr0')

    @property
    def _pagination_page(self) -> Locator:
        return self.base_locator.get_by_role('link')
