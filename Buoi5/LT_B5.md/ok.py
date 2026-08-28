from abc import ABC, abstractmethod


# 1. Lớp trừu tượng BeverageStore
class BeverageStore(ABC):

    def __init__(self, drink_name, inventory):
        self.drink_name = drink_name
        self.inventory = inventory  # dict chứa: milk, sugar, honey, ice

    @abstractmethod
    def calculate_price(self, quantity):
        pass

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def required_ingredients(self, quantity):
        pass


# 2. Lớp CoffeeStore (Kế thừa BeverageStore)
class CoffeeStore(BeverageStore):

    def __init__(self, drink_name, inventory, coffee):
        super().__init__(drink_name, inventory)
        self.inventory['coffee'] = coffee

    def calculate_price(self, quantity):
        return 25000 * quantity

    def required_ingredients(self, quantity):
        return {
            'milk': 50 * quantity,
            'sugar': 10 * quantity,
            'honey': 5 * quantity,
            'ice': 100 * quantity,
            'coffee': 20 * quantity
        }

    def show(self):
        print(f"Cửa hàng Cà phê: {self.drink_name}")
        print(f"Kho hiện tại: {self.inventory}")


# 3. Lớp JuiceStore (Kế thừa BeverageStore)
class JuiceStore(BeverageStore):

    def __init__(self, drink_name, inventory, fruits):
        super().__init__(drink_name, inventory)
        self.inventory['fruits'] = fruits  # dict trái cây, ví dụ: {"cam": 500, "xoai": 600}

    def calculate_price(self, quantity):
        return 30000 * quantity

    def required_ingredients(self, quantity):
        req = {
            'milk': 50 * quantity,
            'sugar': 10 * quantity,
            'honey': 5 * quantity,
            'ice': 100 * quantity,
            'fruits': {}
        }
        # Mỗi ly cần 200g cho MỖI loại trái cây đang có trong kho
        for fruit, amount in self.inventory['fruits'].items():
            req['fruits'][fruit] = 200 * quantity
        return req

    def show(self):
        print(f"Cửa hàng Nước ép: {self.drink_name}")
        print(f"Kho hiện tại: {self.inventory}")


# 4. Lớp Order (Quản lý đặt hàng)
class Order:

    def __init__(self, order_list, payment):
        self.order_list = order_list  # list các dict dạng: {"drink": BeverageStore, "quantity": int}
        self.payment = payment

    def check_inventory(self):
        # Kiểm tra kho cho từng món trong order
        for item in self.order_list:
            drink = item["drink"]
            quantity = item["quantity"]
            req = drink.required_ingredients(quantity)

            # Kiểm tra nguyên liệu thông thường (milk, sugar, honey, ice, coffee)
            for ing, amount in req.items():
                if ing != 'fruits':
                    if drink.inventory.get(ing, 0) < amount:
                        return False
                else:
                    # Kiểm tra từng loại trái cây
                    for fruit_name, fruit_amount in req['fruits'].items():
                        if drink.inventory['fruits'].get(fruit_name, 0) < fruit_amount:
                            return False
        return True

    def add_drink(self):
        if not self.check_inventory():
            print("Lỗi: Kho không đủ nguyên liệu để thực hiện đơn hàng!")
            return False

        # Nếu đủ nguyên liệu thì tiến hành trừ kho
        for item in self.order_list:
            drink = item["drink"]
            quantity = item["quantity"]
            req = drink.required_ingredients(quantity)

            for ing, amount in req.items():
                if ing != 'fruits':
                    drink.inventory[ing] -= amount
                else:
                    for fruit_name, fruit_amount in req['fruits'].items():
                        drink.inventory['fruits'][fruit_name] -= fruit_amount

        print("Thêm đơn hàng thành công và đã cập nhật kho!")
        return True

    def calculate_total_price(self):
        total = 0
        for item in self.order_list:
            drink = item["drink"]
            quantity = item["quantity"]
            total += drink.calculate_price(quantity)

        print(f"Tổng tiền đơn hàng: {total:,} VNĐ")
        print(f"Tiền khách đưa: {self.payment:,} VNĐ")

        if self.payment >= total:
            print(f"Tiền thừa trả khách: {self.payment - total:,} VNĐ")
        else:
            print(f"Khách còn thiếu: {total - self.payment:,} VNĐ")


# --- THỬ NGHIỆM CHƯƠNG TRÌNH ---
# Khởi tạo kho nguyên liệu dùng chung
inventory_coffee = {'milk': 1000, 'sugar': 500, 'honey': 200, 'ice': 2000}
coffee_store = CoffeeStore("Cà phê Muối", inventory_coffee, coffee=500)

inventory_juice = {'milk': 1000, 'sugar': 500, 'honey': 200, 'ice': 2000}
juice_store = JuiceStore("Nước ép Hỗn hợp", inventory_juice, fruits={"cam": 500, "xoai": 600})

# Hiển thị thông tin kho ban đầu
coffee_store.show()
juice_store.show()
print("-" * 40)

# Tạo đơn hàng gồm 2 ly cà phê và 1 ly nước ép, khách đưa 100.000 VNĐ
my_order = [
    {"drink": coffee_store, "quantity": 2},
    {"drink": juice_store, "quantity": 1}
]

order1 = Order(order_list=my_order, payment=100000)

# Xử lý đơn hàng
if order1.add_drink():
    order1.calculate_total_price()

print("-" * 40)
# Kiểm tra lại kho sau khi bán
coffee_store.show()
juice_store.show()