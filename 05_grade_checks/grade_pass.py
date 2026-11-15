def has_passed(score):
    """Check if the score is a pass."""
    if type(score) is not int:
        raise TypeError("invalid argument type")

    if score < 0 or score > 100:
        raise ValueError("argument outside permitted range")

    return score >= 50
