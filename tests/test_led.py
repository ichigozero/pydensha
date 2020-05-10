def test_assign_led(pydensha, led_pins):
    assert pydensha._led is None
    pydensha.assign_led(led_pins)
    assert pydensha._led is not None


def test_close_led_before_reassignment(mocker, pydensha_init, led_pins):
    spy = mocker.spy(pydensha_init._led, 'close')
    pydensha_init.assign_led(led_pins)
    spy.assert_called_once()
