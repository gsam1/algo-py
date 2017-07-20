'''
Implements a one directional graph with a method of searching it using
breadth-first search.
'''
import json
from collections import deque

class Graph:
    '''
    The graph takes two inputs - the json file describing it and the function,
    used for the search to evaluate it
    '''
    def __init__(self, f, func):
        self.desc = json.loads(open(f).read())
        self.func = func

    def search(self):
        search_queue = deque()
        # Initialize with the origin
        search_queue += self.desc['you']['nbh']

        while search_queue:
            item = search_queue.popleft()
            if self.func(item):
                print item + " fulfiles the criteria"
                return True
            else:
                search_queue += self.desc[item]['nbh']





if __name__ == "__main__":
    def mango_seller(name):
        return name[-1] == 'm'

    graph = Graph('bfs_example.json', mango_seller)
    graph.search()
