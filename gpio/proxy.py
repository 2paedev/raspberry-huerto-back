import datetime
from .client import ClientGPIO


class ProxyGPIO():

    def save_humidity_air():
        created = datetime.datetime.now()
        value = ClientGPIO.humidity_air()
        data = {
            'created': created,
            'value': value,
        }

    def save_humidity_ground():
        created = datetime.datetime.now()
        value = ClientGPIO.humidity_ground()
        data = {
            'created': created,
            'value': value,
        }

    def save_temperature_air():
        created = datetime.datetime.now()
        value = ClientGPIO.temperature_air()
        data = {
            'created': created,
            'value': value,
        }
