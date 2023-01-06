"""Pydantic models of card data"""
from pydantic import BaseModel


class Card(BaseModel):
    title: str = ...
    url: str = ...
    description: str = ...
    image: str = ...
    button: str = ...


def parse_cards(data: dict) -> list[Card]:
    cards = []
    for card_data in data.values():
        cards.append(Card.parse_obj(card_data))
    return cards
