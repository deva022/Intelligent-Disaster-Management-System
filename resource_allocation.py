class ResourceAllocator:
    def __init__(self):
        # Initialize resources available in the system
        self.rescue_teams = 10  # Number of available rescue teams
        self.basic_medical_supplies = 100  # Units of basic medical kits
        self.advanced_medical_supplies = 50  # Units of advanced medical kits
        self.food_and_water_kits = 200  # Units of food and water supplies
        self.heavy_equipment = 5  # Available heavy machinery (e.g., bulldozers)
        self.shelter_materials = 50  # Tents, blankets, etc.
        self.emergency_vehicles = 10  # Available ambulances or rescue vehicles

    def allocate_resources(self, severity):
        if severity == "mild":
            print("Allocating resources for a mild disaster...")
            self.allocate_rescue_teams(2)
            self.allocate_medical_supplies(basic=True, quantity=10)
            self.allocate_food_and_water(20)
            self.allocate_shelter_materials(10)

        elif severity == "moderate":
            print("Allocating resources for a moderate disaster...")
            self.allocate_rescue_teams(5)
            self.allocate_medical_supplies(basic=False, quantity=20)
            self.allocate_food_and_water(50)
            self.allocate_shelter_materials(20)
            self.allocate_emergency_vehicles(2)

        elif severity == "severe":
            print("Allocating resources for a severe disaster...")
            self.allocate_rescue_teams(8)
            self.allocate_medical_supplies(basic=False, quantity=40)
            self.allocate_food_and_water(100)
            self.allocate_shelter_materials(30)
            self.allocate_heavy_equipment(3)
            self.allocate_emergency_vehicles(5)
        else:
            raise ValueError("Unknown severity level!")

    # Methods for allocating different resources
    def allocate_rescue_teams(self, quantity):
        print(f"Allocating {quantity} rescue teams.")
        self.rescue_teams -= quantity

    def allocate_medical_supplies(self, basic=True, quantity=10):
        if basic:
            print(f"Allocating {quantity} units of basic medical supplies.")
            self.basic_medical_supplies -= quantity
        else:
            print(f"Allocating {quantity} units of advanced medical supplies.")
            self.advanced_medical_supplies -= quantity

    def allocate_food_and_water(self, quantity):
        print(f"Allocating {quantity} food and water kits.")
        self.food_and_water_kits -= quantity

    def allocate_heavy_equipment(self, quantity):
        print(f"Allocating {quantity} units of heavy equipment.")
        self.heavy_equipment -= quantity

    def allocate_shelter_materials(self, quantity):
        print(f"Allocating shelter materials for {quantity} people.")
        self.shelter_materials -= quantity

    def allocate_emergency_vehicles(self, quantity):
        print(f"Allocating {quantity} emergency vehicles.")
        self.emergency_vehicles -= quantity
