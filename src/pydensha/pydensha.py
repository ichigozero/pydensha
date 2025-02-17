from colorzero import Color
from gpiozero import RGBLED
from gpiozero.exc import PinInvalidPin


def _ignore_exception(function):
    def wrapper(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except AttributeError:
            pass

    return wrapper


class PyDensha:
    def __init__(self, led_pins=None):
        self._led = None

        self.assign_led(led_pins)

    @_ignore_exception
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

    @_ignore_exception
    def _close_led(self):
        self._led.close()

    @_ignore_exception
    def operate_led(self, train_infos, on_time=1, off_time=1):
        def _are_all_trains_operate_normally(train_infos):
            return all(
                train_info == '平常運転'
                for train_info in train_infos
            )

        def _is_all_train_either_operate_normally_or_delayed(train_infos):
            return all(
                train_info == '平常運転' or
                train_info == '遅延' for train_info in train_infos
            )

        if None not in train_infos:
            if _are_all_trains_operate_normally(train_infos):
                self._led.color = Color('green')
            elif _is_all_train_either_operate_normally_or_delayed(train_infos):
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
