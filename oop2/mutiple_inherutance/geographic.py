class Geographic:
    def setcordinate(self,lat,long:float):
        self.latitude = lat
        self.longitude = long

    def getcordinate(self):
        return f'latitude: {self.latitude}, longitude: {self.longitude}'

    def gettimezone(self):
        timezone = round(self.longitude/12 - 1)
        if timezone > 0:
            return f'+ {timezone}'
        else:
            return f'{timezone}'

    def getclimate(self):
        if self.latitude <= 66.5 or self.latitude >= 66.5:
            return 'Polar zone'
        elif self.latitude <= 66.5 or self.latitude >= 66.5:
            return 'Temperature zone'
        else:
            return 'Tropical zone'