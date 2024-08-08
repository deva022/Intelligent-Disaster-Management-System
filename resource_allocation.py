import heapq

class Resource:
    def __init__(self, resource_type, quantity, location):
        self.resource_type = resource_type
        self.quantity = quantity
        self.location = location

class AllocationManager:
    def __init__(self):
        self.resources = []

    def add_resource(self, resource):
        heapq.heappush(self.resources, (resource.quantity, resource))

    def allocate_resources(self):
        while self.resources:
            resource = heapq.heappop(self.resources)[1]
            print(f"Allocating {resource.quantity} units of {resource.resource_type} at {resource.location}")

allocation_manager = AllocationManager()
allocation_manager.add_resource(Resource('medical', 100, 'Warehouse A'))
allocation_manager.add_resource(Resource('food', 200, 'Warehouse B'))
