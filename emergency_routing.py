import heapq

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, value):
        self.nodes[value] = value
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))  # Assuming undirected graph

    def shortest_path(self, start, end):
        # Check if the nodes exist
        if start not in self.nodes or end not in self.nodes:
            raise KeyError(f"One or both of the nodes '{start}' and '{end}' are not present in the graph.")
        
        queue = []
        heapq.heappush(queue, (0, self.nodes[start]))
        distances = {node: float('infinity') for node in self.nodes}
        distances[start] = 0
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
        return distances[end]

# Example usage
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_edge('A', 'B', 1)
graph.add_edge('B', 'C', 2)
shortest_distance = graph.shortest_path('A', 'C')
print("Shortest Distance:", shortest_distance)
