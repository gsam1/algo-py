'''
Implementation of Dijkstra's Algorithm for finding the path in a graph
with the lowest value.
Same as breadth-first search - input is a JSON. The output will be a path dict.
'''
import json

def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

class Weighted_Graph:
    def __init__(self, f):
        self.desc = json.loads(open(f).read())

    def lowcost_path(self,start_node):
        costs = {}
        for key in self.desc.keys():
            if key in self.desc[start_node]['weights'].keys():
                costs[key] = self.desc[start_node]['weights'][key]
            else:
                costs[key] = float('inf')

        parents = {}
        for key in self.desc.keys():
            parents[key] = self.desc[key]['parent']

        processed = []

        node = find_lowest_cost_node(costs, processed)

        while node is not None:
            cost = costs[node]
            neighbors = self.desc[node]['weights']
            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if costs[n] < new_cost:
                    costs[n] = new_cost
                    parents[n] = node

            processed.append(node)
            node = find_lowest_cost_node(costs, processed)

        return costs





if __name__ == "__main__":
    wgraph = Weighted_Graph('da_example.json')
    print wgraph.lowcost_path('start')
