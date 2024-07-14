import numpy as np
from domain import Card, DoorType, DrawCard, CardType, CardFactory
from typing import List

class ServiceDrawCard(DrawCard):
  p_def_min: float = 0.15
  p_def_max: float = 0.3
  p_monster_min: float = 0.3

  monster_level_diff: int = 2
  monster_level_sigma: int = 2.3
  possible_monster_levels = np.arange(1, 25)

  def draw_door(self, level: int, method='sigmoid') -> Card:
    door_type = self._draw_card_door_type(level, method)
    card_level: int = 1

    if door_type == DoorType.MONSTER:
        card_level = self._draw_card_monster_level(level)

    card_type = CardFactory.create_card(CardType.DOOR, None, None, card_level, door_type)

    return card_type
  
  def _draw_card_door_type_linear_probabilities(self, level: int) -> List[float]:
      P_n = self.p_def_min - self.p_def_max * (level - 1) / 9
      P_m = max(self.p_monster_min, (1 - P_n) * (1 - level / 10))
      P_c = 1 - P_m - P_n
      return P_m, P_c, P_n
  
  def _draw_card_door_type_sigmoid_probability(self, level: int, k = 1, L0 = 5) -> List[float]:
    P_n = self.p_def_max - (self.p_def_max - self.p_def_min) * (1 / (1 + np.exp(k * (level - L0))))
    P_m = max(self.p_monster_min, (1 - P_n) * (1 / (1 + np.exp(k * (level - L0)))))
    P_c = 1 - P_m - P_n
    return P_m, P_c, P_n
  
  def _draw_card_door_type(self, level: int, method='sigmoid') -> DoorType:
    if method == 'linear':
        P_m, P_c, P_n = self._draw_card_door_type_linear_probabilities(level)
    elif method == 'sigmoid':
        P_m, P_c, P_n = self._draw_card_door_type_sigmoid_probability(level)
    else:
        raise ValueError("Method should be 'linear' or 'sigmoid'")
    
    random_number = np.random.rand()
    
    if random_number < P_m:
        return DoorType.MONSTER
    elif random_number < P_m + P_c:
        return DoorType.CURSE
    else:
        return DoorType.DEFAULT
    
  def _draw_card_monster_level(self, level: int) -> int:
    mu = level + self.monster_level_diff

    unnormalized_probs = np.exp(-((self.possible_monster_levels - mu) ** 2) / (2 * self.monster_level_sigma ** 2))
    normalized_probs = unnormalized_probs / np.sum(unnormalized_probs)

    npValue = np.random.choice(self.possible_monster_levels, p=normalized_probs)

    return npValue.item()