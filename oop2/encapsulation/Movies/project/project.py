class Project:
    def __init__(self,name,time,location) -> None:
        self.name = name
        self.time = time
        self.location = location
        

    def show(self):
        print('===== Project =====')
        print(f'name :{self.name}')
        print(f'time :{self.time} months')
        print(f'location :{self.location}')

    def get_budget(self):
        return self.__dudget

    def update_budget(self,budget):
        self.__budget = budget