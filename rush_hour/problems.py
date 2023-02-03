""" This module contains rush hour problems. """

from py_search.base import Problem, Node
from typing import Generator


class ZeroHeuristic(Problem):
  """A class used to represent a zero heuristic problem"""

  def successors(self, node: Node) -> Generator[Node, None, None]:
    """Method to Computes successors.

    Args:
        node (Node): Node to computes successors.

    Yields:
         Generator[Node, None, None]: Successors.
    """
    for action, new_node in node.state.get_next_possible_states():
      path_cost = node.cost() + 1
      yield Node(new_node, node, action, path_cost)

  def heuristic(self, node: Node) -> int:
    """Method to get heuristic.

    Args:
        node (Node):  Node to compute heuristic.

    Returns:
        int: Heuristic value.
    """
    return 0

  def node_value(self, node: Node):
    """Method used to compute the value of a node.

    Args:
        node (Node): Node to compute value.

    Returns:
        _type_: Value of a node.
    """
    return node.cost() + self.heuristic(node)

  def goal_test(self, state_node: Node, goal_node: Node = None) -> bool:
    """Method to test of whether a complete assignment has been reached.

    Args:
        state_node (Node): Current state node.
        goal_node (Node, optional): Goal node. Defaults to None.

    Returns:
        bool: Complete assignment has been reached or not.
    """
    return state_node.state.is_solved()


class ManhattanDistanceHeuristic(ZeroHeuristic):
  """A class used to represent a manhattan distance heuristic problem"""

  def heuristic(self, node: Node):
    """Method to get heuristic.

    Args:
        node (Node):  Node to compute heuristic.

    Returns:
        int: Heuristic value.
    """
    return node.state.get_distance_to_exit()


class BlockingVehiclesHeuristic(ZeroHeuristic):
  """A class used to represent a blocking vehicles heuristic problem"""

  def heuristic(self, node: Node):
    """Method to get heuristic.

    Args:
        node (Node):  Node to compute heuristic.

    Returns:
        int: Heuristic value.
    """
    return node.state.get_num_blocking_vehicles()


class ImprovedBlockingVehiclesHeuristic(ZeroHeuristic):
  """A class used to represent a improved blocking vehicles heuristic problem"""

  def heuristic(self, node: Node):
    """Method to get heuristic.

    Args:
        node (Node):  Node to compute heuristic.

    Returns:
        int: Heuristic value.
    """
    return node.state.get_improved_num_blocking_vehicles()


class DistanceImprovedBlockingVehiclesHeuristic(ZeroHeuristic):
  """A class used to represent a manhattan distance with improved blocking
        vehicles heuristic problem"""

  def heuristic(self, node: Node):
    """Method to get heuristic.

    Args:
        node (Node):  Node to compute heuristic.

    Returns:
        int: Heuristic value.
    """
    return (
        node.state.get_improved_num_blocking_vehicles() +
        node.state.get_distance_to_exit()
    )
