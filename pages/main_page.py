from playwright.sync_api import Locator, expect, Page

from pages.components.bulls_list import BullsList
from pages.components.pagination import Pagination
from pages.components.sales_filter import SalesFilter
from pages.top_menu import TopMenu


class MainPage(TopMenu):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def close_notification_success(self) -> None:
        self._notification_success.locator('div').nth(1).click()

    def wait_notification_success(self) -> None:
        self._notification_success.wait_for()

    def reload_page(self) -> None:
        self.page.reload()

    @property
    def sales_filter(self) -> SalesFilter:
        base_locator = self.page.get_by_test_id('sales__filter')
        return SalesFilter(self.page, base_locator)

    @property
    def bulls_list(self) -> BullsList:
        base_locator = self.page.get_by_test_id('bulls-list_bull').locator('//..')
        return BullsList(self.page, base_locator)

    @property
    def pagination(self) -> Pagination:
        base_locator = self.page.get_by_test_id('component_pagination')
        return Pagination(self.page, base_locator)

    @property
    def _notification_success(self) -> Locator:
        return self.page.get_by_test_id('component_notification_type_success')
