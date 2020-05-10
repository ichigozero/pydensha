from gpiozero import RGBLED


class PyDensha:
    def __init__(self, led_pins=None):
        self._led = None

        self.assign_led(led_pins)

    def assign_led(self, led_pins):
        try:
            self._led = RGBLED(
                red=led_pins['red'],
                green=led_pins['green'],
                blue=led_pins['blue']
            )
        except TypeError:
            pass
