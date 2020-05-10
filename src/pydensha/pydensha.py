from gpiozero import RGBLED


def _exc_attr_err(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AttributeError:
            pass
    return wrapper


class PyDensha:
    def __init__(self, led_pins=None):
        self._led = None

        self.assign_led(led_pins)

    @_exc_attr_err
    def assign_led(self, led_pins):
        self._close_led()

        self._led = RGBLED(
            red=led_pins.get('red'),
            green=led_pins.get('green'),
            blue=led_pins.get('blue')
        )

    @_exc_attr_err
    def _close_led(self):
        self._led.close()
