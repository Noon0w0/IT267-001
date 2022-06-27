class Student:
    def __init__(self,stuid,name,major) -> None:
        self._stuid = stuid
        self._name = name
        self._major = major

    def _displayNameAndMajor(self):
        print("Name: ", self._name)
        print("Major: ", self._major)
