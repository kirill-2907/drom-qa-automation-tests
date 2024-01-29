from playwright.sync_api import Page, Locator

from pages.top_menu import TopMenu


class LoginPage(TopMenu):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def fill_login(self, login: str) -> None:
        self._login_field.fill(login)

    def fill_password(self, password: str) -> None:
        self._pass_field.fill(password)

    def click_enter_button(self) -> None:
        self._enter_button.click()

    @property
    def _login_form(self) -> Locator:
        return self.page.locator('#signForm')

    @property
    def _login_field(self) -> Locator:
        return self._login_form.get_by_label("Телефон / Логин")

    @property
    def _pass_field(self) -> Locator:
        return self._login_form.get_by_label("Пароль")

    @property
    def _enter_button(self) -> Locator:
        return self._login_form.get_by_role("button", name="Войти с паролем")