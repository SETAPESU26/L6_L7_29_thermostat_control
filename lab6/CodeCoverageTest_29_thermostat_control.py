
from thermostat_control import target_temperature, hvac_action, energy_alert


# TARGET TEMPERATURE BRANCHES

def test_away_branch():
    assert target_temperature("away", True, 12) == 16

def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18

def test_sleep_after_22():
    assert target_temperature("sleep", True, 22) == 18

def test_sleep_during_day():
    assert target_temperature("sleep", True, 12) == 20

def test_unoccupied_branch():
    assert target_temperature("home", False, 12) == 18

def test_morning_branch():
    assert target_temperature("home", True, 6) == 22

def test_morning_boundary():
    assert target_temperature("home", True, 9) == 20

def test_evening_branch():
    assert target_temperature("home", True, 17) == 21

def test_evening_boundary():
    assert target_temperature("home", True, 22) == 20

def test_normal_branch():
    assert target_temperature("home", True, 12) == 20


# HVAC ACTION BRANCHES

def test_idle_branch():
    assert hvac_action(20, 20.5, 10) == "idle"

def test_heat_boost_branch():
    assert hvac_action(18, 22, 4) == "heat_boost"

def test_heat_branch():
    assert hvac_action(18, 22, 5) == "heat"

def test_cool_boost_branch():
    assert hvac_action(25, 20, 31) == "cool_boost"

def test_cool_branch():
    assert hvac_action(25, 20, 30) == "cool"


# ENERGY ALERT BRANCHES

def test_empty_readings_branch():
    assert energy_alert([], 10) == "ok"

def test_all_readings_within_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"

def test_readings_equal_half():
    assert energy_alert([12, 15, 5, 8], 10) == "warning"

def test_critical_branch():
    assert energy_alert([12, 15, 20], 10) == "critical"

def test_reading_below_limit():
    assert energy_alert([5, 12, 8], 10) == "warning"
