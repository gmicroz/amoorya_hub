class Store:
    def __init__(self, device, count, price) -> None:
        self.device = device
        self.count = count
        self.price = price
    
    def sell(self, quantity):
        self.count -= quantity
        print("Current Storage : ", self.count)



iphone = Store("iphone", 15, 3500)


iphone.sell(5) # نريد تنفيذ البيع وخصم الكمية 

