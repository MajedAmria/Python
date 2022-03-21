
class Product:
    def __init__(self, name, price, qty, cat):
        self.name= name
        self.price=price
        self.qty=qty
        self.cat=cat

    def add_tax(self, price):
        self.price +=price*0.18
        return self
    def print_product(self):
        print("product Name:" , self.name,"Product Price: " , self.price, "Avaliable QTY: " , self.qty, "Product Categoriy: ", self.cat)

if __name__ == "__main__":
    product = Product('Apple', 10, 15, 'Fruit')
    print(product.add_tax(0.18))
    product.print_product()
    print(__name__)