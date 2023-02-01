""" This module contains rush hour problems. """

from py_search.base import Problem, Node


class NoHeuristicRushHour(Problem):

  def successors(self, node):
    for new_node in node.state.get_next_possible_states():
      path_cost = node.cost() + 1
      yield Node(new_node, node, '', path_cost)
    return

  def goal_test(self, state_node, goal_node=None):
    return state_node.state.is_solved()

  def node_value(self, node):
    return node.cost()
