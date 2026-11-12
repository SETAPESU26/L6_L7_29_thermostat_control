
from hypothesis import given, strategies as st
from thermostat_control import (
    parse_setpoint,
    average_temperature,
    schedule_slot
)


# Test 1: Fuzz parse_setpoint()
@given(st.one_of(st.text(), st.none()))
def test_parse_setpoint_no_crash(s):
    try:
        result = parse_setpoint(s)
        assert isinstance(result, float)
    except (ValueError, TypeError, IndexError):
        pass


# Test 2: Fuzz average_temperature()
@given(st.one_of(st.text(), st.none()))
def test_average_temperature_no_crash(s):
    try:
        result = average_temperature(s)
        assert isinstance(result, float)
    except (ValueError, TypeError, ZeroDivisionError):
        pass


# Test 3: Fuzz schedule_slot()
@given(st.one_of(st.text(), st.none()))
def test_schedule_slot_no_crash(s):
    try:
        result = schedule_slot(s)
        assert isinstance(result, str)
    except (ValueError, TypeError, IndexError):
        pass
