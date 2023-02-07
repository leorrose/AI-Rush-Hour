"""This module contains Vehicle class for rush hour game.

"""

from typing import List, Tuple

CARS = ('X', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')
TRUCKS = ('O', 'P', 'Q', 'R')


class Vehicle:
  """A class used to represent a Vehicle"""

  def __init__(self, symbol: str, x: int, y: int, orientation: str) -> None:
    """Vehicle initializer

    Args:
        symbol (str): Vehicle symbol. should be in ('X', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K') for cars and in ('O', 'P', 'Q',
            'R') for trucks. 
        x (int): Vehicle x coordinate. should be between 0-5.
        y (int): Vehicle y coordinate. should be between 0-5.
        orientation (str): Vehicle orientation. should be between "V" or "H".

    """
    # Validate symbol
    if (symbol not in CARS) and (symbol not in TRUCKS):
      raise ValueError(
          f"symbol most be in {CARS} for cars and in {TRUCKS} for trucks. "
      )

    # Validate orientation
    if orientation != 'H' and orientation != 'V':
      raise ValueError("orientation most be V or H")

    # Assign properties
    self._symbol = symbol
    self._x = x
    self._y = y
    self._orientation = orientation
    self._length = 2 if symbol in CARS else 3
    self._x_end = (
        self._x if self._orientation == "V" else self._x + (self._length - 1)
    )
    self._y_end = (
        self._y if self._orientation == "H" else self._y + (self._length - 1)
    )

  def __eq__(self, __o: object) -> bool:
    # Test if object is an instance of Vehicle
    if not isinstance(__o, Vehicle):
      return False
    # Check if object is equal
    return (
        self.symbol == __o.symbol and self.x == __o.x and self.y == __o.y and
        self.orientation == __o.orientation
    )

  def __ne__(self, __o: object) -> bool:
    # Check if object is not equal
    return not self.__eq__(__o)

  def __repr__(self) -> str:
    return f"Vehicle({self.symbol}, {self.x}, {self.y}, {self.orientation})"

  def __hash__(self) -> int:
    return hash(self.__repr__())

  @property
  def symbol(self) -> int:
    """Vehicle symbol. should be in ('X', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K') for cars and in ('O', 'P', 'Q', 'R') for trucks."""
    return self._symbol

  @property
  def x(self) -> int:
    """Vehicle x coordinate. should be between 0-5."""
    return self._x

  @property
  def x_end(self) -> int:
    """Vehicle x end coordinate. should be between 0-5."""
    return self._x_end

  @property
  def y(self) -> int:
    """Vehicle y coordinate. should be between 0-5"""
    return self._y

  @property
  def y_end(self) -> int:
    """Vehicle y end coordinate. should be between 0-5."""
    return self._y_end

  @property
  def orientation(self) -> str:
    """Vehicle orientation. should be between "V" or "H"""
    return self._orientation

  @property
  def length(self) -> str:
    """Vehicle length. should be between 2 for car and 3 for truck"""
    return self._length

  @symbol.setter
  def symbol(self, value) -> None:
    raise AttributeError("Can set attribute only on creation.")

  @x.setter
  def x(self, value) -> None:
    # Get x end value
    x_end = value if self._orientation == "V" else value + (self._length - 1)
    # Validate x and x_end
    if (value < 0) or (value > 5):
      raise ValueError("x most be between 0-5")
    if (x_end < 0) or (x_end > 5):
      raise ValueError("x_end most be between 0-5")
    # Assign property
    self._x = value
    self._x_end = x_end

  @x_end.setter
  def x_end(self, value) -> None:
    raise AttributeError("x_end is decided by the value of y")

  @y.setter
  def y(self, value) -> None:
    # Get y end value
    y_end = value if self._orientation == "H" else value + (self._length - 1)
    # Validate y and y_end
    if (value < 0) or (value > 5):
      raise ValueError("y most be between 0-5")
    if (y_end < 0) or (y_end > 5):
      raise ValueError("y_end most be between 0-5")
    # Assign property
    self._y = value
    self._y_end = y_end

  @y_end.setter
  def y_end(self, value) -> None:
    raise AttributeError("y_end is decided by the value of y")

  @orientation.setter
  def orientation(self, value) -> None:
    raise AttributeError("Can set attribute only on creation.")

  @length.setter
  def length(self, value) -> None:
    raise AttributeError("length is decided by the value of symbol")

  @symbol.deleter
  def symbol(self) -> None:
    del self._symbol

  @x.deleter
  def x(self) -> None:
    del self._x

  @x_end.deleter
  def x_end(self) -> None:
    del self._x_end

  @y.deleter
  def y(self) -> None:
    del self._y

  @y_end.deleter
  def y_end(self) -> None:
    del self._y_end

  @orientation.deleter
  def orientation(self) -> None:
    del self._orientation

  @length.deleter
  def length(self) -> None:
    del self._length

  def move_vehicle(self, direction: str) -> None:
    """Method to move vehicle.

    Args:
        direction (str): Direction to move. should be left, right, down or up.

    Raises:
        ValueError: If direction is incorrect or invalid direction.

    """
    if direction == "left":
      if self.orientation != "H":
        ValueError("Cannot move vertical vehicle right")
      self.x -= 1
    elif direction == "right":
      if self.orientation != "H":
        ValueError("Cannot move vertical vehicle right")
      self.x += 1
    elif direction == "down":
      if self.orientation != "V":
        ValueError("Cannot move vertical vehicle right")
      self.y += 1
    elif direction == "up":
      if self.orientation != "V":
        ValueError("Cannot move vertical vehicle right")
      self.y -= 1
    else:
      raise ValueError("Invalid direction")

  def can_move_vehicle(self, direction: str) -> bool:
    opposite_direction = {
        "left": "right",
        "right": "left",
        "down": "up",
        "up": "down"
    }
    opposite_direction = opposite_direction[direction]
    try:
      self.move_vehicle(direction)
      self.move_vehicle(opposite_direction)
      return True
    except ValueError:
      return False

  def get_location_indexes(self) -> Tuple[List[int], List[int]]:
    """Method to get vehicle indexes on grid

    Returns:
        Tuple[List[int], List[int]]: y indexes, x indexes
    """
    if self.orientation == "H":
      return [self.y] * self._length, list(range(self.x, self.x_end + 1))
    return list(range(self.y, self.y_end + 1)), [self.x] * self._length
