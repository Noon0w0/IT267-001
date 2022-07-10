class JuiceOrder:
    menu_type = "Juice"
    total = 0

    def __init__(self,menu:str,size:str,price) -> None:
        self.menu = menu
        self.size = size
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
        }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def computer_price(self):
        if self.size == 'B':
            self.price += 5
        else:
            self.price
            JuiceOrder.total = self.price * self.size
    
    
    
    def display_order(self):
        self.check_menu()
        self.display_order()
        return f'{self.menu} ({self.size} * ${self.price} => ${JuiceOrder.total}'

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
        order1 = JuiceOrder("WJ","B")
        order2 = JuiceOrder("OJ")
        order3 = JuiceOrder("PJ","B")

        print(order1.display_order())
        print(order2.display_order())
        print(order3.display_order())