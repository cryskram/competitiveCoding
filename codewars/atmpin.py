def validate_pin(pin: str) -> bool:
    if len(pin) == 4 or len(pin) == 6:
        return pin.isnumeric()
    return False
