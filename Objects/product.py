class Product:
    def __init__(self, name, desc, price, quantity=1):
        self.name = name
        self.desc = desc
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return '{"name":"%s", "desc": "%s","price":"%s"' % (self.name, self.desc, self.price)