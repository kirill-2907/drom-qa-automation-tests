from playwright.sync_api import Page, Locator


class Dropdown:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def select_option(self, option: str) -> None:
        self.base_locator.get_by_text(option).click()


class InputButton:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def click(self) -> None:
        self.base_locator.click()

    def fill(self, option: str) -> None:
        self.base_locator.get_by_role('combobox').fill(option)

    def select(self, option: str) -> None:
        self.base_locator.get_by_text(option).click()

    @property
    def _drop_down_locator(self) -> Locator:
        return self.base_locator.get_by_test_id('component_select_dropdown')

    @property
    def dropdown(self) -> Dropdown:
        return Dropdown(self.page, self._drop_down_locator)


class DoubleInputButton:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def click_from(self) -> None:
        self._input_from.click()

    def click_to(self) -> None:
        self._input_to.click()

    def fill_from(self, option: str) -> None:
        self._input_from.fill(option)

    def fill_to(self, option: str) -> None:
        self._input_to.fill(option)

    @property
    def _input_from(self) -> Locator:
        return self.base_locator.locator('input').nth(0)

    @property
    def _input_to(self) -> Locator:
        return self.base_locator.locator('input').nth(1)

    @property
    def _dropdown_from(self) -> Locator:
        return self.base_locator.get_by_role('listbox').nth(0)

    @property
    def _dropdown_to(self) -> Locator:
        return self.base_locator.get_by_role('listbox').nth(1)


class SelectButton:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def click(self) -> None:
        self.base_locator.click()

    @property
    def dropdown(self) -> Dropdown:
        return Dropdown(self.page, self.base_locator.get_by_test_id('component_select_dropdown'))


class CheckBox:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def check(self) -> None:
        self.base_locator.check()
