""" This module contains RushHourBoard class for rush hour game.

"""

from __future__ import annotations
import numpy as np
from rush_hour.vehicle import Vehicle
from typing import Tuple, List, Generator
import copy

# Set the goal vehicle
GOAL_VEHICLE_SYMBOL = 'X'
GOAL_VEHICLE = Vehicle(GOAL_VEHICLE_SYMBOL, 4, 2, 'H')


class RushHourBoard:
  """A class used to represent a rush hour board"""

  def __init__(self, vehicles: List[Vehicle]) -> None:
    """RushHourBoard initializer

    Args:
        vehicles (List[Vehicle]): List of vehicles in board.
    """
    self._vehicles = vehicles

  def __eq__(self, __o: object) -> bool:
    # Test if object is an instance of RushHourBoard
    if not isinstance(__o, RushHourBoard):
      return False
    # Check if object is equal
    sorted_vehicles = sorted(self.vehicles, key=lambda x: x.symbol)
    sorted_vehicles_o = sorted(__o.vehicles, key=lambda x: x.symbol)
    return sorted_vehicles == sorted_vehicles_o

  def __repr__(self) -> str:
    return self.get_board().__repr__()

  def __str__(self) -> str:
    return self.get_board().__str__()

  def __hash__(self) -> int:
    return hash(self.__repr__())

  @property
  def vehicles(self) -> List[Vehicle]:
    """Rush hour board vehicles"""
    return self._vehicles

  def _get_empty_board(self) -> np.array:
    """Method to get empty rush hour board.

    Returns:
        np.array: Empty rush hour board
    """
    return np.asarray(
        [
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' '],
        ]
    )

  def get_board(self) -> np.array:
    """Method to get current rush hour board.

    Returns:
        np.array: Rush hour board.
    """
    # Get empty board
    board = self._get_empty_board()
    # Fill board with vehicles
    for vehicle in self.vehicles:
      board[vehicle.get_location_indexes()] = vehicle.symbol
    return board

  def get_next_possible_states(
      self
  ) -> Generator[Tuple[Tuple[str, str], RushHourBoard], None, None]:
    """Method to get all possible next states from current state.

    Yields:
         Generator[Tuple[Tuple[str, str]], RushHourBoard]: A generator of
            actions and next possible states.
    """
    # Get current board
    board = self.get_board()
    # Go over all vehicles
    for vehicle_idx in range(0, len(self.vehicles)):
      # Get the vehicle
      vehicle = self.vehicles[vehicle_idx]
      # Move left or right
      if vehicle.orientation == 'H':
        # Check left position is legal and empty
        if vehicle.can_move_vehicle("left") and board[vehicle.y,
                                                      vehicle.x - 1] == ' ':
          # Move vehicle in next state to not affect current state
          new_vehicles = copy.deepcopy(self.vehicles)
          new_vehicles[vehicle_idx].move_vehicle("left")
          yield (vehicle.symbol, "left"), RushHourBoard(new_vehicles)
        # Check left position is legal and empty
        if vehicle.can_move_vehicle("right") and board[vehicle.y,
                                                       vehicle.x_end +
                                                       1] == ' ':
          # Move vehicle in next state to not affect current state
          new_vehicles = copy.deepcopy(self.vehicles)
          new_vehicles[vehicle_idx].move_vehicle("right")
          yield (vehicle.symbol, "right"), RushHourBoard(new_vehicles)
      # Move down or up
      else:
        # Check up position is legal and empty
        if vehicle.can_move_vehicle("up") and board[vehicle.y - 1,
                                                    vehicle.x] == ' ':
          # Move vehicle in next state to not affect current state
          new_vehicles = copy.deepcopy(self.vehicles)
          new_vehicles[vehicle_idx].move_vehicle("up")
          yield (vehicle.symbol, "up"), RushHourBoard(new_vehicles)
        # Check down position is legal and empty
        if vehicle.can_move_vehicle("down") and board[vehicle.y_end + 1,
                                                      vehicle.x] == ' ':
          # Move vehicle in next state to not affect current state
          new_vehicles = copy.deepcopy(self.vehicles)
          new_vehicles[vehicle_idx].move_vehicle("down")
          yield (vehicle.symbol, "down"), RushHourBoard(new_vehicles)

  def get_distance_to_exit(self) -> int:
    """Method to get distance of red car to goal car

    Returns:
        int: Distance of red car to goal car
    """
    # Find the red car
    red_car = None
    for vehicle in self.vehicles:
      if vehicle.symbol == GOAL_VEHICLE_SYMBOL:
        red_car = vehicle
        break

    # Get distance
    distance = abs(red_car.x - GOAL_VEHICLE.x) + abs(red_car.y - GOAL_VEHICLE.y)
    return distance

  def get_num_blocking_vehicles(self) -> int:
    """Method to get number of vehicle blocking the red car

    Returns:
        int: Number of vehicle blocking the red car.

    """
    # Get current board
    board = self.get_board()
    # Counter for number of blocking cars
    num = 0
    # Loop from exit until we get to the red car
    for i in range(5, -1, -1):
      # Get cell content
      cell = board[2, i]
      # Return number of blocking vehicle
      if cell == "X":
        break
      # No blocking vehicle to add
      elif cell == " ":
        continue
      # Blocking vehicle to add
      else:
        num += 1
    return num

  def get_improved_num_blocking_vehicles(self) -> int:
    """Method to get number of vehicle blocking the red car and check if these
        vehicles are also blocked.

    Returns:
        int: Number of vehicle blocking the red car and if a vehicle is blocked
            too than we count it as two instead of 1.

    """
    # Get current board
    board = self.get_board()
    # Counter for number of blocking vehicle
    num = 0
    # Define set of vehicles blocking
    vehicles_blocking = set()
    # Loop from exit until we get to the red car
    for i in range(5, -1, -1):
      # Get cell content
      cell = board[2, i]
      # Return number of blocking vehicle
      if cell == "X":
        break
      # No blocking vehicle to add
      elif cell == " ":
        continue
      # Blocking car to add
      else:
        # Add vehicle symbol
        vehicles_blocking.add(cell)
        num += 1

    # Loop over all blocking vehicle
    for vehicle in self.vehicles:
      if vehicle.symbol in vehicles_blocking:
        if (not vehicle.can_move_vehicle("up")
           ) and (not vehicle.can_move_vehicle("up")):
          num += 1
    return num

  def is_solved(self) -> bool:
    """Method to check if board is solved

    Returns:
        bool: board is solved indicator.
    """
    return GOAL_VEHICLE in self.vehicles
