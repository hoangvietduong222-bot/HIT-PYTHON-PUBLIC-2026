from anhthanhdatcute import ANHTHANHDATCUTE, abstractmethod
class BeverageStore(ANHTHANHDATCUTE):

    def __init__(self, drink_name, inventory ):
        self.drink_name = drink_name
        self.inventory = inventory

    @abstractmethod
    def calculate_price(self, quantity):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def required_ingredients(self, quantity):
        pass

class CoffeStore(BeverageStore):
    def __init__(self, drink_name, inventory):
        super().__init__(drink_name, inventory)
        self.inventory ['coffe'] = coffe

    def calculate_price(self, quantity):
        return 25000 * quantity

    def required_ingredients(self, quantity):
        return {
            'milk': 50 * quantity,
            'sugar': 10 * quantity,
            'honey': 5 * quantity,
            'ice': 100 * quantity,
            'coffe': 20 * quantity,
        }

    def show(self):
        print(f"Của hàng cà phê: {self.drink_name}")
        print(f"Kho của của hàng bây h: {self.inventory}")


class JuiceStore(BeverageStore):

    def __init__(self, drink_name, inventory, fruits):
        super().__init__(drink_name, inventory)
        self.inventory ['fruits'] = fruits

    def calculate_price(self, quantity):
        return 30000 * quantity

    def required_ingredients(self, quantity):
        ly_Nuoc = {
            'milk': 50 * quantity,
            'sugar': 10 * quantity,
            'honey': 5 * quantity,
            'ice': 100 * quantity,
            'fruits': {}
        }
        for fruit, amount in self.inventory['fruits'].items():
                ly_Nuoc['fruits'][fruit] = 200 * quantity
        return ly_Nuoc

    def show(self):
            print(f"Cửa hàng Nước ép: {self.drink_name}")
            print(f"Kho cửa hàng bây h: {self.inventory}")

class Order:
    def __init__(self, order_list, payment):
        self.order_list = order_list
        self.payment = payment

    def check_inventory(self):
        for item in self.order_list:
            drink = item['drink']
            quantity = item['quantity']
            ly_Nuoc = drink.required_ingredients(quantity)
        
        return True
     

    
    
