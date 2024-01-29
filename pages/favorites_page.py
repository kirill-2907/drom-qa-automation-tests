from playwright.sync_api import Page, Locator, expect

from pages.components.favorite_card import FavoriteCard
from pages.top_menu import TopMenu


class FavoritesPage(TopMenu):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def get_first_card_title(self) -> str:
        return FavoriteCard(self.page, self._first_card).get_title()

    def get_first_card_cost(self) -> int:
        return FavoriteCard(self.page, self._first_card).get_cost()

    def remove_first_card(self) -> None:
        FavoriteCard(self.page, self._first_card).click_button_remove()

    def wait_message_del_from_favorites(self) -> None:
        expect(self._message.get_by_text('Удалено из избранного')).to_be_visible()

    @property
    def _first_card(self) -> Locator:
        return self._cards_list.locator('.bull-item__content-wrapper').nth(0)

    @property
    def _cards_list(self) -> Locator:
        return self.page.locator('.favorites-list')

    @property
    def _message(self) -> Locator:
        return self.page.locator('#flashMessage')
