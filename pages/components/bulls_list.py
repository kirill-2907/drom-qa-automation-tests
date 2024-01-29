from typing import List

from playwright.sync_api import Page, Locator

from pages.components.card import Card
from pages.components.pagination import Pagination
from pages.components.sales_filter import SalesFilter


class BullsList:
    def __init__(self, page: Page, base_locator: Locator) -> None:
        self.page = page
        self.base_locator = base_locator
        self.card_locator = self.base_locator.get_by_test_id('bulls-list_bull')
        self.filter = SalesFilter(self.page, self.base_locator.get_by_test_id('sales__filter'))
        self.pagination = Pagination(self.page, self.base_locator.get_by_test_id('component_pagination'))

    def add_first_card_to_favorites(self) -> None:
        Card(self.page, self._first_card_locator).click_add_favorites()
        self.page.pause()

    def get_first_card_title(self) -> str:
        return Card(self.page, self._first_card_locator).get_title()

    def get_first_card_cost(self) -> int:
        return Card(self.page, self._first_card_locator).get_cost()

    def get_list_cards(self) -> List[Card]:
        card_count = self._get_cards_count()
        list_cards = []
        for card_number in range(card_count):
            card = Card(self.page, self.card_locator.nth(card_number))
            list_cards.append(card)
        return list_cards

    def _get_cards_count(self) -> int:
        return self.card_locator.count()

    @property
    def first_card(self) -> Card:
        return Card(self.page, self._first_card_locator)

    @property
    def _first_card_locator(self) -> Locator:
        return self.card_locator.nth(0)

