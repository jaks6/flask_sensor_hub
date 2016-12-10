from sense_hat import SenseHat

sense = SenseHat()

class sensordata:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def get_values():
    d = sensordata(
    	temp_humidity_sensor=sense.get_temperature_from_humidity(),
    	temp_pressure_sensor=sense.get_temperature_from_pressure(),
    	humidity=sense.get_humidity(),
    	pressure=sense.get_pressure())
    return d

def avg_temp():
	return (sense.get_temperature_from_humidity() + sense.get_temperature_from_pressure() ) / 2