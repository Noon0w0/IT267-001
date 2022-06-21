
bird_type = 'Parrot'
class Bird:
    #Class variable
    bird_name = 'Pater'
    
    def __init__(self,color) -> None:
        #
        self.color = color

        #local varable
        country = 'Thailand'
        print(country)

    def show(self):
        return f'{bird_type}{Bird.bird_name} has {self.color}'

if __name__ == '__main__':
    print(f'***** {bird_type} *****') #เรียกใช้ golble variable
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())

#เรีนก class variable 
#print(bird_name) error

#เรีนก class variable 
#ชื่อคราส.class_variable
print(my_bird.bird_name)

# ชื่อวัตถุ.class variable
print(my_bird.bird_name)

#เรียก instance variable
#prin(bird_color) error

# ชื่อวัตถุ.intance_variable
print(my_bird.color)