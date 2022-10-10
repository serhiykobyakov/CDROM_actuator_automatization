""" ShutterCD Arduino device class template """

__version__ = '10.10.2022'
__author__ = 'Serhiy Kobyakov'

from arduino_device import ArduinoDevice


class ShutterCD(ArduinoDevice):
    """ ShutterCD Arduino device class template """
    # define the device name:
    # this is the string with which the device responds to b'?' query
    _device_name = "ShutterCD"

    def __init__(self, comport):
        # repeat assigning class variables, so they are visible in self.__dict__:
        self._device_name = self._device_name

        # read the device parameters from INI file
        # all except COMPORTSPEED, READTIMEOUT, WRITETIMEOUT, LONGREADTIMEOUT and SHORTESTTIMEBETWEENREADS:
        # config = configparser.ConfigParser()
        # config.read(self._device_name + '.INI')
        # self.[some parameter] = config[self._device_name]['some parameter']

        # start serial communication with the device
        # this is the place for the line!
        super().__init__(comport)

        # open the shutter - this is the default init state
        self.send_and_get_late_answer('o')
        self._shutter_open = True

    def __del__(self):
        # open the shutter - this is the default init state
        self.send_and_get_late_answer('o')
        
        # this is the place for the line!
        super().__del__()

    @property
    def is_open(self) -> bool:
        return self._shutter_open

    def open(self):
        """ open shutter """
        if not self._shutter_open:
            answer = self.send_and_get_late_answer('o')
            if answer != '0':
                print(f"Error: got {answer} in reply to \"o\" command!")
            else:
                self._shutter_open = True

    def close(self):
        """ close shutter """
        if self._shutter_open:
            answer = self.send_and_get_late_answer('c')
            if answer != '0':
                print(f"Error: got {answer} in reply to \"c\" command!")
            else:
                self._shutter_open = False
