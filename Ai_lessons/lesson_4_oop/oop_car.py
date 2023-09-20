
class Car:
    def __init__(self, name, color, model, top_speed, price) -> None:
        self.name = name
        self.color = color
        self.model = model
        self.top_speed = top_speed
        self.price = price
    
    def vat(self):
        vat = self.price * 15 / 100
        return f" Vat value is : {vat} S.R"
    
     


car1 = Car(name="camry", color="red", model=2020, top_speed=220, price=20000)


print(car1.vat())
