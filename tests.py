from oceanspp import Graph, shortest_path
import pytest

'''
setup_module(module):
teardown_module(module):
setup_function(function):

In a class:
setup(self): gets run last when a method is called
setup_class(cls):
setup_method(self, method):

'''

class TestShortestPaths:
    obstacle_a = {(1.0, 2.0) : [(4.0, 2.5), (1.0, 8.0)],
                  (4.0, 2.5) : [(1.0, 2.0), (5.0, 3.0)],
                  (5.0, 3.0) : [(4.0, 2.5), (4.5, 5.0)],
                  (4.5, 5.0) : [(5.0, 3.0), (3.0, 5.0)],
                  (3.0, 5.0) : [(4.5, 5.0), (3.0, 7.0)],
                  (3.0, 7.0) : [(3.0, 5.0), (4.0, 7.0)],
                  (4.0, 7.0) : [(3.0, 7.0), (4.0, 8.0)],
                  (4.0, 8.0) : [(4.0, 7.0), (1.0, 8.0)],
                  (1.0, 8.0) : [(1.0, 2.0), (4.0, 8.0)]
                }
    obstacle_b = {(6.0, 1.0) : [(7.0, 2.0), (10.0,1.5)],
                  (7.0, 2.0) : [(6.0, 1.0), (8.0, 6.0)],
                  (8.0, 6.0) : [(7.0, 2.0), (10.0,1.5)],
                  (10.0, 1.5) : [(8.0, 6.0), (6.0, 1.0)]
                }
    op_graph = { (1.0, 2.0) : [(4.0, 2.5), (1.0, 8.0), (6.0, 1.0)],
                 (4.0, 2.5) : [(1.0, 2.0), (5.0, 3.0)],
                 (5.0, 3.0) : [(4.0, 2.5), (6.0, 1.0), (8.0, 6.0), (4.5, 5.0)],
                 (4.5, 5.0) : [(5.0, 3.0), (4.0, 8.0), (6.0, 1.0)],
                 (4.0, 8.0) : [(4.5, 5.0), (1.0, 8.0), (4.0, 7.0), (8.0, 6.0)],
                 (1.0, 8.0) : [(1.0, 2.0), (4.0, 8.0)],
                 (6.0, 1.0) : [(1.0, 2.0), (5.0, 3.0), (4.5, 5.0), (8.0, 6.0), (10.0, 1.5)],
                 (8.0, 6.0) : [(5.0, 3.0), (4.0, 8.0), (6.0, 1.0), (10.0, 1.5)],
                 (10.0, 1.5) : [(8.0, 6.0), (6.0, 1.0)],
                 (4.0, 7.0) : [(4.0, 8.0)]
                }

    def setup_method(self, method):
        self.graph = Graph(obstacle_a, obstacle_b)
        self.op_network = Graph(self.op_graph)

    def test_shortest_path_1(self):
        ship = (10.0, 5.5)
        port = (1.0, 2.0)
        shortest = shortest_path(self.op_network, ship, port)
        assert str(shortest) == '[(10.0, 5.5), (8.0, 6.0), (5.0, 3.0), (4.0, 2.5), (1.0, 2.0)]'

    #def test_visible_vertices(self):
    #    v = (1.0,2.0)
    #    self.op_network.visible_vertices(v, self.graph)
