def test_assign_led(pydensha, led_pins):
    assert pydensha._led is None
    pydensha.assign_led(led_pins)
    assert pydensha._led is not None
