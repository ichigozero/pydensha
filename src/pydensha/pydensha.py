from gpiozero import RGBLED
from gpiozero.exc import PinInvalidPin
from colorzero import Color


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

        try:
            self._led = RGBLED(
                red=led_pins.get('red'),
                green=led_pins.get('green'),
                blue=led_pins.get('blue')
            )
        except PinInvalidPin:
            pass

    @_exc_attr_err
    def _close_led(self):
        self._led.close()

    @_exc_attr_err
    def operate_led(self, train_infos,
                    on_time=1, off_time=1):
        if all(train_info == '平常運転' for train_info in train_infos):
            self._led.color = Color('green')
        elif '遅延' in train_infos:
            if not any(train_info != '平常運転' and
                       train_info != '遅延' for train_info in train_infos):
                self._led.blink(
                    on_time=on_time,
                    off_time=off_time,
                    on_color=Color('yellow')
                )
        else:
            self._led.blink(
               on_time=on_time,
               off_time=off_time,
               on_color=Color('red')
            )
