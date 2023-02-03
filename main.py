""" """

import os
import time
import functools
from rush_hour.vehicle import Vehicle
from rush_hour.board import RushHourBoard, GOAL_VEHICLE
from search.bfs import BFS
from rush_hour.problem import ZeroHeuristicRushHour, BlockingCarsHeuristicRushHour
from py_search.uninformed import breadth_first_search, depth_first_search
from py_search.informed import best_first_search

from py_search.utils import compare_searches

DIR_PATH = os.path.dirname(__file__)
PROBLEMS_PATH = f"{DIR_PATH}/problems"

if __name__ == "__main__":
  for problem in os.listdir(PROBLEMS_PATH):
    with open(os.path.join(PROBLEMS_PATH, problem), 'r') as f:
      vehicles_info = f.read().splitlines()
      vehicles = [
          Vehicle(symbol, int(x), int(y), orientation)
          for symbol, x, y, orientation in vehicles_info
      ]
      board = RushHourBoard(vehicles)
      print(f"\n\n{problem}")
      compare_searches(
          problems=[BlockingCarsHeuristicRushHour(initial=board)],
          searches=[best_first_search]
      )
      """
      bfs = BFS(board)
      start_time = time.time()
      sol = bfs.solve()
      end_time = time.time()
      print(
          f"Solution of Problem {problem}, Time - {end_time-start_time}, Length {len(sol)}"
      )
      """
