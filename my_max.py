
def my_max(iterable):
    max_val = None
    if isinstance(iterable, (list, set, tuple)):
        max_val = iterable[0] if isinstance(iterable, (list, tuple)) else next(iter(iterable))
        for item in iterable:
            if item > max_val:
                max_val = item
    return max_val
