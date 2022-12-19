def check_number_input(string: str, minimum: int = None, maximum: int = None) -> bool:
    """
    This function check if the string is convertible into integer
    If minimum and/or maximum are given, check also if it's between them
    :param string: The string that will be checked for a number
    :param minimum: The minimum the string have to respect
    :param maximum: The maximum the string have to respect
    :returns: True if the string is convertible to digit and respect the minimum and the maximum
    """
    if not string.isdigit():
        return False
    if maximum is not None and minimum is not None:
        return maximum >= int(string) >= minimum
    elif maximum is not None:
        return maximum >= int(string)
    elif minimum is not None:
        return int(string) >= minimum
    return True
