import allure
import pytest
from playwright.sync_api import expect

from pages.main_page import MainPage

BRAND_TOYOTA = 'Toyota'
MODEL_HARRIER = 'Harrier'
FUEL_HYBRID = 'Гибрид'
MILAGE_FROM = 1
YEAR_FROM = 2007


@pytest.mark.filter
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Check cars filter by params')
def test_filter_cars(f_main_page: MainPage) -> None:
    main_page = f_main_page

    with allure.step('Click filter advanced button'):
        main_page.sales_filter.click_expand_search()

    with allure.step(f'Select brand - {BRAND_TOYOTA}'):
        main_page.sales_filter.select_brand(BRAND_TOYOTA)

    with allure.step(f'Select model - {MODEL_HARRIER}'):
        main_page.sales_filter.select_model(MODEL_HARRIER)

    with allure.step(f'Select fuel type - {FUEL_HYBRID}'):
        main_page.sales_filter.select_fuel(FUEL_HYBRID)

    with allure.step('Check checkbox unsold'):
        main_page.sales_filter.check_checkbox_unsold()

    with allure.step(f'Select milage from - {MILAGE_FROM}'):
        main_page.sales_filter.fill_milage_from(MILAGE_FROM)

    with allure.step(f'Select year from - {YEAR_FROM}'):
        main_page.sales_filter.select_year_from(YEAR_FROM)

    with allure.step('Click show button'):
        main_page.sales_filter.click_button_show()

    with allure.step('Check that current page is 1'):
        current_page = main_page.pagination.get_current_page()
        assert current_page == 1

    with allure.step('Check that cars milage in bulls list are visible'):
        list_cards = main_page.bulls_list.get_list_cards()
        for card in list_cards:
            assert card.milage_locator.is_visible(), 'Milage locator is missed'
            assert len(card.get_milage()) > 0, 'Milage field is empty'

    with allure.step(f'Check that cars years are greater or equal {YEAR_FROM}'):
        for card in list_cards:
            assert card.get_year() >= YEAR_FROM

    with allure.step('Check that cars titles are without line-through'):
        for card in list_cards:
            expect(card.title_locator).not_to_have_css('text-decoration-line', 'line-through'), (
                'Car is sold'
            )

    with allure.step('Click pagination page 2 and check that page is switched'):
        main_page.pagination.select_page(2)
        current_page = main_page.pagination.get_current_page()
        assert current_page == 2

    with allure.step('Check that cars milage are visible'):
        list_cards = main_page.bulls_list.get_list_cards()
        for card in list_cards:
            assert card.milage_locator.is_visible(), 'Milage locator is missed'
            assert len(card.get_milage()) > 0, 'Milage field is empty'

    with allure.step(f'Check that cars years are greater or equal {YEAR_FROM}'):
        for card in list_cards:
            assert card.get_year() >= YEAR_FROM

    with allure.step('Check that cars are not sold'):
        for card in list_cards:
            expect(card.title_locator).not_to_have_css('text-decoration-line', 'line-through'), (
                'Car is sold'
            )
