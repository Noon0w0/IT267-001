class Area:
    def __init__(self,base,high) -> None:
        self.__base = base
        self.__high = high



    
    #getter
    @property
    def base(self):
        return self.__base
    @property
    def  high(self):
        return self.__high

    @base.setter
    def base(self,value):
        self.__base = value

    def compute_area(self):
        return (0.5 * self.base * self.high)