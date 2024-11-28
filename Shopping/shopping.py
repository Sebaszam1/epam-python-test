class Shopping:
    def __init__(self):
        self.items = {'apple': 5, 'corn': 7, 'blueberries': 10}
    
    def add_item(self, item, price):
            self.items[item] = price
            print(f"The item {item} has been created or updated")
    
    def get_all_items(self):
         return self.items
    
    def get_price(self, item):
        if item in self.items:
            return self.items[item]
        return f"The item '{item}' does not exist"
    

    
class Taxes:
    TAX=0.07

    @classmethod
    def modify_tax(cls, new_tax):
         cls.TAX = new_tax
         return f"The tax has been updated"

    @classmethod
    def get_tax(cls):
        return cls.TAX
    
class Total:
     
     def get_total(costs, bought_items, tax_rate):
        total=0
        
        for item in bought_items:
            if item in costs: 
                price = costs[item] 
                total += price
        total_with_tax = total * (1 + tax_rate)
        return round(total_with_tax, 2)