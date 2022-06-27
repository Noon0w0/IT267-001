from geographic import Geographic
from temperature import Temperature

class Country(Geographic,Temperature):
    def __init__(self,name,area,pop) -> None:
        self.name = name
        self.area = area
        self.population = pop

    def getpopulationdensity(self):
        return self.population / self.area

    def showdetail(self):
        print(f'Country: {self.name}')
        #สถานที่ตั้ง latitude และ longtidude
        print(f'Location: {self.getcordinate()}')
        #แสดงขนาดพื้นที่,จำนวนประชากร และความหนาแน่นของประชากร
        print(f'Population: {self.population}')
        print(f'Area: {self.area}')
        print(f'Density: {self.getpopulationdensity()}')
        
        #Time Zone, Climate, Temperature, Weather
        print(f'Time Zone: {self.gettimezone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelcius()}')
        print(f'Temperature(F): {self.getfahrenheit()}')
        print(f'Weather: {self.getweather()}')

        print('*******************************')