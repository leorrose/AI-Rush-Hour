from rush_hour.board import RushHourBoard
from typing import List


class BFS:

  def __init__(self, start_board: RushHourBoard) -> None:
    """BFS initializer

    Args:
        start_board (RushHourBoard): Start board to look for a solution.
    """
    self.start = start_board

  def solve(self) -> List[RushHourBoard]:
    """Method to apply BFS solution

    Returns:
        List[RushHourBoard]: Boards from start to solution or empty list when
            no solution was found.
    """
    # Define  map from node to parent for path construction
    parent = {}
    # Define queue of open list nodes
    open = []
    # Define set of closed list nodes
    visited = set()
    # Add start node to open list
    open.append(self.start)
    # Loop over open list
    while open:
      # Get first node
      node = open.pop(0)
      # Goal test
      if node.is_solved():
        # define path containing end node
        path = [node]
        # Backtrace until we reach start node
        while path[-1] != self.start:
          # Append parent of last node
          path.append(parent[path[-1]])
        # Reverse path from end -> start to start -> end
        path.reverse()
        # return solution
        return path
      # Expand node
      for new_node in node.get_next_possible_states():
        # Make sure no duplicate states
        if new_node not in visited:
          # Map new node to node
          parent[new_node] = node
          # Add new node to open list
          open.append(new_node)
          # Add new node to closed list
          visited.add(new_node)
    return []
