import re
from typing import List

import pytest  # noqa
from playwright.sync_api import Page

SEARCH_INTEGER_PATTERN = re.compile(r"\d+")


@pytest.mark.parametrize(
    "path",
    [
        "/fun-fact-full-load",
        "/fun-fact-partial-load",
    ],
)
def test_get_fun_facts(path: str, page: Page):
    page.goto(path)

    assert page.get_by_text("daisyUI").is_visible()
    assert page.get_by_text("Full Load Page").is_visible()
    assert page.get_by_text("Partial Load Page").is_visible()

    # Check if counting is working properly
    page.wait_for_selector(':text("Total Fun Facts Count:")')
    total_count_text: str = page.get_by_text("Total Fun Facts Count:").inner_text()
    assert SEARCH_INTEGER_PATTERN.search(total_count_text).group()

    # Check if cards are loaded properly
    cards_titles: List[str]
    cards_bodies: List[str]
    cards_titles, cards_bodies = get_cards(page=page)

    # Check if getting new random fun facts is working
    page.get_by_text("Get Random Fun Facts").click()

    # Introduce a delay to wait for DOM update
    page.wait_for_timeout(1000)

    new_cards_titles: List[str]
    new_cards_bodies: List[str]
    new_cards_titles, new_cards_bodies = get_cards(page=page)

    assert cards_titles != new_cards_titles
    assert cards_bodies != new_cards_bodies

    # Check navigation
    page.get_by_text("Full Load Page").click()
    page.get_by_text("Partial Load Page").click()


def get_cards(page: Page) -> List[List[str]]:
    page.wait_for_selector(".card")
    cards = page.query_selector_all(".card")
    assert len(cards) == 3

    cards_titles: List[str] = []
    cards_bodies: List[str] = []
    for card in cards:
        card_title = card.query_selector(".card-title").inner_text()
        card_body = card.query_selector("p").inner_text()

        assert card_title
        assert card_body

        cards_titles.append(card_title)
        cards_bodies.append(card_body)
    cards_titles = sorted(cards_titles)
    cards_bodies = sorted(cards_bodies)

    return cards_titles, cards_bodies
