class Student:
    def __init__(self,stuid,name,major) -> None:
        self._stuid = stuid
        self._name = name
        self.major = major

    def displayNameAndMajor(self):
        print(f'Name: {self._name}')
        print(f'Major: {self.major}')
