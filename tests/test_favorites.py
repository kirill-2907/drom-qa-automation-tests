import allure
import pytest
from playwright.sync_api import expect

from pages.favorites_page import FavoritesPage
from pages.main_page import MainPage

COLOR_RED_FAVORITE = 'rgb(219, 0, 26)'


@pytest.mark.favorites
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Check add first card to favorites')
def test_add_first_card_to_favorites(
    f_login_user: MainPage,
) -> None:
    main_page = f_login_user

    with allure.step('Add first card to favorites'):
        first_car_title = main_page.bulls_list.get_first_card_title()
        first_car_cost = main_page.bulls_list.get_first_card_cost()

        main_page.bulls_list.add_first_card_to_favorites()

    with allure.step('Wait notification that card were added to favorites'):
        main_page.wait_notification_success()
        main_page.close_notification_success()

    with allure.step('Check that button add card to favorite is red'):
        first_card = main_page.bulls_list.first_card
        expect(first_card.favorite_locator).to_have_css('color', COLOR_RED_FAVORITE)

    with allure.step('Reload page and check that button add card to favorite is still red'):
        main_page.reload_page()
        first_card = main_page.bulls_list.first_card
        expect(first_card.favorite_locator).to_have_css('color', COLOR_RED_FAVORITE)

    with allure.step('Go to favorites page'):
        main_page.click_favorite_button()
        favorite_page = FavoritesPage(main_page.page)

        favorite_card_title = favorite_page.get_first_card_title()
        favorite_card_cost = favorite_page.get_first_card_cost()

    with allure.step('Check that added card to favorites is shown in favorites'):
        assert favorite_card_title == first_car_title
        assert favorite_card_cost == first_car_cost

    # TODO: add this step to a fixture
    with allure.step('Remove added card from favorites'):
        favorite_page.remove_first_card()
        favorite_page.wait_message_del_from_favorites()
