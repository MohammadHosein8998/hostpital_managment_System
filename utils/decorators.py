


def Error_handler(func_name):
    def inner(*args, **kwargs):
        try:
            result = func_name(*args, **kwargs)
            return True, result
        except Exception as e:
            return False, e

    return inner