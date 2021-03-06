#lightswitch_oop.py
class LightSwitch():
    def __init__(self) -> None:
        self.switch_status = False

    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show(self):
        print(f"status = {self.switch_status}")

#สร้างวัตถุ(OBJECT) จากแม่พิมพ์(CLASS)
switch_obj = LightSwitch()

#เรียกใช้เมธอด/ฟังชั่น
switch_obj.show() #False
switch_obj.turnon()
switch_obj.show() #Ture
switch_obj.turnoff()
switch_obj.show() #False
switch_obj.turnoff()
