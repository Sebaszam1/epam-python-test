from shopping import Shopping
from shopping import Taxes
from shopping import Total

def interactive_mode():
    shop = Shopping()
    print("Welcome to the Shopping System!")
    print("Available commands:")
    print(" - add <item> <price>: Add or update an item with its price")
    print(" - list: Show all items and their prices")
    print(" - price <item>: Get the price of an item")
    print(" - tax: Get the current tax rate")
    print(" - set_tax <new_tax>: Update the tax rate")
    print(" - total items bought separate by comma: Calculate the total")

    while True:
        command = input("> ").strip()
        parts = command.split(" ")

        if parts[0] == "add" and len(parts) == 3:
            try:
                item = parts[1]
                price = float(parts[2])
                print(price)
                shop.add_item(item, price)
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
        
        elif parts[0] == "list":
            items = shop.get_all_items()
            print("Items in the store:")
            for item, price in items.items():
                print(f" - {item}: ${price}")
        
        elif parts[0] == "price" and len(parts) == 2:
            item = parts[1]
            print(shop.get_price(item))
        
        elif parts[0] == "tax":
            print(f"Current tax rate: {Taxes.get_tax() * 100:.2f}%")
        
        elif parts[0] == "set_tax" and len(parts) == 2:
            try:
                new_tax = float(parts[1])
                if 0 <= new_tax <= 1:
                    print(Taxes.modify_tax(new_tax))
                else:
                    print("Tax rate must be between 0 and 1.")
            except ValueError:
                print("Invalid tax rate. Please enter a numeric value.")

        elif parts[0] == "total":
            try:
                bought_items = parts[1].split(",")
                bought_items = [item.strip() for item in bought_items]
                print(bought_items)

                tax = Taxes.get_tax()
                items = shop.get_all_items()

                print(Total.get_total(items, bought_items, tax))
            except ValueError:
                print("An error")
        
        else:
            print("Invalid command. Type 'help' for the list of available commands.")

def main():
        interactive_mode()

if __name__ == "__main__":
    main()
