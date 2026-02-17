def get_ticket_price(age: int, is_student: bool) -> int:
    if age < 12:
        return 8
    elif age >= 65:
        return 10
    else:
        return 12 if is_student else 15
