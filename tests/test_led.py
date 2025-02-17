import pytest
from colorzero import Color


def test_assign_led(pydensha, led_pins):
    assert pydensha._led is None

    pydensha.assign_led(led_pins)

    assert pydensha._led is not None


def test_assign_led_with_invalid_pins(pydensha):
    assert pydensha._led is None

    invalid_pins = {'red': '', 'green': '', 'blue': ''}
    pydensha.assign_led(invalid_pins)

    assert pydensha._led is None


def test_close_led_before_reassignment(mocker, pydensha_init, led_pins):
    spy = mocker.spy(pydensha_init._led, 'close')
    pydensha_init.assign_led(led_pins)

    spy.assert_called_once()


@pytest.mark.parametrize(
    'train_infos', [
        ['平常運転', '平常運転'],
        pytest.param(['平常運転', '遅延'], marks=pytest.mark.xfail),
        pytest.param(['平常運転', 'その他'], marks=pytest.mark.xfail),
    ]
)
def test_turn_on_led_with_green_color(mocker, pydensha_init, train_infos):
    pydensha_init.operate_led(train_infos)

    assert pydensha_init._led.color == Color('green')


@pytest.mark.parametrize(
    'train_infos', [
        ['遅延', '遅延'],
        ['遅延', '平常運転'],
        pytest.param(['遅延', 'その他'], marks=pytest.mark.xfail),
        pytest.param(['平常運転', 'その他'], marks=pytest.mark.xfail),
    ]
)
def test_blink_led_with_yellow_color(mocker, pydensha_init, train_infos):
    spy = mocker.spy(pydensha_init._led, 'blink')
    pydensha_init.operate_led(train_infos)

    spy.assert_called_once_with(
        on_time=1,
        off_time=1,
        on_color=Color('yellow')
    )


@pytest.mark.parametrize(
    'train_infos', [
        ['その他', '運転計画'],
        ['その他', '平常運転'],
        ['その他', '遅延'],
        pytest.param(['遅延', '平常運転'], marks=pytest.mark.xfail),
        pytest.param(['平常運転', '平常運転'], marks=pytest.mark.xfail),
    ]
)
def test_blink_led_with_red_color(mocker, pydensha_init, train_infos):
    spy = mocker.spy(pydensha_init._led, 'blink')
    pydensha_init.operate_led(train_infos)

    spy.assert_called_once_with(
        on_time=1,
        off_time=1,
        on_color=Color('red')
    )


@pytest.mark.parametrize(
    'train_infos', [
        ['平常運転', None],
        [None, None],
        pytest.param(['平常運転', '遅延'], marks=pytest.mark.xfail),
    ]
)
def test_unchanging_led_state(mocker, pydensha_init, train_infos):
    spy_blink = mocker.spy(pydensha_init._led, 'blink')
    pydensha_init.operate_led(train_infos)

    assert pydensha_init._led.color != Color('green')
    assert spy_blink.call_count == 0
