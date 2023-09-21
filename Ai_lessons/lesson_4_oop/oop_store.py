class Store:
    def __init__(self, device, count, price) -> None:
        self.device = device
        self.count = count
        self.price = price
    
    def sell(self, quantity):
        ...



iphone = Store("iphone", 15, 3500)

iphone.sell(2) # نريد تنفيذ البيع وخصم الكمية 