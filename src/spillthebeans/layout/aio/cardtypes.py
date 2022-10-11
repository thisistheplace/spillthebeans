"""Pydantic models of card data"""
from pydantic import BaseModel
from pydantic_yaml import YamlModelMixin

class Card(YamlModelMixin, BaseModel):
    url: str = ...
    description: str = ...
    image: str = ...