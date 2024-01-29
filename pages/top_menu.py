from playwright.sync_api import Page, Locator, expect


class TopMenu:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_locator = self.page.get_by_test_id('component_header')

    def click_login_button(self) -> None:
        self._login_button.click()

    def click_favorite_button(self) -> None:
        self._favorite_button.click()

    @property
    def _link_auto(self) -> Locator:
        return self.base_locator.get_by_role('link', name='Автомобили')

    @property
    def _login_button(self) -> Locator:
        return self.base_locator.get_by_test_id('component_header_login')

    @property
    def _favorite_button(self) -> Locator:
        return self.base_locator.get_by_test_id('component_header_my-favorite').nth(1)
