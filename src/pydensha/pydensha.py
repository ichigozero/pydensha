from gpiozero import RGBLED


class PyDensha:
    def __init__(self, led_pins=None):
        self._led = None

        self.assign_led(led_pins)

    def assign_led(self, led_pins):
        self._close_led()

        try:
            self._led = RGBLED(
                red=led_pins.get('red'),
                green=led_pins.get('green'),
                blue=led_pins.get('blue')
            )
        except AttributeError:
            pass

    def _close_led(self):
        try:
            self._led.close()
        except AttributeError:
            pass
