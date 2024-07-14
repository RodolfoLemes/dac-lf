from abc import ABC, abstractmethod
from ctypes import Union
from enum import Enum, auto
from typing import Optional

class CardType(Enum):
    TREASURE = auto()
    DOOR = auto()

class DoorType(Enum):
    MONSTER = auto()
    CURSE = auto()
    DEFAULT = auto()

class Card(ABC):
    name: Optional[str]
    description: Optional[str]
    level: int
    card_type: CardType

    def __init__(self, name: Optional[str], description: Optional[str], level: int, card_type: CardType):
        self.name = name
        self.description = description
        self.level = level
        self.card_type = card_type

    @abstractmethod
    def card_type(self):
        pass
    
    def __str__(self) -> str:
        return f"Name: {self.name}, Description: {self.description}, Level: {self.level}, Type: {self.card_type.name}"
    
    # json
    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'level': self.level,
            'card_type': self.card_type.name
        }

class Treasure(Card):
    def __init__(self, name: str, description: str, level: int):
        super().__init__(name, description, level, CardType.TREASURE)

    def card_type(self):
        return self.card_type

# Door card class with specific types (Monster, Curse, and Default)
class Door(Card):
    def __init__(self, name: str, description: str, level: int, door_type: DoorType):
        super().__init__(name, description, level, CardType.DOOR)
        self.door_type = door_type

    def card_type(self):
        return self.card_type

    def door_specific_type(self):
        return self.door_type
    
    def __str__(self) -> str:
        return f"{super().__str__()}, Door Type: {self.door_type.name}"
    
    def to_json(self):
        return {
            **super().to_json(),
            'door_type': self.door_type.name
        }
    

class CardFactory:
    @staticmethod
    def create_card(card_type: CardType, name: Optional[str], description: Optional[str], level: int, door_type: Optional[DoorType] = None) -> Card:
        if card_type == CardType.TREASURE:
            return Treasure(name, description, level)
        
        if card_type == CardType.DOOR:
            if door_type is None:
                raise ValueError("door_type must be provided for Door cards")
            return Door(name, description, level, door_type)
        
        raise ValueError(f"Unknown card type: {card_type}")