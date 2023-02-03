""" This module contains the main code to run.

"""

import os
from rush_hour.vehicle import Vehicle
from rush_hour.board import RushHourBoard
from rush_hour.problems import (
    ZeroHeuristic, ManhattanDistanceHeuristic, BlockingVehiclesHeuristic,
    ImprovedBlockingVehiclesHeuristic, DistanceImprovedBlockingVehiclesHeuristic
)
from py_search.uninformed import (breadth_first_search, depth_first_search)
from py_search.informed import (
    best_first_search, iterative_deepening_best_first_search
)
from py_search.utils import compare_searches

# Get boards path
DIR_PATH = os.path.abspath(os.path.dirname(__file__))
BOARDS_PATH = os.path.join(DIR_PATH, "boards")

if __name__ == "__main__":
  # Loop over each board
  for board_number in os.listdir(BOARDS_PATH):
    # Open board file
    with open(os.path.join(BOARDS_PATH, board_number), 'r') as f:
      # Get each vehicle in board
      vehicles = [
          Vehicle(symbol, int(x), int(y), orientation)
          for symbol, x, y, orientation in f.read().splitlines()
      ]
      # Create board
      board = RushHourBoard(vehicles)

      # print board number
      print(f"\n\n{board_number}")

      # Run BFS and DFS
      compare_searches(
          problems=[
              ZeroHeuristic(initial=board),
          ], searches=[breadth_first_search, depth_first_search]
      )

      # Run A* & IDA*
      compare_searches(
          problems=[
              ZeroHeuristic(initial=board),
              ManhattanDistanceHeuristic(initial=board),
              BlockingVehiclesHeuristic(initial=board),
              ImprovedBlockingVehiclesHeuristic(initial=board),
              DistanceImprovedBlockingVehiclesHeuristic(initial=board),
          ],
          searches=[best_first_search, iterative_deepening_best_first_search]
      )
