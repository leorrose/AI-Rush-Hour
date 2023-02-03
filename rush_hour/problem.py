""" This module contains rush hour problems. """

from py_search.base import Problem, Node


class BlockingCarsHeuristicRushHour(Problem):

  def successors(self, node):
    for action, new_node in node.state.get_next_possible_states():
      path_cost = node.cost() + 1
      yield Node(new_node, node, action, path_cost)

  def heuristic(self, node: Node):
    return node.state.get_num_blocking_cars()

  def node_value(self, node):
    return node.cost() + self.heuristic(node)

  def goal_test(self, state_node, goal_node=None):
    return state_node.state.is_solved()


class ZeroHeuristicRushHour(Problem):

  def successors(self, node):
    for action, new_node in node.state.get_next_possible_states():
      path_cost = node.cost() + 1
      yield Node(new_node, node, action, path_cost)

  def heuristic(self, node):
    return 0

  def node_value(self, node):
    return node.cost() + self.heuristic()

  def goal_test(self, state_node, goal_node=None):
    return state_node.state.is_solved()