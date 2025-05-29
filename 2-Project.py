class FactoryOrders:
    def __init__(self, name):
        self.name = name
        self.orders = [[0] for _ in range(2)]  # ماتریس برای کالا ۰ و ۱ هر کرخانه

    def add_order(self, part_id, quantity):
        if part_id in [0, 1]:
            self.orders[part_id][0] += quantity
            print(f"Added {quantity} units of part {part_id} to {self.name}.")
        else:
            print("Invalid part number. Only 0 or 1 allowed.")

    def print_orders(self):
        print(f"\nOrders for {self.name}:")
        for i in range(2):
            print(f"Part {i}: {self.orders[i][0]} units")


class OrderManager:
    def __init__(self, factory1: FactoryOrders, factory2: FactoryOrders):
        self.factory1 = factory1
        self.factory2 = factory2

    def compare_factories(self):
        print("\nComparing orders between factories:")
        for i in range(2):
            qty1 = self.factory1.orders[i][0]
            qty2 = self.factory2.orders[i][0]

            if qty1 > qty2:
                print(f"Part {i}: {self.factory1.name} has more orders ({qty1} > {qty2})")
            elif qty2 > qty1:
                print(f"Part {i}: {self.factory2.name} has more orders ({qty2} > {qty1})")
            else:
                print(f"Part {i}: Both factories have equal orders ({qty1} = {qty2})")




factory1 = FactoryOrders("Factory 1")
factory2 = FactoryOrders("Factory 2")

while True:
    print("\nPlace a new order")
    factory_num = input("Enter factory number (1 or 2, or 'q' to quit): ").strip()
    if factory_num.lower() == 'q':
        break

    if factory_num not in ['1', '2']:
        print("Invalid factory number.")
        continue

    try:
        part_id = int(input("Enter part number (0 or 1): "))
        quantity = int(input("Enter quantity to order: "))

        if factory_num == '1':
            factory1.add_order(part_id, quantity)
        else:
            factory2.add_order(part_id, quantity)
    except ValueError:
        print("Please enter valid numbers.")


factory1.print_orders()
factory2.print_orders()


manager = OrderManager(factory1, factory2)
manager.compare_factories()
