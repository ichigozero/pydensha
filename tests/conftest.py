import pytest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory, MockPWMPin

from pydensha import PyDensha


@pytest.yield_fixture
def mock_factory(request):
    save_factory = Device.pin_factory
    Device.pin_factory = MockFactory()
    yield Device.pin_factory

    if Device.pin_factory is not None:
        Device.pin_factory.reset()
        Device.pin_factory = save_factory


@pytest.fixture
def pwm(request, mock_factory):
    mock_factory.pin_class = MockPWMPin


@pytest.fixture(scope='module')
def led_pins():
    return {
        'red': 4,
        'blue': 17,
        'green': 27
    }


@pytest.fixture
def pydensha(mock_factory, pwm):
    return PyDensha()


@pytest.fixture
def pydensha_init(mock_factory, pwm, led_pins):
    return PyDensha(led_pins)
