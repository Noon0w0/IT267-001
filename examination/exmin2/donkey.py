from Horse import Horse
class Donkey:
    def __init__(self,age,weight) -> None:
        self.age = age
        self.weight = weight
    
    def sound(self,sound):
        self.sound = sound

    def show_info(self):
        print(f'sound : {self.sound}')