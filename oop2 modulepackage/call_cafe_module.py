from cafe import Dessert,Drink
#แสดงรายการของร้านค้า
dessrt_menu = Dessert()
print(dessrt_menu.sho_dessert())

#แสดงรายการเครื่องดื่มของร้าน
drink_menu = Drink()
print(drink_menu.show_drink)

#เพิ่มรายการเครื่องดื่ม
drink_menu.add_drink('Juice')
drink_menu.add_drink('Smoothy')
print(drink_menu.show_drink())