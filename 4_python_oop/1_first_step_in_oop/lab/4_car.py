class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car1 = Car("Audi", "RS6", "MTM 1000HP")
print(car1.get_info())
