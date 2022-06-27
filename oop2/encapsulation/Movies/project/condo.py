from project import Project
class Condo(Project):
    def __init__(self, name, time, location,budget,type) -> None:
        super().__init__(name, time, location)
        self.type = 'condo'
        self.__budget = budget

    def show(self):
        super().show()
        print(f'type :{self.type}')
        print(f'condo budget :{self.get_budget} MB')
        print(f'project budget :{self.get_budget} MB')