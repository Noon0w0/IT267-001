class Customer:
    def __init__(self) -> None:
        self.name = ''
        self.address = ''
        self.phone = ''

    def new_customer(self):
        self.name = input('Enter Customer Name: ')
        self.address = input('Enter Customer Address: ')
        self.phone = input('Enter Customer Phone: ')

    def cus_info(self):
        return f'name: {self.name}\naddress: {self.address}\nphone: {self.phone}'