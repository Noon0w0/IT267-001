class Horse:
    def __init__(self,max_height,name,color) -> None:
        self.max_height = max_height
        self.name = name
        self.color = color

    def run(self,run):
        self.run = run

    def show_name(self,show_name):
        self.show_name = show_name

    def show_info(self):
        print('=============')
        print(f'name: {self.name}')
        print(f'color: {self.color}')
        print(f'max : {self.max_height}')