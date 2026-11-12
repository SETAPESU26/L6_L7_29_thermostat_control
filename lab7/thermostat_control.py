
import math


def parse_setpoint(text):
    if not isinstance(text, str) or len(text) < 2:
        raise ValueError("Invalid setpoint")

    unit = text[-1].upper()

    if unit not in ('C', 'F'):
        raise ValueError("Unit must be C or F")

    try:
        value = float(text[:-1])
    except ValueError:
        raise ValueError("Invalid temperature value")

    if not math.isfinite(value):
        raise ValueError("Temperature must be finite")

    if unit == 'F':
        value = (value - 32) * 5 / 9

    return round(value, 1)


def average_temperature(readings_csv):
    if not isinstance(readings_csv, str) or not readings_csv.strip():
        raise ValueError("Readings must be a non-empty CSV string")

    try:
        values = [float(r.strip()) for r in readings_csv.split(',')]

        if not values or any(not math.isfinite(v) for v in values):
            raise ValueError("Invalid temperature readings")

    except ValueError:
        raise ValueError("CSV contains invalid temperature readings")

    return sum(values) / len(values)


def schedule_slot(time_text):
    if not isinstance(time_text, str):
        raise ValueError("Time must be a string")

    parts = time_text.split(':')

    if len(parts) != 2:
        raise ValueError("Time must be in HH:MM format")

    hour_text, minute_text = parts

    if (len(hour_text) != 2 or len(minute_text) != 2
            or not hour_text.isdigit()
            or not minute_text.isdigit()):
        raise ValueError("Time must be in HH:MM format")

    hour = int(hour_text)
    minute = int(minute_text)

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        raise ValueError("Invalid hour or minute")

    if hour < 6:
        return 'night ' + str(minute)

    return 'day ' + str(minute)


def main():
    print("==== Running parse_setpoint ====")
    user_input = input("Enter a setpoint (e.g. 21.5C or 70F): ")
    result = parse_setpoint(user_input)
    print("Setpoint in Celsius:", result)

    print("\n==== Running average_temperature ====")
    user_input = input("Enter sensor readings as CSV (e.g. 20.5,21,22.5): ")
    result = average_temperature(user_input)
    print("Average Temperature:", result)

    print("\n==== Running schedule_slot ====")
    user_input = input("Enter a time as HH:MM (e.g. 07:30): ")
    result = schedule_slot(user_input)
    print("Schedule Slot:", result)


if __name__ == "__main__":
    main()
