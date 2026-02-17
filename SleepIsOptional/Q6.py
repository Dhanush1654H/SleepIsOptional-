def convert_temperature(value: float, unit: str) -> float | str:
    if unit == 'C':
        result = (value * 9/5) + 32
        return round(result, 1)
    elif unit == 'F':
        result = (value - 32) * 5/9
        return round(result, 1)
    else:
        return "Invalid Unit"
