class Vehicle:
    def __init__(self,make,model,color):
        self.make = make
        self.color = color
        self.model = model
        def move(self):
            print("starts moving")
        def hoot(self):
            print("honk honk")

class Bus (Vehicle):
    def __init__(self,make,model,color,capacity):
        super().__init__(make,model,color)
        self.capacity = capacity
    def start_bording(self):
        print("The bus is now loading")

class Lorry(Vehicle):
    def __init__(self,make,model,color,max_load):
        super().__init__(make,model,color)
        self.max_load=max_load
    def load(self):
        print("started loading")


