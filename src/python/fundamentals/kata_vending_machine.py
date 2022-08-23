"""
Vending Machine

Task

In this simple Kata aimed at beginners your task is to recreate a vending
machine. You will have to make a class called VendingMachine with at least one
method called vend. On creation of a new instance of VendingMachine the items
Array and Initial vending machine money is passed. The vend method should take
two arguments 1. Selection code of the item (not case sensitive) and 2. Amount
of money the user inserts into the machine.

An example call of the vend method

machine.vend("A01", 0.90)

where the selected item is A01 and the money given to the machine is 90p

An example of the items Array is below

items = [{'name':"Smarties", 'code':"A01", 'quantity':10, 'price':0.60},
         {'name':"Caramac Bar", 'code':"A02", 'quantity':5, 'price':0.60},
         {'name':"Dairy Milk", 'code':"A03", 'quantity':1, 'price':0.65},
         {'name':"Freddo", 'code':"A04", 'quantity':1, 'price':0.25}];

Rules

1. If the money given to the machine is less than the item cost return "Not
enough money!"

2. If the quantity is 0 for an item return "Item Name: Out of stock!". Where
"Item Name" is the name of the item selected.

3. If an item is correctly selected return "Vending Item Name with 9.40 change."
. Where "Item Name" is the name of the item and change if any given.

4. If an item is correctly selected and there is no change needed then return
"Vending Item Name". Where "Item Name" is the name of the item.

5. If an invalid item is selected return "Invalid selection! : Money in vending
machine = 11.20". Where 11.20 is the machines money float.

6. If a selection is successful then the quantity should be updated.

7. The vending machine never runs out of money for simplicity however you will
need to keep track of the amount of money in the machine at anytime (this is not
tested in any of the test cases)

8. Change is always given to 2 decimal places ie 7.00

Good luck and Enjoy
"""


class VendingMachine:
    """A vending machine representation"""

    def __init__(self, items, money: float) -> None:
        self.items = items
        self.money = money

    def vend(self, selection: str, buyer_money: float) -> str:
        """Dispenses the selected item and gives change if needed.

        Args:
            selection (str): The item selected.
            item_money (float): The money provided.

        Returns:
            str: The item and change.
        """

        for idx, item in enumerate(self.items):
            if selection == item["code"]:
                item_name = self.items[idx]["name"]
                item_price = self.items[idx]["price"]

                # Out of stock
                if self.items[idx]["quantity"] == 0:
                    return f"{item_name}: Out of stock!"

                # Not enough money given
                if buyer_money < item_price:
                    return "Not enough money!"

                # Vending item with no change needed
                if buyer_money == item_price:
                    self.items[idx]["quantity"] -= 1
                    self.money += buyer_money
                    return f"Vending {item_name}"

                # Vending item with change
                change = buyer_money - item_price
                self.items[idx]["quantity"] -= 1
                self.money -= change
                return f"Vending {item_name} with {change:.2f} change."

        return (
            f"Invalid selection! : Money in vending machine = {self.money:.2f}"
        )


if __name__ == "__main__":
    items = [
        {"name": "Smarties", "code": "A01", "quantity": 10, "price": 0.60},
        {"name": "Caramac Bar", "code": "A02", "quantity": 5, "price": 0.60},
        {"name": "Dairy Milk", "code": "A03", "quantity": 1, "price": 0.65},
        {"name": "Freddo", "code": "A04", "quantity": 0, "price": 0.25},
    ]

    machine = VendingMachine(items, 100)
    print(machine.vend("A03", 1))

    machine = VendingMachine(items, 0)
    print(machine.vend("A01", 0.60))

    machine = VendingMachine(items, 100)
    print(machine.vend("A02", 0.10))

    machine = VendingMachine(items, 100)
    print(machine.vend("A04", 1.00))

    machine = VendingMachine(items, 100)
    print(machine.vend("B01", 1.00))