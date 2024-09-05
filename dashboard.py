from data_collection import DataCollector
from disaster_prediction import Predictor
from resource_allocation import AllocationManager
from emergency_routing import Graph
import numpy as np

class Dashboard:
    def __init__(self):
        self.data_collector = DataCollector()
        self.predictor = Predictor()
        self.allocation_manager = AllocationManager()
        self.graph = Graph()

        # Example training data (replace with actual historical data)
        X_train = np.array([[15], [18], [20], [25]])
        y_train = np.array([0, 0, 1, 1])

        # Train the predictor model
        self.predictor.train_model(X_train, y_train)

        # Add nodes and edges to the graph
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('B', 'C', 2)

    def run(self):
        print("Collecting data...")
        self.data_collector.collect_data()
        print("Predicting disaster...")
        prediction = self.predictor.predict_disaster(self.data_collector.data_points[0])
        print("Prediction:", prediction)
        print("Allocating resources...")
        self.allocation_manager.allocate_resources(prediction)
        print("Finding shortest path...")
        shortest_distance = self.graph.shortest_path('A', 'C')
        print("Shortest Distance:", shortest_distance)

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
