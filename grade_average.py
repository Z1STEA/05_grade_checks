def calculate_average(mark_one, mark_two):
    """Calculate the average of two marks."""
    if type(mark_one) is not int or type(mark_two) is not int:
        raise TypeError("invalid argument type")

    if mark_one < 0 or mark_one > 100 or mark_two < 0 or mark_two > 100:
        raise ValueError("argument outside permitted range")

    return (mark_one + mark_two) / 2
