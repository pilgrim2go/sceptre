def list_join(a, b):
    if a and not isinstance(a, list):
        raise TypeError(f'{a} is not a list')
    if b and not isinstance(b, list):
        raise TypeError(f'{b} is not a list')

    if a is None:
        return b

    if b is not None:
        return a + b

    return a


def dict_merge(a, b):
    if a and not isinstance(a, dict):
        raise TypeError(f'{a} is not a dict')
    if b and not isinstance(b, dict):
        raise TypeError(f'{b} is not a dict')

    if a is None:
        return b

    if b is not None:
        return a.update(b)

    return a


def child_wins(a, b):
    return b
