#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyGraph is a simple module that with the help of it we can get the shortest path between two vertices in an undirected
graph and we are also able to get all the possible paths between two specified vertices
"""
import sys

__author__ = "Hossein Bahrami Nekoo"
__version__ = "0.1.0"
__license__ = "MIT"

class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def __generate_edges(self):

        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def shortest_path(self, vertex1, vertex2):

        v = self.vertices()
        smallest_paths = []
        paths = self.find_all_paths(vertex1,vertex2)
        smallest = sorted(paths, key=len)[0]

        return smallest

if __name__ == "__main__":

   g = { "A" : ["B", "D", "H"],
         "B" : ["C", "D", "A"],
         "C" : ["B", "F", "D"],
         "D" : ["A","B","C","E"],
         "E" : ["H", "F","D"],
         "F" : ["C","G","E"],
         "G" : ["F","H"],
          "H" : ["A","E","G"]
        }

   graph = Graph(g)

   if sys.argv[1] != '--SP' and sys.argv[1] != '--AP':
       print('syntax error : correct usage is graph.py [--SP|--AP] [start_vertex] [end_vertex]')
       sys.exit(0)
   if len(sys.argv) < 4 or len(sys.argv) > 4:
       print('syntax error : correct usage is graph.py [--SP|--AP] [start_vertex] [end_vertex]')
       sys.exit(0)
   if g.get(sys.argv[2]) == None:
       print(sys.argv[2]+' does not exist in the graph')
       exit(0)
   if g.get(sys.argv[3]) == None:
       print(sys.argv[3]+' does not exist in the graph')
       exit(0)

   if sys.argv[1] == '--SP':
       print('Shortest path between '+sys.argv[2]+' and '+sys.argv[3]+' is:')
       print(graph.shortest_path(sys.argv[2], sys.argv[3]))

   if sys.argv[1] == '--AP':
       print('All paths from '+sys.argv[2]+' and '+sys.argv[3]+' is:')
       print(graph.find_all_paths(sys.argv[2], sys.argv[3]))

