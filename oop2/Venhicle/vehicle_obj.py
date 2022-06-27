#create bus object
from bus import Bus

#create motocycle object
from motorcycle import Motocycle

bus = Bus("Bus",4120,"v1234")
#bus.set_color = 'Blue'
bus.set_color('Blue')
#bus.set_capacity = 34
bus.set_capacity(34)
bus.bus_detail()

bike = Motocycle("Motocycle",2,100,"v5678")
#bike.cc = 1200
bike.set_cc(1200)
bike.bike_detlie()