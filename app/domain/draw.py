from abc import ABC, abstractmethod
from .card import Card

class DrawCard(ABC):
  @abstractmethod
  def draw_door(self, level: int, method='linear') -> Card:
    pass