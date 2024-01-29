from playwright.sync_api import Page, Locator

from pages.components.elements import InputButton, DoubleInputButton, SelectButton, CheckBox


class SalesFilter:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator

    def click_expand_search(self) -> None:
        self._button_filter_advanced.click()

    def click_button_show(self) -> None:
        self._button_show.click()

    def select_brand(self, brand: str) -> None:
        self._input_button_brand.click()
        self._input_button_brand.fill(brand)
        self._input_button_brand.dropdown.select_option(brand)

    def select_model(self, model: str) -> None:
        self._input_button_model.click()
        self._input_button_model.fill(model)
        self._input_button_model.dropdown.select_option(model)

    def select_fuel(self, fuel: str) -> None:
        self._button_fuel.click()
        self._button_fuel.dropdown.select_option(fuel)

    def check_checkbox_unsold(self) -> None:
        self._checkbox_unsold.check()

    def fill_milage_from(self, milage: int) -> None:
        self._milage_buttons.click_from()
        self._milage_buttons.fill_from(str(milage))

    def select_year_from(self, year: int) -> None:
        self._input_year_from.click()
        self._input_year_from.dropdown.select_option(str(year))

    @property
    def _locator_advanced_filter(self) -> Locator:
        return self.base_locator.get_by_test_id('bulls-list_filter_full')

    @property
    def _button_filter_advanced(self) -> Locator:
        return self.base_locator.get_by_test_id('sales__filter_advanced-button')

    @property
    def _button_show(self) -> Locator:
        return self.base_locator.get_by_role('button', name='Показать')

    @property
    def _input_button_brand(self) -> InputButton:
        locator = self.base_locator.get_by_test_id('sales__filter_fid')
        return InputButton(self.page, locator)

    @property
    def _input_button_model(self) -> InputButton:
        locator = self.base_locator.get_by_test_id('sales__filter_mid')
        return InputButton(self.page, locator)

    @property
    def _button_fuel(self) -> SelectButton:
        locator = self.base_locator.get_by_test_id('sales__filter_fuel-type')
        return SelectButton(self.page, locator)

    @property
    def _checkbox_unsold(self) -> CheckBox:
        locator = self.base_locator.get_by_text('Непроданные')
        return CheckBox(self.page, locator)

    @property
    def _milage_buttons(self) -> DoubleInputButton:
        locator = self._locator_advanced_filter.get_by_text('Пробег').locator('//..')
        return DoubleInputButton(self.page, locator)

    @property
    def _input_year_from(self) -> InputButton:
        locator = self.base_locator.get_by_test_id('sales__filter_year-from')
        return InputButton(self.page, locator)
