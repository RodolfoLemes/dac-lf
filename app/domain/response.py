import json
from typing import Any, Optional

from .card import Card

class Response:
  status_code: int
  data: Optional[Card]
  err_message: Optional[str]
  

  def __init__(self, status_code: int, data: Optional[Card], err_message: Optional[str] = None) -> None:
    self.status_code = status_code
    self.data = data
    self.err_message = err_message

  # response function, convert to json
  def to_json(self):
    payload = {
      'status_code': self.status_code,
    }

    if self.data:
      payload['data'] = self.data.to_json()

    if self.err_message:
      payload['err_message'] = self.err_message

    return payload
  

